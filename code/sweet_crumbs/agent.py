"""Model setup and tool-calling loop."""

from langchain.chat_models import init_chat_model
from pydantic import ValidationError

from sweet_crumbs.config import MAX_STEPS, MODEL, PROVIDER
from sweet_crumbs.tools import TOOLS

llm = init_chat_model(MODEL, model_provider=PROVIDER, temperature=0.2)
llm_with_tools = llm.bind_tools(list(TOOLS.values()))


def run_agent(messages: list) -> str:
    """Run the tool-calling loop and return the assistant's final answer."""
    for _ in range(MAX_STEPS):
        response = llm_with_tools.invoke(messages)
        messages.append(response)

        if not getattr(response, "tool_calls", None):
            return response.content if isinstance(response.content, str) else str(response.content)

        for call in response.tool_calls:
            name = call.get("name", "")
            args = call.get("args", {})
            if name not in TOOLS:
                result = f"Unknown tool: {name}"
            else:
                try:
                    result = TOOLS[name].invoke(args)
                except (ValidationError, TypeError, ValueError) as exc:
                    result = f"Tool error: invalid arguments ({exc})."
                except Exception as exc:
                    result = f"Tool error: {type(exc).__name__}: {exc}"

            print(f"  [tool] {name}({args}) -> {result}")
            messages.append({
                "role": "tool",
                "content": str(result),
                "tool_call_id": call.get("id", ""),
            })

    return "Sorry, I could not finish that within the step limit. A human will help you."

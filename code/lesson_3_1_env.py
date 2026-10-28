"""Lesson 3.1: safely read settings from .env."""

import os

from dotenv import load_dotenv
from sweet_crumbs.config import PROJECT_ROOT

load_dotenv(PROJECT_ROOT / ".env")

provider = os.getenv("PROVIDER", "ollama")
model = os.getenv("MODEL", "llama3.2:latest")
api_key = os.getenv("ANTHROPIC_API_KEY", "")

print(f"Provider: {provider}, model: {model}")
if not api_key:
    print("No Anthropic API key set.")
else:
    print(f"Anthropic API key loaded ({len(api_key)} characters).")

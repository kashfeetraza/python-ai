"""Central app settings loaded from .env."""

import os
from pathlib import Path

from dotenv import load_dotenv

# Locate .env at the code/project root, regardless of the current directory.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

PROVIDER = os.getenv("PROVIDER", "ollama").strip()
MODEL = os.getenv("MODEL", "llama3.2:latest").strip()
MAX_STEPS = int(os.getenv("MAX_STEPS", "5"))
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "").strip()
DATA_FILE = PROJECT_ROOT / "business.json"

if PROVIDER == "anthropic" and not ANTHROPIC_API_KEY:
    raise SystemExit(
        "PROVIDER is anthropic but ANTHROPIC_API_KEY is empty. Add it to .env."
    )


# Lesson 3.3: External API settings
RATES_URL = os.getenv(
    "RATES_URL",
    "https://open.er-api.com/v6/latest",
)
GEOCODE_URL = os.getenv(
    "GEOCODE_URL",
    "https://geocoding-api.open-meteo.com/v1/search",
)
WEATHER_URL = os.getenv(
    "WEATHER_URL",
    "https://api.open-meteo.com/v1/forecast",
)
HTTP_TIMEOUT = float(os.getenv("HTTP_TIMEOUT", "10"))
CACHE_SECONDS = int(os.getenv("CACHE_SECONDS", "3600"))
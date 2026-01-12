import os
from dotenv import load_dotenv
load_dotenv()

HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "8000"))
LOG_LEVEL = os.getenv("LOG_LEVEL", "info")

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
MONGODB_DB = os.getenv("MONGODB_DB", "parser_api")

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

PLAYWRIGHT_HEADLESS = os.getenv("PLAYWRIGHT_HEADLESS", "true").lower() in ("1", "true", "yes")
PLAYWRIGHT_BROWSER_POOL_SIZE = int(os.getenv("PLAYWRIGHT_BROWSER_POOL_SIZE", "2"))

HTTP_PROXY = os.getenv("HTTP_PROXY", "") or os.getenv("http_proxy", "")
HTTPS_PROXY = os.getenv("HTTPS_PROXY", "") or os.getenv("https_proxy", "")

CACHE_TTL_SECONDS = int(os.getenv("CACHE_TTL_SECONDS", "86400"))
PLAYER_SEARCH_MAX_LINKS = int(os.getenv("PLAYER_SEARCH_MAX_LINKS", "6"))
PLAYER_SCRAPE_MAX_MATCHES = int(os.getenv("PLAYER_SCRAPE_MAX_MATCHES", "50"))

BETAPI_KEY = os.getenv("BETAPI_KEY", "")

CELERY_TASK_DEFAULT_RETRY_DELAY = int(os.getenv("CELERY_TASK_DEFAULT_RETRY_DELAY", "5"))
CELERY_TASK_MAX_RETRIES = int(os.getenv("CELERY_TASK_MAX_RETRIES", "3"))

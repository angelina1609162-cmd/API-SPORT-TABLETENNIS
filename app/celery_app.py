from celery import Celery
from .config import REDIS_URL
from .logger import logger
celery_app = Celery("parser_api", broker=REDIS_URL, backend=REDIS_URL)
celery_app.conf.update(task_track_started=True, task_acks_late=True, worker_prefetch_multiplier=1)
logger.info("Celery ready")

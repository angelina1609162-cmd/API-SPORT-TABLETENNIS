from pymongo import MongoClient, ASCENDING, DESCENDING
from .config import MONGODB_URI, MONGODB_DB
from .logger import logger

client = MongoClient(MONGODB_URI)
db = client[MONGODB_DB]

matches_col = db["matches"]
jobs_col = db["jobs"]

matches_col.create_index([("source", ASCENDING), ("external_id", ASCENDING)], unique=True, sparse=True)
matches_col.create_index([("player", ASCENDING), ("date", DESCENDING)])
matches_col.create_index([("player", ASCENDING), ("scraped_at", DESCENDING)])
logger.info("MongoDB connected and indexes ensured")

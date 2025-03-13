from tortoise import Tortoise
from config import DATABASE_URL

async def init_db():
    """Initialize the database connection"""
    await Tortoise.init(
        db_url=DATABASE_URL,
        modules={"models": ["models"]}  # Ensure "models" contains your Tortoise ORM models
    )
    await Tortoise.generate_schemas()

async def close_db():
    """Close database connections"""
    await Tortoise.close_connections()

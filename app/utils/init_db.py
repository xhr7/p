import logging
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.db.database import SessionLocal
from app.services import user as user_service
from app.schemas.user import UserCreate

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init_db() -> None:
    """
    Initialize the database with some sample data
    """
    db = SessionLocal()
    try:
        # Create a superuser if it doesn't exist
        user = user_service.get_by_email(db, email="admin@example.com")
        if not user:
            user_in = UserCreate(
                email="admin@example.com",
                username="admin",
                password="admin123",
            )
            user = user_service.create(db, obj_in=user_in)
            # Make the user a superuser using SQLAlchemy text
            db.execute(text(f"UPDATE users SET is_superuser = TRUE WHERE id = {user.id}"))
            db.commit()
            logger.info("Superuser created")
        else:
            logger.info("Superuser already exists")
            
        # Create a regular user if it doesn't exist
        user = user_service.get_by_email(db, email="user@example.com")
        if not user:
            user_in = UserCreate(
                email="user@example.com",
                username="user",
                password="user123",
            )
            user_service.create(db, obj_in=user_in)
            logger.info("Regular user created")
        else:
            logger.info("Regular user already exists")
            
    finally:
        db.close()

if __name__ == "__main__":
    logger.info("Creating initial data")
    init_db()
    logger.info("Initial data created")

# Made with Bob

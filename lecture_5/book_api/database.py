"""
Database configuration module.
Provides SQLAlchemy engine, session factory, and database utilities.
"""
from sqlalchemy import create_engine, pool
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator

# Database URL - using SQLite
DATABASE_URL = "sqlite:///./books.db"

# Create engine with optimizations
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=pool.QueuePool,
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True,
    echo=False
)

# Create session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=Session,
    expire_on_commit=False
)

# Base class for declarative models
Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    """
    Dependency for database session management.
    
    Yields:
        Session: Database session instance
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db() -> None:
    """
    Initialize database - create all tables.
    """
    Base.metadata.create_all(bind=engine)
    print("✅ Database initialized successfully")


# Export for use in other modules
__all__ = ["Base", "engine", "SessionLocal", "get_db", "init_db"]
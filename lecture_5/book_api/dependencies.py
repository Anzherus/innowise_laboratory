"""
Dependencies module for FastAPI.
"""
from database import get_db

# Re-export dependencies from database module
__all__ = ["get_db"]
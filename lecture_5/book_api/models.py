"""
SQLAlchemy data models.
Defines the Book model with validation and indexes.
"""
from sqlalchemy import Column, Integer, String, Index
from sqlalchemy.orm import validates
from database import Base
from typing import Optional
import re
from datetime import datetime


class Book(Base):
    """
    Book model representing a book in the collection.
    """
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), nullable=False, index=True)
    author = Column(String(255), nullable=False, index=True)
    year = Column(Integer, nullable=True, index=True)
    
    # Composite indexes for better query performance
    __table_args__ = (
        Index('ix_books_title_author', 'title', 'author'),
        Index('ix_books_author_year', 'author', 'year'),
    )
    
    @validates('title')
    def validate_title(self, key: str, title: str) -> str:
        """
        Validate book title.
        
        Args:
            key: Field name
            title: Book title to validate
            
        Returns:
            str: Validated title
            
        Raises:
            ValueError: If title is invalid
        """
        if not title or not title.strip():
            raise ValueError("Book title cannot be empty")
        if len(title.strip()) > 255:
            raise ValueError("Book title too long (max 255 characters)")
        return title.strip()
    
    @validates('author')
    def validate_author(self, key: str, author: str) -> str:
        """
        Validate author name.
        
        Args:
            key: Field name
            author: Author name to validate
            
        Returns:
            str: Validated author name
            
        Raises:
            ValueError: If author name is invalid
        """
        if not author or not author.strip():
            raise ValueError("Author name cannot be empty")
        if len(author.strip()) > 255:
            raise ValueError("Author name too long (max 255 characters)")
        
        # Allow any characters in author name (supports all languages)
        return author.strip()
    
    @validates('year')
    def validate_year(self, key: str, year: Optional[int]) -> Optional[int]:
        """
        Validate publication year.
        
        Args:
            key: Field name
            year: Publication year to validate
            
        Returns:
            Optional[int]: Validated year or None
            
        Raises:
            ValueError: If year is invalid
        """
        if year is not None:
            current_year = datetime.now().year
            if year < 1000 or year > current_year + 2:
                raise ValueError(f"Year must be between 1000 and {current_year + 2}")
        return year
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"<Book(id={self.id}, title='{self.title}', author='{self.author}', year={self.year})>"


# Export model for use in other modules
__all__ = ["Book"]

"""
Pydantic schemas for data validation and serialization.
Compatible with Pydantic v2.
"""
from pydantic import BaseModel, Field, field_validator
from typing import Optional, List
from datetime import datetime


class BookBase(BaseModel):
    """Base book schema with common fields."""
    title: str = Field(
        ...,
        min_length=1,
        max_length=255,
        description="Book title",
        examples=["War and Peace"]
    )
    author: str = Field(
        ...,
        min_length=1,
        max_length=255,
        description="Book author",
        examples=["Leo Tolstoy"]
    )
    year: Optional[int] = Field(
        None,
        ge=1000,
        le=datetime.now().year + 2,
        description="Publication year",
        examples=[1869]
    )
    
    @field_validator('title')
    @classmethod
    def validate_title(cls, v: str) -> str:
        """Validate book title."""
        v = v.strip()
        if not v:
            raise ValueError("Book title cannot be empty")
        return v
    
    @field_validator('author')
    @classmethod
    def validate_author(cls, v: str) -> str:
        """Validate author name."""
        v = v.strip()
        if not v:
            raise ValueError("Author name cannot be empty")
        return v
    
    model_config = {
        "from_attributes": True,
        "str_strip_whitespace": True
    }


class BookCreate(BookBase):
    """Schema for creating a new book."""
    pass


class BookUpdate(BaseModel):
    """Schema for updating a book (all fields optional)."""
    title: Optional[str] = Field(
        None,
        min_length=1,
        max_length=255,
        description="Book title",
        examples=["War and Peace"]
    )
    author: Optional[str] = Field(
        None,
        min_length=1,
        max_length=255,
        description="Book author",
        examples=["Leo Tolstoy"]
    )
    year: Optional[int] = Field(
        None,
        ge=1000,
        le=datetime.now().year + 2,
        description="Publication year",
        examples=[1869]
    )
    
    model_config = {
        "from_attributes": True,
        "str_strip_whitespace": True
    }


class BookResponse(BookBase):
    """Schema for book response (includes ID)."""
    id: int = Field(..., description="Unique book identifier")
    
    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "example": {
                "id": 1,
                "title": "War and Peace",
                "author": "Leo Tolstoy",
                "year": 1869
            }
        }
    }


class BooksResponse(BaseModel):
    """Schema for paginated list of books."""
    books: List[BookResponse] = Field(..., description="List of books")
    total: int = Field(..., description="Total number of books")
    page: int = Field(..., description="Current page number")
    page_size: int = Field(..., description="Number of items per page")
    total_pages: int = Field(..., description="Total number of pages")
    
    model_config = {"from_attributes": True}


class SearchQuery(BaseModel):
    """Schema for search parameters."""
    title: Optional[str] = Field(None, description="Search by title")
    author: Optional[str] = Field(None, description="Search by author")
    year: Optional[int] = Field(None, description="Search by year")
    year_from: Optional[int] = Field(None, ge=1000, description="Year from")
    year_to: Optional[int] = Field(None, description="Year to")
    page: int = Field(1, ge=1, description="Page number")
    page_size: int = Field(10, ge=1, le=100, description="Items per page")
    
    model_config = {"from_attributes": True}


# Export all schemas
__all__ = [
    "BookBase",
    "BookCreate",
    "BookUpdate",
    "BookResponse",
    "BooksResponse",
    "SearchQuery"
]

"""
Main FastAPI application for Book Collection API.
"""
from fastapi import FastAPI, Depends, HTTPException, status, Query, Path
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import Optional
import uvicorn

# Import project modules
import database
import schemas
import crud
from dependencies import get_db

# Initialize FastAPI application with metadata
app = FastAPI(
    title="Book Collection API",
    description="A RESTful API for managing book collections",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# Configure CORS for web access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Application lifecycle events
@app.on_event("startup")
async def startup_event():
    """Initialize application on startup."""
    database.init_db()
    print("🚀 Application started and ready!")


@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on application shutdown."""
    print("👋 Application shutting down...")


# Health check endpoint
@app.get(
    "/health",
    summary="API Health Check",
    description="Check if the API is running and healthy",
    tags=["System"]
)
async def health_check():
    """
    Health check endpoint for monitoring.
    
    Returns:
        dict: Status and version information
    """
    return {
        "status": "healthy",
        "version": "1.0.0",
        "service": "Book Collection API"
    }


# Book endpoints
@app.post(
    "/books/",
    response_model=schemas.BookResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Add a new book",
    description="Create a new book record in the collection",
    tags=["Books"]
)
async def create_book(
    book: schemas.BookCreate,
    db: Session = Depends(get_db)
) -> schemas.BookResponse:
    """
    Create a new book.
    
    Args:
        book: New book data
        db: Database session
        
    Returns:
        schemas.BookResponse: Created book
    """
    try:
        db_book = crud.book_crud.create_book(db, book)
        return schemas.BookResponse.model_validate(db_book)
    
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating book: {str(e)}"
        )


@app.get(
    "/books/",
    response_model=schemas.BooksResponse,
    summary="Get all books",
    description="Retrieve all books with pagination support",
    tags=["Books"]
)
async def get_books(
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(10, ge=1, le=100, description="Items per page"),
    db: Session = Depends(get_db)
) -> schemas.BooksResponse:
    """
    Get all books with pagination.
    
    Args:
        page: Page number (starts from 1)
        page_size: Number of books per page (1-100)
        db: Database session
        
    Returns:
        schemas.BooksResponse: List of books with pagination metadata
    """
    try:
        skip = (page - 1) * page_size
        books, total = crud.book_crud.get_books(db, skip=skip, limit=page_size)
        total_pages = (total + page_size - 1) // page_size
        
        return schemas.BooksResponse(
            books=[schemas.BookResponse.model_validate(book) for book in books],
            total=total,
            page=page,
            page_size=page_size,
            total_pages=total_pages
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving books: {str(e)}"
        )


@app.get(
    "/books/{book_id}",
    response_model=schemas.BookResponse,
    summary="Get book by ID",
    description="Retrieve a specific book by its identifier",
    tags=["Books"]
)
async def get_book(
    book_id: int = Path(..., ge=1, description="Book ID"),
    db: Session = Depends(get_db)
) -> schemas.BookResponse:
    """
    Get a book by ID.
    
    Args:
        book_id: Book ID
        db: Database session
        
    Returns:
        schemas.BookResponse: Book data
    """
    db_book = crud.book_crud.get_book(db, book_id)
    
    if not db_book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with ID {book_id} not found"
        )
    
    return schemas.BookResponse.model_validate(db_book)


@app.put(
    "/books/{book_id}",
    response_model=schemas.BookResponse,
    summary="Update book",
    description="Update an existing book's information",
    tags=["Books"]
)
async def update_book(
    book_update: schemas.BookUpdate,
    book_id: int = Path(..., ge=1, description="Book ID"),
    db: Session = Depends(get_db)
) -> schemas.BookResponse:
    """
    Update a book.
    
    Args:
        book_update: New book data
        book_id: Book ID to update
        db: Database session
        
    Returns:
        schemas.BookResponse: Updated book
    """
    try:
        db_book = crud.book_crud.update_book(db, book_id, book_update)
        
        if not db_book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Book with ID {book_id} not found"
            )
        
        return schemas.BookResponse.model_validate(db_book)
    
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error updating book: {str(e)}"
        )


@app.delete(
    "/books/{book_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete book",
    description="Delete a book from the collection",
    tags=["Books"]
)
async def delete_book(
    book_id: int = Path(..., ge=1, description="Book ID"),
    db: Session = Depends(get_db)
):
    """
    Delete a book by ID.
    
    Args:
        book_id: Book ID to delete
        db: Database session
    """
    success = crud.book_crud.delete_book(db, book_id)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with ID {book_id} not found"
        )


@app.get(
    "/books/search/",
    response_model=schemas.BooksResponse,
    summary="Search books",
    description="Search books by title, author, or publication year",
    tags=["Books", "Search"]
)
async def search_books(
    title: Optional[str] = Query(None, description="Search by title"),
    author: Optional[str] = Query(None, description="Search by author"),
    year: Optional[int] = Query(None, ge=1000, description="Search by year"),
    year_from: Optional[int] = Query(None, ge=1000, description="Year from"),
    year_to: Optional[int] = Query(None, description="Year to"),
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(10, ge=1, le=100, description="Items per page"),
    db: Session = Depends(get_db)
) -> schemas.BooksResponse:
    """
    Search books with filters and pagination.
    
    Args:
        title: Filter by title
        author: Filter by author
        year: Filter by year
        year_from: Start of year range
        year_to: End of year range
        page: Page number
        page_size: Items per page
        db: Database session
        
    Returns:
        schemas.BooksResponse: Search results with pagination
    """
    try:
        search_query = schemas.SearchQuery(
            title=title,
            author=author,
            year=year,
            year_from=year_from,
            year_to=year_to,
            page=page,
            page_size=page_size
        )
        
        books, total = crud.book_crud.search_books(db, search_query)
        total_pages = (total + page_size - 1) // page_size if total > 0 else 0
        
        return schemas.BooksResponse(
            books=[schemas.BookResponse.model_validate(book) for book in books],
            total=total,
            page=page,
            page_size=page_size,
            total_pages=total_pages
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error searching books: {str(e)}"
        )


# Catch-all route for undefined endpoints
@app.get("/{full_path:path}", include_in_schema=False)
async def catch_all(full_path: str):
    """Handle all undefined routes."""
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Route /{full_path} not found"
    )


if __name__ == "__main__":
    # Run the application
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info"
    )
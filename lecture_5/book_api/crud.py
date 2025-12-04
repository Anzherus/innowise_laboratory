"""
CRUD (Create, Read, Update, Delete) operations for books.
"""
from sqlalchemy.orm import Session
from sqlalchemy import and_, func
from typing import Optional, List, Tuple
import models
import schemas


class BookCRUD:
    """Class for managing book operations."""
    
    @staticmethod
    def get_book(db: Session, book_id: int) -> Optional[models.Book]:
        """
        Get a book by ID.
        
        Args:
            db: Database session
            book_id: Book ID
            
        Returns:
            Optional[models.Book]: Book instance or None if not found
        """
        return db.query(models.Book).filter(models.Book.id == book_id).first()
    
    @staticmethod
    def get_books(
        db: Session, 
        skip: int = 0, 
        limit: int = 100
    ) -> Tuple[List[models.Book], int]:
        """
        Get list of books with pagination.
        
        Args:
            db: Database session
            skip: Number of records to skip
            limit: Maximum number of records
            
        Returns:
            Tuple[List[models.Book], int]: List of books and total count
        """
        total = db.query(func.count(models.Book.id)).scalar()
        
        books = db.query(models.Book)\
            .order_by(models.Book.id)\
            .offset(skip)\
            .limit(limit)\
            .all()
        
        return books, total
    
    @staticmethod
    def create_book(db: Session, book: schemas.BookCreate) -> models.Book:
        """
        Create a new book.
        
        Args:
            db: Database session
            book: New book data
            
        Returns:
            models.Book: Created book instance
        """
        db_book = models.Book(
            title=book.title,
            author=book.author,
            year=book.year
        )
        
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        
        return db_book
    
    @staticmethod
    def update_book(
        db: Session, 
        book_id: int, 
        book_update: schemas.BookUpdate
    ) -> Optional[models.Book]:
        """
        Update a book.
        
        Args:
            db: Database session
            book_id: Book ID to update
            book_update: New book data
            
        Returns:
            Optional[models.Book]: Updated book or None if not found
        """
        db_book = BookCRUD.get_book(db, book_id)
        if not db_book:
            return None
        
        update_data = book_update.dict(exclude_unset=True)
        
        for field, value in update_data.items():
            if value is not None:
                setattr(db_book, field, value)
        
        db.commit()
        db.refresh(db_book)
        
        return db_book
    
    @staticmethod
    def delete_book(db: Session, book_id: int) -> bool:
        """
        Delete a book by ID.
        
        Args:
            db: Database session
            book_id: Book ID to delete
            
        Returns:
            bool: True if book deleted, False if not found
        """
        db_book = BookCRUD.get_book(db, book_id)
        if not db_book:
            return False
        
        db.delete(db_book)
        db.commit()
        
        return True
    
    @staticmethod
    def search_books(
        db: Session,
        search_query: schemas.SearchQuery
    ) -> Tuple[List[models.Book], int]:
        """
        Search books with various filters and pagination.
        
        Args:
            db: Database session
            search_query: Search parameters
            
        Returns:
            Tuple[List[models.Book], int]: List of books and total count
        """
        query = db.query(models.Book)
        
        filters = []
        
        if search_query.title:
            filters.append(models.Book.title.ilike(f"%{search_query.title}%"))
        
        if search_query.author:
            filters.append(models.Book.author.ilike(f"%{search_query.author}%"))
        
        if search_query.year:
            filters.append(models.Book.year == search_query.year)
        
        if search_query.year_from and search_query.year_to:
            filters.append(models.Book.year.between(
                search_query.year_from, 
                search_query.year_to
            ))
        elif search_query.year_from:
            filters.append(models.Book.year >= search_query.year_from)
        elif search_query.year_to:
            filters.append(models.Book.year <= search_query.year_to)
        
        if filters:
            query = query.filter(and_(*filters))
        
        total = query.count()
        
        skip = (search_query.page - 1) * search_query.page_size
        books = query\
            .order_by(models.Book.id)\
            .offset(skip)\
            .limit(search_query.page_size)\
            .all()
        
        return books, total


# Create instance for use
book_crud = BookCRUD()

# Export for use in other modules
__all__ = ["book_crud", "BookCRUD"]
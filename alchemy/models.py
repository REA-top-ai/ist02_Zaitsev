from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text
)
from sqlalchemy.orm import relationship

from database import Base


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    email = Column(String(150), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Один автор -> много постов
    posts = relationship(
        "Post",
        back_populates="author",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Author(name='{self.name}', email='{self.email}')>"


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    published = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Внешний ключ
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)

    # Связи
    author = relationship("Author", back_populates="posts")

    comments = relationship(
        "Comment",
        back_populates="post",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Post(title='{self.title}', published={self.published})>"


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)

    author_name = Column(String(100), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    # Внешний ключ
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)

    # Связь
    post = relationship("Post", back_populates="comments")

    def __repr__(self):
        return f"<Comment(post_id={self.post_id}, author='{self.author_name}')>"


# Создание таблиц
if __name__ == "__main__":
    from database import engine

    Base.metadata.create_all(bind=engine)

    print("✓ Таблицы созданы!")
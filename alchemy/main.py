from datetime import date

from crud import *
from database import Base, SessionLocal, engine


def main():

    # Создание таблиц
    Base.metadata.create_all(bind=engine)

    # Сессия
    session = SessionLocal()

    try:
        print("Начинаем тестирование...\n")

        print("Создаём авторов...")

        author1 = create_author(
            session,
            "Анна Петрова",
            "anna@example.com"
        )

        author2 = create_author(
            session,
            "Иван Сидоров",
            "ivan@example.com"
        )

        print(f"{author1.name} (id={author1.id})")
        print(f"{author2.name} (id={author2.id})\n")

        print("Создаём посты...")

        post1 = create_post(
            session,
            "Первый пост",
            "Содержание первого поста",
            author1.id,
            published=True
        )

        post2 = create_post(
            session,
            "Черновик",
            "Этот пост пока не опубликован",
            author1.id,
            published=False
        )

        post3 = create_post(
            session,
            "Пост Ивана",
            "Текст от Ивана",
            author2.id,
            published=True
        )

        print(f"'{post1.title}' опубликован")
        print(f"'{post2.title}' черновик")
        print(f"'{post3.title}' опубликован\n")

        print("Добавляем комментарии...")

        add_comment(
            session,
            post1.id,
            "Читатель1",
            "Очень полезная статья!"
        )

        add_comment(
            session,
            post1.id,
            "Читатель2",
            "Спасибо!"
        )

        add_comment(
            session,
            post1.id,
            "Аноним",
            "Коротко."
        )

        print("Комментарии добавлены\n")

        print("Публикуем черновик...")

        success = update_post_status(
            session,
            post2.id,
            True
        )

        if success:
            print(f"'{post2.title}' теперь опубликован\n")

        print("Все опубликованные посты:")

        published_posts = get_published_posts(session)

        for post in published_posts:
            print(
                f"- {post.title} | Автор: {post.author.name}"
            )

        print()

        print("Поиск автора по email...")

        found = get_author_by_email(
            session,
            "anna@example.com"
        )

        if found:
            print(f"Найден: {found.name}")

        print()


        print("Поиск автора по имени...")

        found_author = get_author_by_name(
            session,
            "Анна Петрова"
        )

        if found_author:
            print(
                f"Найден автор: {found_author.name}"
            )

        print()

        print("Добавляем нескольких авторов...")

        authors_data = [
            {
                "name": "Мария Иванова",
                "email": "maria@example.com"
            },
            {
                "name": "Олег Смирнов",
                "email": "oleg@example.com"
            }
        ]

        authors = create_multiple_authors(
            session,
            authors_data
        )

        for author in authors:
            print(f"Добавлен: {author.name}")

        print()

        print("Пост с комментариями:")

        post = get_post_with_comments(
            session,
            post1.id
        )

        if post:

            print(f"Пост: {post.title}")

            print(f"Автор: {post.author.name}")

            print(f"Текст: {post.content}")

            print("\nКомментарии:")

            for comment in post.comments:
                print(
                    f"- {comment.author_name}: {comment.text}"
                )

        print()

        print("Посты за сегодня:")

        today_posts = get_published_posts_by_date(
            session,
            date.today()
        )

        for post in today_posts:
            print(f"- {post.title}")

        print()


        print("Топ авторов:")

        top_authors = get_top_authors_by_posts(
            session,
            limit=3
        )

        for rank, (name, count) in enumerate(top_authors, 1):
            print(f"{rank}. {name}: {count} пост(ов)")

    except Exception as e:

        print(f"Ошибка: {e}")

        session.rollback()

    finally:

        session.close()

        print("\nСессия закрыта")


if __name__ == "__main__":
    main()
# FastAPI Blog Project

A simple, scalable, and efficient blog application built using FastAPI. This project demonstrates the power of FastAPI for creating RESTful APIs and serves as a foundation for further development.

## Features

- User authentication and authorization (JWT-based).
- CRUD operations for blog posts.
- Comment system for posts.
- Pagination for listing posts.
- Swagger UI and ReDoc for API documentation.
- Modular architecture for scalability and maintainability.
- Integration with a database (PostgreSQL or SQLite).

## Technologies Used

- **Backend Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database**: SQLAlchemy with PostgreSQL (or SQLite for development).
- **Authentication**: JSON Web Tokens (JWT).
- **Asynchronous Programming**: Powered by Python’s asyncio.
- **Documentation**: Automatic API docs with Swagger UI and ReDoc.
- **Testing**: pytest for testing.

## Prerequisites

- Python 3.9 or higher
- PostgreSQL (optional, can use SQLite for development)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/fastapi-blog.git
   cd fastapi-blog
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:

   Create a `.env` file in the root directory and add the following:

   ```env
   DATABASE_URL=postgresql+asyncpg://username:password@localhost/db_name
   SECRET_KEY=your_secret_key
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

   Replace `username`, `password`, and `db_name` with your PostgreSQL credentials.

5. Run database migrations:

   ```bash
   alembic upgrade head
   ```

6. Start the development server:

   ```bash
   uvicorn app.main:app --reload
   ```

7. Access the API documentation:

   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Project Structure

```plaintext
fastapi-blog/
├── app/
│   ├── main.py         # Entry point of the application
│   ├── models/         # Database models
│   ├── schemas/        # Pydantic models
│   ├── routers/        # API routes
│   ├── services/       # Business logic
│   ├── utils/          # Helper functions
│   ├── core/           # Core configurations (e.g., settings, database connection)
│   └── tests/          # Test cases
├── migrations/         # Alembic migrations
├── .env                # Environment variables
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── alembic.ini         # Alembic configuration
```

## API Endpoints

### Authentication
- **POST** `/auth/login` - User login
- **POST** `/auth/register` - User registration

### Blog Posts
- **GET** `/posts/` - Get a list of posts (with pagination)
- **POST** `/posts/` - Create a new post
- **GET** `/posts/{post_id}` - Get a single post
- **PUT** `/posts/{post_id}` - Update a post
- **DELETE** `/posts/{post_id}` - Delete a post

### Comments
- **POST** `/posts/{post_id}/comments/` - Add a comment to a post
- **GET** `/posts/{post_id}/comments/` - Get comments for a post

## Running Tests

To run the test suite:

```bash
pytest
```

## Deployment

1. Configure a production database and update the `.env` file.
2. Use a production server like `gunicorn` with an ASGI server such as `uvicorn`:

   ```bash
   gunicorn -k uvicorn.workers.UvicornWorker app.main:app
   ```

3. Set up a reverse proxy (e.g., Nginx) for better performance and security.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add a new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

**Happy Coding!** 🚀

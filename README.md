# Utilities Util

A FastAPI-based utility management system for tracking household bills and expenses, with Gmail integration for automated bill processing.

## Features

- 🧾 **Bill Management**: Track and manage utility bills with automated processing
- 📧 **Gmail Integration**: Automatically process utility bills from email
- 👥 **Housemate Management**: Split bills between multiple housemates
- 💰 **Payment Tracking**: Monitor payment status and due dates
- 🔍 **Email Pattern Matching**: Configurable patterns to identify utility bills
- 🐘 **PostgreSQL Database**: Reliable data storage with SQLAlchemy ORM

## Tech Stack

- **Backend**: FastAPI (Python 3.13+)
- **Database**: PostgreSQL with asyncpg and psycopg2
- **ORM**: SQLAlchemy
- **Email**: Gmail API integration
- **Authentication**: Google OAuth2
- **Data Validation**: Pydantic
- **Package Management**: Poetry

## Prerequisites

- Python 3.13 or higher
- PostgreSQL database
- Gmail API credentials (for email integration)
- Poetry for dependency management

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/utilities-util.git
   cd utilities-util
   ```

2. **Install dependencies with Poetry**
   ```bash
   poetry install
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   DATABASE_URL=postgresql://username:password@localhost:5432/utilities_db
   GMAIL_CREDENTIALS_PATH=credentials.json
   ```

4. **Gmail API Setup**
   - Go to the [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select an existing one
   - Enable the Gmail API
   - Create credentials (OAuth 2.0 Client ID)
   - Download the credentials and save as `credentials.json` in the project root

5. **Database Setup**
   - Create a PostgreSQL database
   - Run migrations (if applicable)

## Usage

### Starting the API Server

```bash
poetry run uvicorn src.api.handler:app --reload
```

The API will be available at `http://localhost:8000`

### API Documentation

Once the server is running, visit:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Available Endpoints

#### Bills
- `GET /bill/` - Get all bills
- `GET /bill/{bill_id}` - Get a specific bill
- `POST /bill/` - Create a new bill
- `PUT /bill/{bill_id}` - Update a bill
- `DELETE /bill/{bill_id}` - Delete a bill

#### Email Processing
- Email-related endpoints for processing utility bills from Gmail

## Project Structure

```
src/
├── api/
│   ├── handler.py          # FastAPI app configuration
│   └── route/
│       ├── bill.py         # Bill management endpoints
│       ├── email.py        # Email processing endpoints
│       └── housemate.py    # Housemate management endpoints
├── common/
│   ├── database/
│   │   └── postgres.py     # Database connection and utilities
│   ├── models/             # Pydantic models
│   │   ├── bill.py
│   │   ├── email.py
│   │   ├── housemate.py
│   │   ├── payment.py
│   │   └── utility.py
│   └── poll_email/
│       └── handler.py      # Email polling logic
└── integrations/
    └── gmail.py            # Gmail API integration
```

## Configuration

### Email Pattern Matching
Configure patterns to automatically identify utility bills in your email:

```python
# Example bill filter rule
{
    "utility_id": "electric_company",
    "subject_key_word": "Your Electric Bill",
    "description": "Monthly electric bill",
    "is_active": True
}
```

### Bill Splitting
Configure how bills should be split between housemates:

```python
# Example split configuration
{
    "split_type": "equal",  # or "percentage", "fixed_amount"
    "housemates": ["john", "jane", "bob"]
}
```

## Development

### Running Tests
```bash
poetry run pytest
```

### Code Formatting
```bash
poetry run black src/
poetry run isort src/
```

### Type Checking
```bash
poetry run mypy src/
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Anthony Diep** - [antdiep14@gmail.com](mailto:antdiep14@gmail.com)

## Acknowledgments

- FastAPI for the excellent web framework
- Google APIs for Gmail integration
- PostgreSQL for reliable data storage
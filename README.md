# Speed Card Game

This is the initial state of the Speed card game.

## Prerequisites

- Python 3.x
- Docker
- Make

## Getting Started

### First Time Setup

1. Clone the repository:
```bash
git clone https://github.com/YoccoDante/speed-bff.git
cd speed-bff
```

2. Initialize the project (creates virtual environment, starts Docker containers, and sets up database):
```bash
make init
```

3. Start the database (if not already running):
```bash
make docker-setup
```

4. Run the Flask application:
```bash
make run
```

### Development Workflow

For daily development, you typically need to:

1. Start the database (if not running):
```bash
make docker-setup
```

2. Run the Flask application:
```bash
make run
```

### Docker Setup

The application uses Docker for the PostgreSQL database:
- `speed_postgres`: PostgreSQL database (runs on port 5432)

### Database Setup and Migration

#### Initial Database Setup

After running `make init`, you need to set up the database schema:

1. **Initialize Flask-Migrate** (only needed once):
```bash
FLASK_APP=app.main flask db init
```
This comment sets the env variable for the console session for windows:
```bash
$env:FLASK_APP = "app.main"
```

2. **Create initial migration**:
```bash
FLASK_APP=app.main flask db migrate -m "Initial migration with Player and GameRoom tables"
```

3. **Apply migration to create tables**:
```bash
FLASK_APP=app.main flask db upgrade
```

#### Database Connection

The PostgreSQL database will be available with these connection details:

```
Host: localhost (or 127.0.0.1)
Port: 5432
Database: speed_db
Username: speed
Password: speed

# Connection string format:
postgresql://speed:speed@localhost:5432/speed_db
```

You can use these credentials to connect using any PostgreSQL client (pgAdmin, DBeaver, etc.).

#### ⚠️ Important: Local PostgreSQL Conflicts

**CRITICAL**: If you have a local PostgreSQL installation running, it will conflict with the Docker container on port 5432. This will cause connection errors like:

```
FATAL: role "speed" does not exist
```

**Solution**: Stop your local PostgreSQL service before starting the Docker containers:

```bash
# Stop local PostgreSQL (macOS with Homebrew)
brew services stop postgresql
brew services stop postgresql@16  # or whatever version you have

# Check what's running on port 5432
lsof -i :5432

# Then start Docker containers
make docker-setup
```

**Testing the connection**: Use `127.0.0.1` instead of `localhost` to avoid IPv6/AirPlay conflicts:

```bash
# Test with curl
curl -X POST http://127.0.0.1:5000/auth/sign-up -H "Content-Type: application/json" -d '{"name": "Test", "lastName": "User", "email": "test@test.com", "firebaseId": "123", "refreshToken": "token"}'
```

### Available Commands

#### Setup Commands
- `make init` - First time setup (virtual environment, Docker, database)
- `make docker-setup` - Start Docker containers
- `make venv` - Create and setup virtual environment

#### Application Commands
- `make run` - Run the Flask application

#### Docker Commands
- `make up` - Start all containers
- `make down` - Stop all containers
- `make restart` - Restart containers
- `make logs` - Show container logs
- `make ps` - List running containers
- `make clean` - Remove all containers, volumes, and virtual environment

##### Database Commands
- `make db-create` - Create database
- `make db-migrate` - Run database migrations
- `make db-rollback` - Rollback last migration
- `make db-reset` - Reset database (drop, create, migrate)

#### Package Management
- `make install-deps <package1> [package2] ...` - Install Python packages and update requirements.txt
- `make update-deps` - Update Python dependencies

#### Git Commands
- `make git-clean` - Remove ignored files from Git tracking (keeps files locally)

### Common Workflows

1. **First time setup**:
```bash
make init
# Set up database schema (only needed once)
FLASK_APP=app.main flask db init
FLASK_APP=app.main flask db migrate -m "Initial migration"
FLASK_APP=app.main flask db upgrade
make run
```

2. **Daily development**:
```bash
make docker-setup  # if database is not running
make run
```

3. **Adding new database changes**:
```bash
# After modifying models
FLASK_APP=app.main flask db migrate -m "Description of changes"
FLASK_APP=app.main flask db upgrade
```

4. **Viewing logs**:
```bash
make logs
```

5. **Stopping everything**:
```bash
make down
```

6. **Complete reset**:
```bash
make clean
make init
# Re-run database setup
FLASK_APP=app.main flask db init
FLASK_APP=app.main flask db migrate -m "Initial migration"
FLASK_APP=app.main flask db upgrade
```

## Environment Variables

The application uses the following environment variables:
- `POSTGRES_USER`: Database user (default: speed)
- `POSTGRES_PASSWORD`: Database password (default: speed)
- `POSTGRES_DB`: Database name (default: speed_db)
- `POSTGRES_HOST`: Database host (default: localhost)
- `POSTGRES_PORT`: Database port (default: 5432)

## Troubleshooting

### Common Issues and Solutions

#### 1. "FATAL: role 'speed' does not exist"

**Problem**: Local PostgreSQL is running and conflicting with Docker container.

**Solution**:
```bash
# Stop local PostgreSQL
brew services stop postgresql
brew services stop postgresql@16

# Verify nothing is running on port 5432
lsof -i :5432

# Restart Docker containers
make down
make up
```

#### 2. "relation 'player' does not exist"

**Problem**: Database tables haven't been created yet.

**Solution**:
```bash
# Run database migrations
FLASK_APP=app.main flask db upgrade
```

#### 3. Flask app not responding / AirPlay conflicts

**Problem**: macOS AirPlay is using port 5000, or you're using `localhost` instead of `127.0.0.1`.

**Solution**:
```bash
# Use 127.0.0.1 instead of localhost
curl http://127.0.0.1:5000/

# Or disable AirPlay Receiver in System Preferences > Sharing
```

#### 4. "type 'datetime' does not exist" during migration

**Problem**: Using `DATETIME` instead of `TIMESTAMP` for PostgreSQL.

**Solution**: In your models, use:
```python
from sqlalchemy.types import TIMESTAMP
# Instead of DATETIME
created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), ...)
```

#### 5. Docker containers not starting

**Problem**: Port conflicts or Docker issues.

**Solution**:
```bash
# Check what's using the ports
lsof -i :5432  # PostgreSQL
lsof -i :6379  # Redis

# Clean up Docker
make clean
docker system prune -f
make init
```

## Project Structure

```
.
├── app/
│   ├── __init__.py         # Flask app factory
│   ├── main.py            # Application entry point
│   ├── config.py          # Configuration settings
│   ├── models/            # SQLAlchemy models
│   ├── api/               # Flask-RESTX API endpoints
│   ├── controllers/       # Business logic
│   ├── repositories/      # Data access layer
│   └── utils/             # Utility functions
├── migrations/            # Database migration files
├── Dockerfile            # Python application container
├── docker-compose.yml    # Docker services configuration
├── Makefile             # Build automation
├── requirements.txt     # Python dependencies
└── README.md           # This file
```
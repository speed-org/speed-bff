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

### Database Connection

The PostgreSQL database will be available with these connection details:

```
Host: localhost
Port: 5432
Database: speed_db
Username: speed
Password: speed

# Connection string format:
postgresql://speed:speed@localhost:5432/speed_db
```

You can use these credentials to connect using any PostgreSQL client (pgAdmin, DBeaver, etc.).

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

#### Database Commands
- `make db-create` - Create database
- `make db-migrate` - Run database migrations
- `make db-rollback` - Rollback last migration
- `make db-reset` - Reset database (drop, create, migrate)

### Common Workflows

1. **First time setup**:
```bash
make init
make run
```

2. **Daily development**:
```bash
make docker-setup  # if database is not running
make run
```

3. **Viewing logs**:
```bash
make logs
```

4. **Stopping everything**:
```bash
make down
```

5. **Complete reset**:
```bash
make clean
make init
```

## Environment Variables

The application uses the following environment variables:
- `POSTGRES_USER`: Database user (default: speed)
- `POSTGRES_PASSWORD`: Database password (default: speed)
- `POSTGRES_DB`: Database name (default: speed_db)
- `POSTGRES_HOST`: Database host (default: localhost)
- `POSTGRES_PORT`: Database port (default: 5432)

## Project Structure

```
.
├── main.py              # Application entry point
├── Dockerfile          # Python application container configuration
├── docker-compose.yml   # Docker services configuration
├── Makefile            # Build automation
├── requirements.txt    # Python dependencies
└── .env               # Environment variables (create from example)
```
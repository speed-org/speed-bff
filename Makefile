.PHONY: up down restart logs ps clean db-create db-migrate db-rollback db-reset help run venv init update-deps install-deps git-clean

# Default command
.DEFAULT_GOAL := run

# Helpers
# This allows passing arguments directly to commands
%:
	@:

# Validation function
define validate_args
	@if [ "$(words $(filter-out $@,$(MAKECMDGOALS)))" -eq 0 ]; then \
		echo "Error: Missing path argument. Usage: make $(1) path"; \
		exit 1; \
	fi
endef

# First time setup
init: venv docker-setup db-create

# Docker setup
docker-setup:
	docker compose up -d

# Virtual Environment
venv:
	python -m venv speed-venv
ifeq ($(OS),Windows_NT)
	.\speed-venv\Scripts\activate && pip install -r requirements.txt
else
	. speed-venv/bin/activate && pip install -r requirements.txt
endif

# Update dependencies
update-deps:
	. speed-venv/bin/activate && pip install -r requirements.txt

# Handle unknown targets (required for install-deps command)
%:
	@:

# Install Python packages and add them to requirements.txt
install-deps:
	@if [ "$(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))" = "" ]; then \
		echo "Error: No packages specified. Usage: make install-deps <package1> [package2] [package3] ..."; \
		exit 1; \
	fi
	. speed-venv/bin/activate && pip install $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
	@echo "Adding packages to requirements.txt..."
	@cp requirements.txt requirements.txt.bak
	@. speed-venv/bin/activate && pip freeze > requirements.txt.tmp
	@cat requirements.txt.bak requirements.txt.tmp | sort -u > requirements.txt
	@rm requirements.txt.tmp requirements.txt.bak
	@echo "Packages installed and requirements.txt updated successfully"

# Clean Git cache of ignored files
git-clean:
	@echo "Checking for uncommitted changes..."
	@if [ -n "$$(git status --porcelain)" ]; then \
		echo "⚠️  You have uncommitted changes. Please commit or stash them first:"; \
		git status; \
		echo "\nRun these commands:"; \
		echo "1. git add ."; \
		echo "2. git commit -m \"Your commit message\""; \
		echo "3. make git-clean"; \
		exit 1; \
	fi
	@echo "Removing ignored files from Git tracking (keeping them locally)..."
	git rm -rf --cached .
	git add .
	@echo "\nFiles that will be untracked (but kept locally):"
	git status
	@echo "\nReview the changes above and commit them with:"
	@echo "git commit -m \"Remove ignored files from Git tracking\""

# Docker commands
up:
	docker compose up -d

down:
	docker compose down

restart:
	docker compose restart

logs:
	docker compose logs -f

ps:
	docker compose ps

clean:
	docker compose down -v
	docker system prune -f
	rm -rf speed-venv

# App commands
run: venv
ifeq ($(OS),Windows_NT)
	set PYTHONPATH=$(PWD) && .\speed-venv\Scripts\activate && python -m app.main
else
	PYTHONPATH=$(PWD) . speed-venv/bin/activate && python -m app.main
endif

# Database commands
db-create:
	docker compose exec postgres createdb -U speed speed_db || true

db-migrate:
	# Add your migration command here
	# Example: npm run migrate

db-rollback:
	# Add your rollback command here
	# Example: npm run migrate:rollback

db-reset:
	docker compose down -v
	docker compose up -d
	sleep 5
	$(MAKE) db-create
	$(MAKE) db-migrate

# Lint, Format and Type checking commands
lint: venv
	$(call validate_args,lint)
	. speed-venv/bin/activate && flake8 $(filter-out $@,$(MAKECMDGOALS)) --max-line-length=88 --extend-ignore=E203,W503

fmt: venv
	$(call validate_args,fmt)
	. speed-venv/bin/activate && black $(filter-out $@,$(MAKECMDGOALS))

fmt-check: venv
	$(call validate_args,fmt-check)
	. speed-venv/bin/activate && black --check $(filter-out $@,$(MAKECMDGOALS))

check: venv
	$(call validate_args,check)
	. speed-venv/bin/activate && mypy $(filter-out $@,$(MAKECMDGOALS)) --ignore-missing-imports


# Help command
help:
	@echo "Available commands:"
	@echo "  make init        - First time setup (venv, docker, database)"
	@echo "  make run         - Run the Flask application"
	@echo "  make venv        - Create and setup virtual environment"
	@echo "  make update-deps - Update Python dependencies"
	@echo "  make install-deps <package1> [package2] ... - Install and save Python packages"
	@echo "  make git-clean   - Remove ignored files from Git tracking (keeps files locally)"
	@echo "  make docker-setup- Start Docker containers"
	@echo "  make up          - Start all containers"
	@echo "  make down        - Stop all containers"
	@echo "  make restart     - Restart containers"
	@echo "  make logs        - Show container logs"
	@echo "  make ps          - List running containers"
	@echo "  make clean       - Remove all containers, volumes, and venv"
	@echo "  make db-create   - Create database"
	@echo "  make db-migrate  - Run database migrations"
	@echo "  make db-rollback - Rollback last migration"
	@echo "  make db-reset    - Reset database (drop, create, migrate)" 
	@echo "  make lint path      - Validates linting for a given path"
	@echo "  make fmt path       - Formats the code using black"
	@echo "  make fmt-check path - Checks if code is formatted correctly"
	@echo "  make check path     - Checks typing for a given path"
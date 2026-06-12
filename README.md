# Network Asset Reconciliation

A comprehensive Python application for reconciling network asset inventory with discovered network devices.

## Features

- **File Upload & Parsing**: Support for TXT and Excel formats
- **Data Filtering**: Date-based and column-based filtering
- **Asset Matching**: Advanced comparison engine for asset reconciliation
- **Report Generation**: Detailed reports on matched and unmatched assets
- **REST API**: FastAPI-based endpoints for integration
- **Scheduled Processing**: Automatic processing on file arrival
- **Database**: DuckDB for efficient data management
- **Docker Support**: Containerized deployment

## Project Structure

```
network_asset_reconciliation/
├── app/                    # Main application code
│   ├── api/               # REST API endpoints
│   ├── core/              # Core configuration and utilities
│   ├── parsers/           # File parsers
│   ├── filters/           # Data filtering
│   ├── matching/          # Asset matching logic
│   ├── reports/           # Report generation
│   ├── services/          # Business logic services
│   ├── database/          # Database management
│   ├── models/            # Data models
│   ├── utils/             # Utility functions
│   └── main.py            # Entry point
├── config/                # Configuration files
├── input/                 # Input file directories
├── output/                # Output reports and results
├── logs/                  # Application logs
├── tests/                 # Unit tests
├── docker/                # Docker configuration
└── docs/                  # Documentation
```

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Configure the application:
   ```bash
   cp .env.example .env
   ```

3. Update configuration files in `config/` directory

## Usage

### Running the Application

```bash
python app/main.py
```

### Running Tests

```bash
pytest tests/
```

### Running with Docker

```bash
docker-compose -f docker/docker-compose.yml up
```

## API Documentation

See `docs/api_docs.md` for detailed API documentation.

## Configuration

See `docs/user_guide.md` for configuration guide.

## Architecture

See `docs/architecture.md` for system architecture details.

## License

[Your License Here]

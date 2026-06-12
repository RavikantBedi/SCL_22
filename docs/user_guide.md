# Network Asset Reconciliation - User Guide

## Getting Started

### Prerequisites
- Python 3.11+
- Required packages (see requirements.txt)

### Installation

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Configure settings in `config/settings.yaml`
4. Run the application: `python app/main.py`

## Usage

### File Upload
1. Place files in `input/txt` or `input/excel` directory
2. Use the API or folder watcher to trigger processing

### Processing
1. Configure reconciliation parameters
2. Start the reconciliation process
3. Monitor progress through logs

### Reports
1. Access generated reports in `output/` directory
2. Review matched/unmatched results
3. Export summaries as needed

## Configuration
See `config/settings.yaml` for available configuration options.

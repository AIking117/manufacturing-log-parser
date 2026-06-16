# Manufacturing Log Parser

A Python command-line project for converting raw manufacturing machine logs into clean, structured CSV data for analysis, reporting, and future predictive maintenance workflows.

## Project Overview

Manufacturing equipment often produces raw log files that are difficult to analyze manually. These logs may contain timestamps, machine identifiers, status messages, warnings, errors, downtime events, and production activity.

The goal of this project is to parse messy manufacturing log data and transform it into a structured format that can be used for analysis in tools such as Excel, Power BI, Python, or future machine learning workflows.

This project demonstrates practical Python scripting, command-line interface development, text parsing, file handling, and industrial data-cleaning concepts.

## Why This Project Matters

Machine logs can contain valuable information about equipment health, recurring faults, downtime patterns, and production interruptions. However, raw logs are often too messy to analyze directly.

A parser like this can help turn raw operational data into usable information.

Potential use cases include:

- Identifying recurring machine errors
- Tracking warning and fault events
- Preparing downtime data for reporting
- Converting raw logs into CSV files
- Supporting manufacturing analytics workflows
- Preparing datasets for future predictive maintenance models

## Intended Functionality

The project is designed to:

- Read raw manufacturing log files
- Extract useful fields such as timestamps, machine IDs, severity levels, and event messages
- Convert semi-structured log entries into clean tabular data
- Export parsed results into CSV format
- Support repeatable use through a command-line workflow

## Example Input

    2026-01-15 08:14:22 MACHINE_03 WARNING Temperature exceeded threshold
    2026-01-15 08:17:10 MACHINE_03 ERROR Motor fault detected
    2026-01-15 08:22:45 MACHINE_03 INFO Production resumed

## Example Output

| timestamp | machine_id | severity | message |
|---|---|---|---|
| 2026-01-15 08:14:22 | MACHINE_03 | WARNING | Temperature exceeded threshold |
| 2026-01-15 08:17:10 | MACHINE_03 | ERROR | Motor fault detected |
| 2026-01-15 08:22:45 | MACHINE_03 | INFO | Production resumed |

## Intended CLI Usage

The project is designed to run as a command-line tool.

Example intended command:

    python main.py --input data/raw/sample_log.txt --output data/processed/parsed_logs.csv

The goal is for the tool to accept a raw manufacturing log file, parse important fields, and export a cleaned CSV file for analysis.

## Technologies

This project may use:

- Python
- Regular expressions
- CSV file handling
- pandas
- argparse
- Command-line scripting

## Future Improvements

Planned improvements include:

- Support multiple log formats
- Add automated tests
- Add summary reports for error frequency
- Calculate downtime durations
- Generate machine-level summaries
- Add visual dashboards
- Add anomaly detection
- Prepare features for predictive maintenance modeling

## Portfolio Context

This project is part of my broader transition into AI/ML, data science, and engineering analytics.

The project connects manufacturing, mechanical systems, automation, and analytics by showing how raw operational logs can be transformed into structured data for analysis, reporting, and future predictive maintenance workflows.

## Author

Created by Clement Chai.

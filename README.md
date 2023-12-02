# SonarQube Rules Exporter

## Overview

The SonarQube Rules Exporter is a Python script designed to scrape static code analysis rules from SonarQube's web pages for various programming languages and export them into Excel files. This script supports multiple languages, making it easy for users to quickly gather and analyze SonarQube rules.

## Features

- Supports exporting SonarQube rules for multiple programming languages.
- Exports rules into structured Excel files.
- Automatically numbers the exported rules for easy reference and analysis.

## Usage

1. Ensure Python and the following libraries are installed in your environment:
   - `requests`
   - `beautifulsoup4` (or `bs4`)
   - `pandas`
   - `openpyxl`

2. Before running the script, modify or verify the URLs in the script as needed.

3. To run the script, use the following command:

   ```bash
   python sonar_rules_exporter.py

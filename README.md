# 🧪 Amazon Website Automation (Playwright + Pytest)

## Overview
Automates a basic search flow on the Amazon website using Playwright and Pytest in Python.

## Setup
```bash
pip install -r requirements.txt
playwright install
pytest -v --html=report.html --self-contained-html
```

## Project Structure
- `pages/` → Page Object Models
- `tests/` → Test scripts
- `conftest.py` → Fixtures for browser/page setup
- `pytest.ini` → Configuration
- `requirements.txt` → Dependencies
- `README.md` → Setup instructions

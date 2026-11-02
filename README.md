# Sauce Demo Playwright + pytest BDD Framework

A small end-to-end test framework for [Sauce Demo](https://www.saucedemo.com/), built with Python, Playwright, pytest, and pytest-bdd. It demonstrates page objects, shared pytest fixtures, and readable Gherkin scenarios.

## Project structure

```text
.
├── features/
│   ├── checkout.feature         # Checkout details and order review
│   ├── login.feature            # Successful sign-in
│   ├── negative_scenarios.feature # Invalid login and checkout validation
│   └── place_order.feature      # Completing a purchase
├── pages/
│   ├── cart_page.py             # Shopping cart page object
│   ├── checkout_page.py         # Checkout and order confirmation page object
│   ├── inventory_page.py        # Product inventory page object
│   └── login_page.py            # Login page object
├── tests/
│   ├── conftest.py              # Shared URL and page-object fixtures
│   └── steps/
│       └── test_sauce_demo_steps.py
├── reports/                     # Generated HTML test reports
├── pytest.ini                   # pytest and pytest-bdd configuration
└── requirements.txt
```

## Requirements

- Python 3.9 or newer
- pip
- A supported Playwright browser (Chromium is used in the commands below)

## Setup

Create and activate a virtual environment from the project directory.

**Windows PowerShell**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
playwright install chromium
```

**macOS/Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
playwright install chromium
```

On Linux CI machines, install browser system dependencies with `playwright install --with-deps chromium`.

## Run the scenarios

Run all BDD scenarios:

```bash
pytest
```

Run just the scenarios tagged `@smoke`:

```bash
pytest -m smoke
```

Run only the login scenario marked `@login`:

```bash
pytest -m login
```

Run with a visible browser:

```bash
pytest --headed
```

## Test reports

The framework uses `pytest-html` to generate a standalone HTML report. Reports are written to `reports/pytest-report.html`.

Create the report directory if it does not exist, then run the test suite with the HTML options:

**Windows PowerShell**

```powershell
New-Item -ItemType Directory -Force reports | Out-Null
pytest --html=reports\pytest-report.html --self-contained-html
```

**macOS/Linux**

```bash
mkdir -p reports
pytest --html=reports/pytest-report.html --self-contained-html
```

Open `reports/pytest-report.html` in a browser to review pass/fail results and test details. Re-running the command updates the report at that path.

## GitHub Actions

The workflow at `.github/workflows/tests.yml` runs the marked login scenario on pushes, pull requests, and manual dispatch. It installs Chromium, writes the HTML report to `reports/pytest-report.html`, and uploads that report as the `login-test-report` artifact.

Run a specific feature or scenario file:

```bash
pytest tests/steps/test_sauce_demo_steps.py
```

Playwright's pytest plugin runs headless by default and provides the `page` fixture. To use a different browser, pass `--browser firefox` or `--browser webkit` after installing it with `playwright install firefox` or `playwright install webkit`.

## Configuration

The target URL defaults to `https://www.saucedemo.com`. Override it by setting `SAUCEDEMO_URL` before running pytest.

**Windows PowerShell**

```powershell
$env:SAUCEDEMO_URL = "https://your-test-environment.example"
pytest
```

**macOS/Linux**

```bash
SAUCEDEMO_URL=https://your-test-environment.example pytest
```

The demo credentials are Sauce Demo's public test account: `standard_user` / `secret_sauce`. Do not use real credentials in test scenarios.

## Included feature scenarios

- **Login:** valid credentials show the product inventory.
- **Checkout:** add the Sauce Labs Backpack, enter customer details, and verify the order summary and total.
- **Place order:** complete checkout and verify the confirmation message.
- **Negative scenarios:** invalid password displays a login error, and checkout without required details shows a validation error.

Assertions use Playwright's auto-waiting `expect` API. Page interactions are kept in page objects, while the feature file describes behavior in Gherkin.

## Troubleshooting

- If pytest reports that no browser executable is available, run `playwright install chromium`.
- If browser startup fails on a Linux host due to missing OS libraries, run `playwright install --with-deps chromium`.
- If the application is unavailable, verify network access to the configured Sauce Demo URL.

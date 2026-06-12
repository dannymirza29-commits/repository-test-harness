# Repository Test Harness

Automated testing framework for validating code repositories in isolated Docker environments.

## Overview

Runs test suites in containerized environments to ensure consistent, reproducible results.
Collects coverage metrics and generates structured test reports.

## Architecture
## Usage

```bash
python harness.py --repo <path> --container <image>
```

## Output

Generates `test_report.json` with:
- Test results (passed/failed)
- Execution time
- Code coverage percentage
- Failed test details

## Technologies

Python | Docker | CMake | Testing | CI/CD

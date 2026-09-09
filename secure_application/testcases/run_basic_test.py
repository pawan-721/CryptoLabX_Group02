import sqlite3
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "src" / "bank.db"

if DB.exists():
    DB.unlink()

p = subprocess.run(
    [sys.executable, str(ROOT / "src" / "main.py")],
    input="1\nalice\nalice123\n2\n1\n8\n",
    text=True,
    capture_output=True,
)

assert "Login successful" in p.stdout
assert "Account: Alice" in p.stdout
print("TC01 and TC04 passed.")

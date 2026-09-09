# Lab Assignment 3 - Online Banking

## Group
Group 2

## Application
Online Banking System

The assignment requires a small application with core banking functionality and three vulnerabilities. Group 2 maps to **Online Banking**.

## Core functionalities
1. User login
2. Balance inquiry
3. Fund transfer
4. Beneficiary management
5. Transaction history

## Implemented vulnerabilities
1. **SQL Injection** - login builds the SQL query using string concatenation.
2. **Broken Access Control** - balance/transfer operations accept an account ID without checking that it belongs to the logged-in user.
3. **Insecure Session Management** - a predictable user-ID-based session token is stored in memory without expiry or robust session invalidation.

## Requirements
- Python 3
- SQLite3 (included with standard Python)

## Run
```bash
cd secure_application/src
python3 main.py
```

A SQLite database named `bank.db` is created automatically.

## Demo accounts
- alice / alice123
- bob / bob123
- admin / admin123

These are intentionally simple credentials for a lab demonstration.

## Vulnerability demonstrations

### 1. SQL Injection
At login, try:
- Username: `' OR '1'='1' --`
- Password: anything

The vulnerable query can be altered because input is concatenated into SQL.

### 2. Broken Access Control
Login as `alice`, choose Balance, and enter account ID `2`.
Alice can view Bob's balance because ownership is not checked.

For the transfer demonstration, login as Alice and enter source account ID `2`. The program uses the supplied source ID instead of enforcing that it matches the logged-in account.

### 3. Insecure Session Management
The session token is simply the logged-in user's numeric ID and has no expiry. The session is held in a global variable, demonstrating weak session lifecycle design.

## SAST
Bandit can be used for Python static analysis:

```bash
pip install bandit
bandit -r src -f txt -o sast/bandit_report.txt
```

## Repository structure

```text
CryptoLabX/
├── classical/
├── modern/
├── hashing/
├── attacks/
├── analysis/
├── docs/
├── secure_application/
│   ├── src/
│   ├── reports/
│   ├── screenshots/
│   ├── sast/
│   ├── outputs/
│   ├── testcases/
│   └── README.md
└── README.md
```

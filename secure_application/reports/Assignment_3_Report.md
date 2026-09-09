# Assignment 3 Report - Online Banking System

## 1. Objective
Develop a small console-based Online Banking application demonstrating core functionality and three intentionally introduced security vulnerabilities.

## 2. Application
**Online Banking System - Group 2**

## 3. Functionalities
- Login
- Balance inquiry
- Fund transfer
- Beneficiary management
- Transaction history

## 4. Technology
- Python 3
- SQLite
- Console interface
- Bandit for Python SAST

## 5. Vulnerability 1: SQL Injection

### Location
`src/main.py` - `login()`

### Cause
The username and password are directly concatenated into the SQL statement.

### Demonstration
Use:
- Username: `' OR '1'='1' --`
- Password: `anything`

### Impact
An attacker can manipulate the SQL query and potentially bypass authentication.

### Fix
Use parameterized SQL queries:
```python
conn.execute(
    "SELECT * FROM users WHERE username = ? AND password = ?",
    (username, password)
)
```

## 6. Vulnerability 2: Broken Access Control

### Location
`src/main.py` - `show_balance()` and `transfer()`

### Cause
The application accepts an account ID from the user without verifying that the account belongs to the authenticated user.

### Demonstration
Login as Alice and request account ID `2`. Bob's balance is displayed.

### Impact
Unauthorized users can access another customer's financial information. The same design can allow an unauthorized source account to be selected for a transfer.

### Fix
Never trust a user-supplied source/owner ID. Derive it from the authenticated session and enforce authorization before every sensitive operation.

## 7. Vulnerability 3: Insecure Session Management

### Location
`src/main.py` - `login()`

### Cause
The session token is simply the numeric user ID and is stored in a global variable. There is no expiry or robust lifecycle management.

### Impact
Predictable session identifiers make session security weak and can enable session abuse in a real multi-user implementation.

### Fix
Generate a cryptographically random session identifier, store session state server-side, set an expiry, rotate the token after authentication, and invalidate it on logout.

## 8. Test Cases

| TC | Test | Expected result |
|---|---|---|
| TC01 | Valid Alice login | Login succeeds |
| TC02 | Invalid password | Login fails |
| TC03 | SQL injection login input | Vulnerability is demonstrated |
| TC04 | Alice checks account 1 | Alice balance displayed |
| TC05 | Alice checks account 2 | Unauthorized Bob balance is displayed |
| TC06 | Add beneficiary | Beneficiary is stored |
| TC07 | List beneficiaries | User's beneficiaries displayed |
| TC08 | Valid transfer | Balance decreases |
| TC09 | Transaction history | Transfer appears |
| TC10 | Logout then balance | Login required |

## 9. SAST
Run Bandit against the source folder:

```bash
bandit -r src -f txt -o sast/bandit_report.txt
```

Store the generated report inside `sast/`.

## 10. Conclusion
The application implements the required small-scale banking workflow while deliberately demonstrating SQL Injection, Broken Access Control, and Insecure Session Management. The report also describes appropriate remediation for each vulnerability.

import sqlite3
import uuid
from datetime import datetime

DB = "bank.db"
CURRENT_SESSION = None


def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.executescript("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE,
        password TEXT,
        name TEXT,
        balance REAL
    );

    CREATE TABLE IF NOT EXISTS beneficiaries (
        id INTEGER PRIMARY KEY,
        owner_id INTEGER,
        beneficiary_name TEXT,
        account_no TEXT
    );

    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        receiver_account TEXT,
        amount REAL,
        created_at TEXT
    );
    """)

    if cur.execute("SELECT COUNT(*) FROM users").fetchone()[0] == 0:
        cur.executemany(
            "INSERT INTO users(username,password,name,balance) VALUES(?,?,?,?)",
            [
                ("alice", "alice123", "Alice", 10000.0),
                ("bob", "bob123", "Bob", 7000.0),
                ("admin", "admin123", "Bank Admin", 50000.0),
            ],
        )
        cur.executemany(
            "INSERT INTO beneficiaries(owner_id,beneficiary_name,account_no) VALUES(?,?,?)",
            [
                (1, "Bob", "ACC1002"),
                (2, "Alice", "ACC1001"),
            ],
        )
    conn.commit()
    conn.close()


# VULNERABILITY 1: SQL Injection
# The username/password are directly concatenated into SQL.
def login():
    global CURRENT_SESSION

    username = input("Username: ")
    password = input("Password: ")

    # conn = get_db()
    # query = (
    #     "SELECT * FROM users WHERE username = '"
    #     + username
    #     + "' AND password = '"
    #     + password
    #     + "'"
    # )
    # try:
    #     user = conn.execute(query).fetchone()
    # except sqlite3.Error as e:
    #     print("Database error:", e)
    #     conn.close()
    #     return

    conn = get_db()

    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    user = conn.execute(query, (username, password)).fetchone()

    try:
        user = conn.execute(query).fetchone()
    except sqlite3.Error as e:
        print("Database error:", e)
        conn.close()
        return

    if user:
        # VULNERABILITY 2: Insecure Session Management
        # A predictable/in-memory session token is used with no expiry,
        # logout invalidation, or secure server-side session lifecycle.
        CURRENT_SESSION = {
            "token": str(user["id"]),
            "user_id": user["id"],
            "username": user["username"],
        }
        print(f"Login successful. Welcome {user['name']}!")
    else:
        print("Invalid username or password.")
    conn.close()


def current_user():
    if CURRENT_SESSION is None:
        print("Please login first.")
        return None
    conn = get_db()
    user = conn.execute(
        "SELECT * FROM users WHERE id = ?", (CURRENT_SESSION["user_id"],)
    ).fetchone()
    conn.close()
    return user


def show_balance():
    user = current_user()
    if not user:
        return

    # VULNERABILITY 3: Broken Access Control
    # User-supplied account ID is accepted without verifying ownership.
    account_id = input(
        "Enter account ID to view balance (1=Alice, 2=Bob, 3=Admin): "
    )

    conn = get_db()
    row = conn.execute(
        "SELECT id, username, name, balance FROM users WHERE id = ?",
        (account_id,),
    ).fetchone()
    conn.close()

    if row:
        print(f"Account: {row['name']} | Balance: Rs.{row['balance']:.2f}")
    else:
        print("Account not found.")


def add_beneficiary():
    user = current_user()
    if not user:
        return

    name = input("Beneficiary name: ")
    account_no = input("Beneficiary account no: ")

    conn = get_db()
    conn.execute(
        "INSERT INTO beneficiaries(owner_id,beneficiary_name,account_no) VALUES(?,?,?)",
        (user["id"], name, account_no),
    )
    conn.commit()
    conn.close()
    print("Beneficiary added.")


def list_beneficiaries():
    user = current_user()
    if not user:
        return

    conn = get_db()
    rows = conn.execute(
        "SELECT id, beneficiary_name, account_no FROM beneficiaries WHERE owner_id = ?",
        (user["id"],),
    ).fetchall()
    conn.close()

    if not rows:
        print("No beneficiaries.")
        return

    for row in rows:
        print(f"{row['id']}. {row['beneficiary_name']} - {row['account_no']}")


def transfer():
    user = current_user()
    if not user:
        return

    # Demonstrates insufficient validation and the broken-access-control design:
    # the source account is taken from the user instead of being independently
    # authorized against the logged-in identity.
    source_id = input("Source account ID: ")
    receiver = input("Receiver account no: ")
    amount_text = input("Amount: ")

    try:
        amount = float(amount_text)
    except ValueError:
        print("Invalid amount.")
        return

    conn = get_db()
    source = conn.execute(
        "SELECT * FROM users WHERE id = ?", (source_id,)
    ).fetchone()

    if not source:
        print("Source account not found.")
        conn.close()
        return

    if amount <= 0 or amount > source["balance"]:
        print("Invalid amount or insufficient balance.")
        conn.close()
        return

    conn.execute(
        "UPDATE users SET balance = balance - ? WHERE id = ?",
        (amount, source_id),
    )

    conn.execute(
        "UPDATE users SET balance = balance + ? WHERE id = ?",
        (amount, receiver),
    )

    conn.execute(
        "INSERT INTO transactions(user_id,receiver_account,amount,created_at) VALUES(?,?,?,?)",
        (source_id, receiver, amount, datetime.now().isoformat(timespec="seconds")),
    )
    conn.commit()
    conn.close()
    print("Transfer successful.")


def transaction_history():
    user = current_user()
    if not user:
        return

    conn = get_db()
    rows = conn.execute(
        "SELECT receiver_account, amount, created_at FROM transactions WHERE user_id = ? ORDER BY id DESC",
        (user["id"],),
    ).fetchall()
    conn.close()

    if not rows:
        print("No transactions.")
        return

    for row in rows:
        print(
            f"{row['created_at']} -> {row['receiver_account']} : Rs.{row['amount']:.2f}"
        )


def logout():
    global CURRENT_SESSION
    CURRENT_SESSION = None
    print("Logged out.")


def menu():
    while True:
        print("\n===== ONLINE BANKING SYSTEM =====")
        print("1. Login")
        print("2. Check Balance")
        print("3. Transfer Funds")
        print("4. Add Beneficiary")
        print("5. List Beneficiaries")
        print("6. Transaction History")
        print("7. Logout")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            login()
        elif choice == "2":
            show_balance()
        elif choice == "3":
            transfer()
        elif choice == "4":
            add_beneficiary()
        elif choice == "5":
            list_beneficiaries()
        elif choice == "6":
            transaction_history()
        elif choice == "7":
            logout()
        elif choice == "8":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    init_db()
    menu()

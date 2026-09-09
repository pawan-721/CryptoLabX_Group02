# Test Cases

## TC01 - Valid login
Input:
alice
alice123

Expected:
Login successful.

## TC02 - Invalid login
Input:
alice
wrongpass

Expected:
Invalid username or password.

## TC03 - SQL Injection
Input:
Username: ' OR '1'='1' --
Password: anything

Expected:
Authentication can be bypassed in the vulnerable implementation.

## TC04 - Own balance
Login as Alice and choose balance.
Account ID: 1

Expected:
Alice's balance is displayed.

## TC05 - Broken access control
Login as Alice and choose balance.
Account ID: 2

Expected:
Bob's balance is displayed, demonstrating unauthorized access.

## TC06 - Add beneficiary
Login as Alice.
Choose Add Beneficiary.
Enter:
Name: TestUser
Account: ACC9999

Expected:
Beneficiary added.

## TC07 - Transaction
Login as Alice.
Choose Transfer.
Source account ID: 1
Receiver: ACC1002
Amount: 100

Expected:
Transfer successful.

## TC08 - Transaction history
Choose Transaction History after a transfer.

Expected:
The transfer appears in the list.

## TC09 - Logout
Choose Logout and then Balance.

Expected:
Please login first.

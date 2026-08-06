import os
import hashlib
import subprocess

password = "admin123"

username = input("Enter username: ")
command = input("Enter command: ")

# Command Injection
os.system(command)

# Weak Cryptography
hashed_password = hashlib.md5(password.encode()).hexdigest()

# Dangerous subprocess usage
subprocess.call(command, shell=True)

# Debug information
print(password)
print("MD5:", hashed_password)
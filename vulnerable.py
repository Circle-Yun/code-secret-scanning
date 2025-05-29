# vulnerable.py

import os
import subprocess
import pickle
import hashlib
import requests
import jwt
import sqlite3

# 1. OS Command Injection (CWE-78)
def cmd_injection():
    cmd = input("Enter a command: ")
    os.system(cmd)  # 위험
    subprocess.call(cmd, shell=True)  # 위험

# 2. Deserialization of untrusted data (CWE-502)
def unsafe_deserialization():
    data = input("Enter serialized object: ")
    obj = pickle.loads(data.encode())  # 위험

# 3. Hardcoded credentials (CWE-798)
def hardcoded_credentials():
    username = "admin"
    password = "P@ssw0rd!"  # 하드코딩된 비밀번호
    print("Logging in with", username, password)

# 4. Weak hashing (CWE-327)
def weak_hashing():
    password = input("Enter password: ")
    hashed = hashlib.md5(password.encode()).hexdigest()  # 취약한 해시
    print("MD5 Hash:", hashed)

# 5. Insecure HTTP request (CWE-319)
def insecure_http():
    r = requests.get("http://example.com/api/data")  # HTTPS 아님

# 6. JWT without verification (CWE-345)
def jwt_insecure():
    token = input("Enter JWT: ")
    decoded = jwt.decode(token, options={"verify_signature": False})  # 서명 검증 안함

# 7. SQL Injection (CWE-89)
def sql_injection():
    user_input = input("Enter username: ")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE name = '{user_input}'"  # 취약한 쿼리
    cursor.execute(query)
    print(cursor.fetchall())

# 실행
cmd_injection()
unsafe_deserialization()
hardcoded_credentials()
weak_hashing()
insecure_http()
jwt_insecure()
sql_injection()

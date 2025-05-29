# demo.py

import subprocess

def insecure(): # insecure 함수 정의
	cmd = input("Enter command: ")
	subprocess.call(cmd, shell=True) # ⚠️ Command Injection 가능성

insecure() # insecure 함수 실행

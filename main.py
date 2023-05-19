import os
import subprocess

DEBUG = 0

loc = "dev" if DEBUG else "src"
os.chdir(f".\{loc}")
subprocess.run(["python", "-u", "main.py"], shell=True)
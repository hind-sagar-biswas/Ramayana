import os
import subprocess

DEBUG = 0

loc = "src"
if DEBUG: loc = "dev"

os.chdir(f".\{loc}")
subprocess.run(["python", "-u", "main.py"], shell=True)

import os
import subprocess

DEBUG = 1

loc = "src"
if DEBUG: loc = "dev"

os.chdir(f".\{loc}")
subprocess.run(["python", "-u", "main.py"], shell=True)

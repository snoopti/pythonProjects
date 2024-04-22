import os
import time
import subprocess
import importlib

output_path = "./src/output"
input_path = "./src/input"

libraries = ["turtle", "pytube", "subprocess", "os", "tkinter", "random", "spotdl"]

def create_dirs():
    os.makedirs(output_path, exist_ok=True)
    os.makedirs(input_path, exist_ok=True)
    print("Directories created!")

def install_libs():
    missing_libs = []

    for lib in libraries:
        try:
            importlib.import_module(lib)
            print(f"{lib} is installed.")
        except ImportError:
            missing_libs.append(lib)

    if missing_libs:
        try:
            subprocess.run(["pip", "install", *missing_libs], check=True)
            print(f"Libraries installed: {', '.join(missing_libs)}")
        except subprocess.CalledProcessError as e:
            print(f"Error during installation: {e}")
    else:
        print("All libraries are already installed!")

print("Setting up...")

create_dirs()
time.sleep(1)
install_libs()

print("\nSetup complete!")
time.sleep(10)

import subprocess
import time
import os

# Find venv python executable path (adjust '.venv' to your folder name)
venv_python = os.path.join(".venv", "Scripts", "python.exe")

# Base config
image = "Yukimura.png"
x_scale = 1
script = "ascii.py"

# Loop through all 31 greyscales
for more in range(31):
    print(f"\n================= Greyscale {more} =================\n")

    # Build command
    command = [
        venv_python,
        script,
        "--img",
        image,
        "--x",
        str(x_scale),
        "--more",
        str(more),
    ]

    # Run and display output directly in terminal
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"[!] Error running scale {more}: {e}")

    time.sleep(2)  # Pause 2 seconds after each render

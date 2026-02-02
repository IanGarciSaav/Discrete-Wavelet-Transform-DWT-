import subprocess
import os

def run_script(script_name):
    # Set working directory to the project base (one level up from src)
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    subprocess.run(["python", script_name], check=True, cwd=base_dir)

if __name__ == "__main__":
    run_script("src/DWT.py")
    run_script("src/DistanciasEuclidianas.py")
    run_script("src/Media&DeviacionEstandar.py")
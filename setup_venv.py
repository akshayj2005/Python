import os
import shutil
import sys

def copy_sitecustomize():
    # Path to your virtual environment's site-packages
    venv_path = os.path.join(os.getcwd(), '.venv')
    site_packages = None

    # Find site-packages folder (different on Windows vs Linux/macOS)
    for root, dirs, files in os.walk(venv_path):
        if 'site-packages' in dirs:
            site_packages = os.path.join(root, 'site-packages')
            break

    if site_packages is None:
        print("Error: Could not find site-packages folder inside .venv")
        sys.exit(1)

    # Path to your custom script
    src = os.path.join(os.getcwd(), 'custom_scripts', 'sitecustomize.py')

    # Destination path
    dest = os.path.join(site_packages, 'sitecustomize.py')

    try:
        shutil.copy2(src, dest)
        print(f"Copied sitecustomize.py to {dest}")
    except Exception as e:
        print(f"Failed to copy sitecustomize.py: {e}")

if __name__ == "__main__":
    copy_sitecustomize()

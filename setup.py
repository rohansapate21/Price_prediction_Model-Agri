import subprocess
import sys

def install_requirements():
    """Install the required packages for the Crop Price Prediction application"""
    print("Installing required packages...")
    
    # List of required packages
    packages = [
        "flask",
        "flask-cors",
        "numpy",
        "scikit-learn"
    ]
    
    # Install packages
    for package in packages:
        print(f"Installing {package}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"✓ {package} installed successfully.")
        except subprocess.CalledProcessError:
            print(f"✗ Failed to install {package}. Please install it manually.")
    
    print("\nSetup complete. You can now run the application using start_app.bat or python start_app.py")

if __name__ == "__main__":
    install_requirements() 
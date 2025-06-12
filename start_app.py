import subprocess
import webbrowser
import os
import time
import sys

def main():
    print("Starting Crop Price Prediction Application...")
    
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Start the Flask server in a subprocess
    flask_process = None
    try:
        print("Starting Flask server...")
        flask_process = subprocess.Popen([sys.executable, 'app.py'], 
                                        cwd=current_dir,
                                        stdout=subprocess.PIPE, 
                                        stderr=subprocess.PIPE)
        
        # Wait a bit for the server to start
        time.sleep(2)
        
        # Open the application in the browser using the Flask server
        app_url = "http://localhost:5000/"
        print(f"Opening application in your browser at {app_url}")
        webbrowser.open(app_url)
        
        print("\nApplication started successfully!")
        print("- Flask server is running on http://localhost:5000")
        print("- Frontend is now open in your browser")
        print("\nPress Ctrl+C to stop the application")
        
        # Keep the script running until interrupted
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nShutting down the application...")
    finally:
        # Clean up the subprocess when done
        if flask_process:
            flask_process.terminate()
            print("Flask server stopped.")

if __name__ == "__main__":
    main() 
import subprocess
import webbrowser
import sys

def run_flask_app():

    python_dir = sys.executable

    flask_process = subprocess.Popen([python_dir, 'app.py'])
    webbrowser.open('http://localhost:5000')
    flask_process.wait()

if __name__ == '__main__':
    run_flask_app()

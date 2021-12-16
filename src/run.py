from src import app
from src.config import PORT, DEBUG

if __name__ == "__main__":
    print("Start server ....")
    if DEBUG:
        app.run(port=PORT, debug=True)
    else:
        app.run('0.0.0.0', port=PORT, debug=False)
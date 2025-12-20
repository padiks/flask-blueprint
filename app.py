# app.py - 2 (entry point)

from core.app_factory import create_app

app = create_app()

if __name__ == "__main__":
    app.run()

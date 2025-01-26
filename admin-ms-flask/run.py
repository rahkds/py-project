from app.app import create_app
from app.config.config import app_config

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=(app_config.get('PORT')))



from app.api import api
from app import create_app
from app.config import Config

config = Config()
app = create_app(config)
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
    

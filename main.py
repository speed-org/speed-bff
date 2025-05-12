from app.api import api
from app.utils.create_app import create_app


app = create_app()
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
    

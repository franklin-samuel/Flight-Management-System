from flask import Flask
from flasgger import Swagger
from backend.app.api.voos import routes

app = Flask(__name__)
app.register_blueprint(routes)

swagger = Swagger(app)

if __name__ == "__main__":
    app.run(debug=True)
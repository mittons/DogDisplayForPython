import os;
from flask import Flask
from flask_cors import CORS
from dog_app.routes import configure_routes
from dog_app.services import DogBreedService
from dog_app.config import *

def create_app(dog_breed_service=None):
    app = Flask(__name__)

    cors_config = {
        "origins": ["http://localhost:*"],  # Allows only requests from localhost. Change for production
        "methods": ["GET", "OPTIONS"],  # Allows only GET and OPTIONS methods
        "allow_headers": ["Origin", "Content-Type", "X-Custom-Signature-Header"],  # Specifies which headers can be used in the actual request
        "expose_headers": ["X-Custom-Signature-Header"],  # Exposes the specified headers
        "supports_credentials": False,  # If True, allows sending of cookies and authorization headers with requests
        "max_age": None  # Indicates how long the results of a preflight request can be cached
    }

    CORS(app, resources={
        "/": cors_config,
        "/renderBreeds": cors_config
    })

    env = os.environ.get('FLASK_ENV', 'development')
    if env == 'production':
        app.config.from_object(ProductionConfig)
    elif env == 'testing':
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    if dog_breed_service is None:
        dog_breed_service = DogBreedService(app.config['SERVICE_URL'])

    configure_routes(app, dog_breed_service)
    return app

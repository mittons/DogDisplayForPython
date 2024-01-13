from flask import render_template, jsonify, Response
from dog_app.services import DogBreedService
from dog_app import digital_signatures

def configure_routes(app, dog_breed_service):
    # -----------------------------------------------------------------------------------
    # | Route that serves the initial site, with a header and a request dog data button
    @app.route('/')
    def index():
        return create_signed_response(render_template("dog_screen_init.html"))

    # --------------------------------------------------------------------------
    # | Route that serves rendered dog breed data as partial html upon request
    @app.route('/renderBreeds', methods=['GET'])
    def render_breeds():
        data = dog_breed_service.get_data()
        if data:
            return create_signed_response(render_template("dog_breeds_partial.html", data=data))
        else:
            return jsonify({"error": "Error: Unable to fetch data from the external service"}), 500

    # This function generates a cryptographic signature for the data passed to it, using the private key made available in the current setup.
    #   - This is so that data recipients using the matching public key can authenticate the data before it is included in the html rendered by their browser.
    def create_signed_response(response_data):
        encoded_signature = digital_signatures.sign_data(response_data)
        response = Response(response_data)
        response.headers['X-Custom-Signature-Header'] = encoded_signature

        return response

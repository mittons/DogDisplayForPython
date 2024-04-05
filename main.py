import os
from dog_app import create_app

app = create_app()

if __name__ == '__main__':
    port = 5679 if os.environ.get('FLASK_ENV') == 'production' else 5678

    app.run(host="localhost", port=port, debug=False)

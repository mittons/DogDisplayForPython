from dog_app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host="localhost", port=5678, debug=False)

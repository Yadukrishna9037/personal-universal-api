from app import create_app

app = create_app()

if __name__ == '__main__':
    # Run the server in debug mode for development
    app.run(debug=True, port=5000)
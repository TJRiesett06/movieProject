from website import create_app

app = create_app()

if __name__ == '__main__': #run main to start website
    app.run(debug=True)


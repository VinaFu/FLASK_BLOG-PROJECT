from flaskblog import create_app

app = create_app()

if __name__=="__main__":
    app.run(debug=True)
    # means only call in ternimal via name, it can start debug mode
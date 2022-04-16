import app

the_app = app.wep_create_app()

if __name__ == "__main__":
    the_app.run(host="0.0.0.0", port=5000, debug=True)

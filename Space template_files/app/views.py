from app import app
@app.route("/")
def root_fun():
    return "Hello world"
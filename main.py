from flask import Flask, request, render_template, make_response


app = Flask(__name__)

@app.route("/index")
@app.route("/home")
@app.route("/")
def index():
    response  = make_response(render_template("index.html"))
    response.set_cookie('BogdanTest', 
    'testme123123', 
    max_age=3600,  #  hour (in seconds)
    expires=None,  
    path='/',      
    domain=None,   
    secure=True,   
    httponly=True  
    )
    return response

@app.route("/search")
def search():
    return render_template("search.html")
    BogdanTest = request.cookies.get('BogdanTest')

@app.route("/add")
def add():
    return render_template("add.html")
    BogdanTest = request.cookies.get('BogdanTest')

if __name__ == '__main__':
    app.run(debug=True)
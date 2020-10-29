from flask import Flask
app = Flask(__name__)

@app.route("/<int:number>", methods=["GET"])
def range():


@app.route("/<int:number>/odd", methods=["GET"])
def odd_range():

@app.route("/<int:number>/odd", methods=["GET"])
def even_range():


@app.route("")
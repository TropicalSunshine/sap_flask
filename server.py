from flask import Flask
import json

app = Flask(__name__)

@app.route("/<int:number>", methods=["GET"])
def default_range(number):
    result = []
    for n in range(1, number + 1):
        result.append(n)
    return {
        "result" : tuple(result)
    }

@app.route("/<int:number>/odd", methods=["GET"])
def odd_range(number):
    result = []
    for n in range(1, number + 1, 2):
        if(n % 2 == 1):
            result.append(n)
    return {
        "result" : tuple(result)
    }

@app.route("/<int:number>/even", methods=["GET"])
def even_range(number):
    result = []
    for n in range(2, number + 1, 2):
        result.append(n) 
    return {
        "result" : tuple(result)
    }


@app.route("/<int:number>/prime", methods=["GET"])
def prime_range(number):
    result = []
    s = [True] * number
    
    for a in range(2, number):
        if s[a] == True:
            result.append(a)
            
            for b in range(2, number):
                if (a * b) >= number:
                    break
                s[a * b] = False
    
    return {
        "result" : tuple(result)
    }


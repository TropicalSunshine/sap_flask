from flask import Flask
import json

app = Flask(__name__)

@app.route("/<int:number>", methods=["GET"])
def range(number):
    result = []
    for n in range(1, number + 1):
        result.append(n)
    return result

@app.route("/<int:number>/odd", methods=["GET"])
def odd_range(number):
    result = []
    for n in range(1, number + 1):
        if(n % 2 == 1):
            result.append(n)
    return result

@app.route("/<int:number>/even", methods=["GET"])
def even_range(number):
    result = []
    for n in range(1, number + 1):
        if(n % 2 == 0):
            result.append(n) 
    return result


@app.route("/<int:number>/prime", methods=["GET"])
def prime_range(number):
    result = [];
    s = [];
    
    for n in range(1, number + 1):
        s.append(True)
    
    from n in range(2, number + 1)
        if(s[n] == true):
            result.append(n);
            
            for b in range(2, number + 1):
                s[n * b] = False
    
    return result;


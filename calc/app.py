# Put your app in here.

from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def do_add():
    """Add a and b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)
    return str(result)

@app.route('/sub')
def do_sub():
    """Subtract b from a."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)
    return str(result)

@app.route('/mult')
def do_mult():
    """Multiply a and b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)
    return str(result)

# Further Study

@app.route('/div')
def do_div():
    """Divide a by b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)
    return str(result)

# Mapping of operation names to functions
operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}

@app.route("/math/<oper>")
def do_math(oper):
    """Perform the specified math operation on a and b."""
    
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    
    # Look up the operation in the dictionary and execute it
    result = operators[oper](a, b)

    return str(result)
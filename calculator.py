from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cal/<int:num1>/<op>/<int:num2>')
def calculate(num1, op, num2):
    if op == 'add':
        result = num1 + num2
    elif op == 'subtract':
        result = num1 - num2
    elif op == 'multiply':
        result = num1 * num2
    elif op == 'modulus':
        result = num1 % num2
    else:
        return "Invalid operation"

    return render_template('user.html', num1=num1, op=op, num2=num2, result=result)

if __name__ == '__main__':
    app.run(debug=True)

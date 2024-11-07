from flask import Flask, request

app = Flask(__name__)

@app.route('/joku-juttu')
def print_joku_juttu():
    return 'Siinä sulle joku kolmas juttu!'

@app.route('/sum')
def calculate_sum():
    # print(request.args.get('num2'))
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
    except ValueError:
        return 'Parameter error: use numbers!'
    except TypeError:
        return 'Parameter(s) missing!'
    return str(num1 + num2)

if __name__ == '__main__':
    app.run(use_reloader=True, port=3000)

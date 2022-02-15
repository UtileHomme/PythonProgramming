from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello world"


@app.route('/add_two_numbers', methods=['POST'])
def add_two_nums():
    # Get x,y from the posted data
    dataDict = request.get_json()

    if "x" not in dataDict:
        return "ERROR", 305
    x = dataDict['x']
    y = dataDict['y']
    z = x + y

    retJson = {
        "z": z
    }

    return jsonify(retJson), 200


@app.route('/hithere')
def hi_there_everyone():
    return 'I just hit hithere'


@app.route('/bye')
def bye():
    # c = 2 * 534l
    # s = str(c)

    ret_Json = {
        'Name': 'Elfarouk',
        'Age': 22,
        "phones": [
            {
                "phoneName": "Iphone8",
                "phoneNumber": 1111,
            },
            {
                "phoneName": "Nokia",
                "phoneNumber": 11121,
            }
        ]
    }
    return jsonify(ret_Json)


if __name__ == "__main__":
    app.run(port=5000, debug=True)

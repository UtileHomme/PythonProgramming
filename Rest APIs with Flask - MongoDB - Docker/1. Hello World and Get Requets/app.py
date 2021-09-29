from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello world"


@app.route('/hithere')
def hi_there_everyone():
    return 'I just hit hithere'


@app.route('/bye')
def bye():
    # c = 2 * 534
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

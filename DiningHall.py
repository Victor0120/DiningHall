from flask import Flask, request
import requests

order = {
    "order_id": 1,
    "table_id": 1,
    "waiter_id": 1,
    "items": [3, 4, 4, 2],
    "priority": 3,
    "max_wait": 45,
    "pick_up_time": 1631453140,
    "cooking_time": 65,
    "cooking_details": [
        {
            "food_id": 3,
            "cook_id": 1,
        },
        {
            "food_id": 4,
            "cook_id": 1,
        },
        {
            "food_id": 4,
            "cook_id": 2,
        },
        {
            "food_id": 2,
            "cook_id": 3,
        },
    ]

}

app = Flask(__name__)


@app.route("/", methods=['POST'])
def home():
    data = request.form
    order_id = data['order_id']
    table_id = data['table_id']
    print(order_id)
    print(table_id)
    return 'Orders Distributed'


@app.route("/distribution")
def distribution():
    r = requests.post("http://192.168.0.103:5000/", data=order)
    return print(r.text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True, threaded=True)

from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify('Hello, World!')

@app.route('/home')
def get_home():
    return jsonify('You are now home!')

@app.route('/users')
def get_users():
    users = [
        {"id":1,"name":"Erik K", "country": "se"},
        {"id":2,"name":"Erik N", "country": "se"},
        {"id":3,"name":"Tommy", "country": "se"},
        {"id":4,"name":"Tatiana", "country": "se"},
        {"id":5,"name":"Victor", "country": "se"},
        {"id":6,"name":"Emma", "country": "se"},
    ]
    return jsonify(users=users)

if __name__ == '__main__':
    app.run()
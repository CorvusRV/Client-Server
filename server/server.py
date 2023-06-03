import json
from flask import Flask, request
from data_process import Processing


app = Flask(__name__)
Processing.creating_db()

@app.route('/db/resources', methods=['GET'])
def get_data():
    data = Processing.get_data_from_db()
    return json.dumps(data)

@app.route('/db/save', methods=['POST'])
def post_data():
    json_date = request.get_json()
    Processing.writing_data_to_db(json_date)
    return json.dumps('200')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)

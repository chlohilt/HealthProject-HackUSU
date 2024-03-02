from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/api/process-data', methods=['POST'])
def process_data():
    data = request.json
    # Convert JSON array to Python list
    data_list = list(data)
    
    # Process the list here (edit as needed)
    processed_list = [x * 2 for x in data_list]  # Example processing
    
    # Convert list back to JSON array and return
    return jsonify(processed_list)

if __name__ == '__main__':
    app.run(debug=True, port=5700)

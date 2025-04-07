from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/notify', methods=['POST'])
def notify():
    data = request.json
    return jsonify({"message": f"Notification sent to {data['email']}"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)

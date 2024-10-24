from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print(data)
    return jsonify({'message': 'Webhook erfolgreich empfangen!'})

if __name__ == '__main__':
    app.run(debug=True)
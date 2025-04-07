from flask import Flask, request, jsonify

app = Flask(__name__)

products = []

@app.route('/products', methods=['POST'])
def add_product():
    data = request.json
    product = {'id': len(products) + 1, 'name': data['name'], 'price': data['price']}
    products.append(product)
    return jsonify(product), 201

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

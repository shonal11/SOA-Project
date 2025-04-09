from flask import Flask, request, jsonify

app = Flask(__name__)

restaurants = []

@app.route('/restaurants', methods=['POST'])
def add_restaurant():
    data = request.json
    if 'name' not in data or 'address' not in data:
        return jsonify({"error": "Restaurant name and address are required"}), 400
    restaurant = {'id': len(restaurants) + 1, 'name': data['name'], 'address': data['address'], 'menus': []}
    restaurants.append(restaurant)
    return jsonify(restaurant), 201

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    return jsonify(restaurants)

@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = next((r for r in restaurants if r['id'] == id), None)
    if restaurant is None:
        return jsonify({"error": "Restaurant not found"}), 404
    return jsonify(restaurant)

@app.route('/restaurants/<int:id>/menus', methods=['POST'])
def add_menu(id):
    restaurant = next((r for r in restaurants if r['id'] == id), None)
    if restaurant is None:
        return jsonify({"error": "Restaurant not found"}), 404
    data = request.json
    if 'name' not in data or 'price' not in data:
        return jsonify({"error": "Menu item name and price are required"}), 400
    menu_item = {'id': len(restaurant['menus']) + 1, 'name': data['name'], 'price': data['price']}
    restaurant['menus'].append(menu_item)
    return jsonify(menu_item), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)

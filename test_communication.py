import requests

# Test communication from User Service to Restaurant Service
user_service_url = 'http://localhost:5001/users'
restaurant_service_url = 'http://localhost:5004/restaurants'
product_service_url = 'http://localhost:5002/products'

# Fetching data from User Service
user_response = requests.get(user_service_url)
print(f"User Service Response: {user_response.status_code} - {user_response.json()}")

# Fetching data from Restaurant Service
restaurant_response = requests.get(restaurant_service_url)
print(f"Restaurant Service Response: {restaurant_response.status_code} - {restaurant_response.json()}")

# Fetching data from Product Service
product_response = requests.get(product_service_url)
print(f"Product Service Response: {product_response.status_code} - {product_response.json()}")

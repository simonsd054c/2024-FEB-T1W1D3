from flask import Flask, request

app = Flask(__name__)

# base_url/
@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/another_route")
def another_route():
    return "This is another route"

@app.route("/one_more_route")
def one_more_route():
    return "One more route."

products = [
    {
        "id": 0,
        "title": "Product 0",
        "price": 110
    },
    {
        "id": 1,
        "title": "Product 1",
        "price": 50
    },
    {
        "id": 2,
        "title": "Product 2",
        "price": 70
    },
    {
        "id": 3,
        "title": "Product 3",
        "price": 70
    },
    {
        "id": 4,
        "title": "Product 4",
        "price": 70
    },
    {
        "id": 5,
        "title": "Product 5",
        "price": 70
    },
    {
        "id": 6,
        "title": "Product 6",
        "price": 70
    }
]

@app.route("/products")
def get_products():
    limit = request.args.get("limit")
    if limit:
        limit = int(limit)
        return products[0:limit]
    else:
        return products

@app.route("/products/0")
def get_product_0():
    return products[0]

@app.route("/products/2")
def get_product_2():
    return { "error": "Product Not Found." }, 404

# Create a new product
@app.route("/products", methods=["POST"])
def create_product():
    # get the info from the request body
    body_data = request.get_json()
    print(body_data)
    products.append(body_data)
    return products

# Delete a product
@app.route("/products/1", methods=["DELETE"])
def delete_product_1():
    del products[1]
    return {"message": "Product 1 deleted successfully"}

# Updating a product using PUT
@app.route("/products/2", methods=["PUT"])
def update_product2_put():
    body_data = request.get_json()
    products[2] = body_data
    return products[2]

# Update a product using PATCH
@app.route("/products/3", methods=["PATCH"])
def update_product3_patch():
    body_data = request.get_json()
    products[3]["title"] = body_data.get("title") or products[3]["title"]
    products[3]["price"] = body_data.get("price") or products[3]["price"]
    return products[3]
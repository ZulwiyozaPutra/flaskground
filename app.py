from flask import Flask, jsonify, request, render_template
from stores import stores

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/stores/", methods=["POST"])
def post_store():
    data = request.get_json()
    store = {
        "name": data["name"],
        "items": [] if (data["items"] is None) else data["items"]
    }
    stores.append(store)
    message = "a store %s added!" % store
    return jsonify({"message": message})


@app.route("/stores/<string:name>/")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store)
        else:
            message = "There is no store named %s" % name
            return jsonify({"message": message})


@app.route("/stores/")
def get_stores():
    json_stores = jsonify({"stores": stores})
    return json_stores


@app.route("/stores/<string:name>/items", methods=["POST"])
def post_item(name):
    for store in stores:
        if store["name"] == name:
            data = request.get_json()
            item = {
                "name": data["name"],
                "price": data["price"]
            }
            store["items"].append(item)
            message = "an item %s added!" % item
            return jsonify({"message": message})
        else:
            message = "There is no store named %s" % name
            return jsonify({"message": message})


@app.route("/stores/<string:name>/items/")
def get_item(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store["items"])
        else:
            message = "There is no store named %s" % name
            return jsonify({"message": message})


app.run(debug=True)

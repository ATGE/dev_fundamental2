from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["POST"])
def hello():
    return "Hello World!"



from flask import Flask
from truck_delivery_pamy.content_manager import ContentManager
from api.views import client_api


app = Flask(__name__)

app.add_url_rule("/clients", view_func=client_api.list_clients)
app.add_url_rule("/clients", view_func=client_api.save_client, methods=["POST"])
app.add_url_rule("/clients/<client_id>", view_func=client_api.get_client_by_id)
app.add_url_rule("/clients/<client_id>", view_func=client_api.delete_client_by_id, methods=["DELETE"])


if __name__ == "__main__":
    connector = ContentManager()
    app.run(host="0.0.0.0", debug=True, use_reloader=True)

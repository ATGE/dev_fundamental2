import json
from flask import request, jsonify
from truck_control.content_manager import ContentManager
from truck_control.client import Client

CLIENT_TYPE = "client"


def list_clients():
    connector = ContentManager()
    connector.get_all(CLIENT_TYPE)
    return jsonify({"message": "the client was saved successfully"})


def save_client():
    a = request.json
    keys = ["name", "email", "cellphone", "address"]
    for k in keys:
        if k not in a:
            raise jsonify({"message": f"{k} parameters are required"})
    client_obj = Client(a["name"],
                        a["email"],
                        a["cellphone"],
                        a["address"],
                        )
    connector = ContentManager()
    connector.save_document(client_obj.name, client_obj.__dict__, CLIENT_TYPE)
    return jsonify({"message": "the client was saved successfully"})


def get_client_by_id(client_id):
    connector = ContentManager()
    result = connector.get_document(client_id, CLIENT_TYPE)
    if result:
        return jsonify(json.loads(result))
    else:
        return jsonify({"message": "Not found"}), 404


def delete_client_by_id(client_id):
    connector = ContentManager()
    connector.delete(client_id, CLIENT_TYPE)
    return jsonify({"message": "client was deleted successfully"})



class Client:
    def __init__(self, name, email, cellphone, address):
        self.name = name
        self.email = email
        self.cellphone = cellphone
        self.address = address
        self.address_start_point = address
        self.address_end_point = address

    def to_dict(self):
        return {}

    def get_all_routes(self):
        pass


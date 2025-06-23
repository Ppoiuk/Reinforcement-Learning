import json

class FileIOManager:
    @staticmethod
    def save_to_json(data, filename):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def load_from_json(filename):
        with open(filename, 'r') as f:
            return json.load(f)
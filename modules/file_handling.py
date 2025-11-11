import json

class FileHandling:

    @staticmethod
    def writing_for_jason(data, json_file):
            with open(json_file, "w") as f:
                new_data = json.dumps(data, indent=4)
                f.write(new_data)


    @staticmethod
    def conversion_to_python(json_file):
        with open(json_file) as j:
            python_data = json.load(j)
        return python_data

from csv import DictReader, DictWriter
from pathlib import Path

from check_if_file_exists import check_if_file_exists


class DataBaseOperations:
    def __init__(self, path_to_file="files") -> None:
        self.path_to_file = path_to_file
        self.encoding = "utf_8"

    def create_file_name(self, model_class) -> str:
        """
        This function creates a file from the model class name

        The first line creates the file name from the model class
        """
        # Modal name and content
        modal_name = model_class.__class__.__name__
        model_dict = vars(model_class)

        # File name and headers
        file_name = Path(f"{self.path_to_file}/{modal_name.lower()}.csv")
        fields = [attribute for attribute in model_dict]

        # We check if the file exists before return the file
        check_if_file_exists(file_name, self.encoding, fields)

        return file_name

    def create_dictionary(self, model_class):
        """
        This function creates a dictionary from the model class
        and returns it as well as the name of teh model class being passed in
        """

        model_dict = vars(model_class)
        fields = [field for field in model_dict]

        return model_dict, fields

    def write_to_file(self, model_class) -> None:
        """
        Write items from a model_class to file
        """
        file_name = self.create_file_name(model_class)
        model_dict, fields = self.create_dictionary(model_class)

        content = {f"{key}": val for key, val in model_dict.items()}

        with open(file_name, "a", encoding=self.encoding, newline="") as file:
            csvWriter = DictWriter(file, fieldnames=fields)
            csvWriter.writerow(content)

    def read_from_file(self, model_class) -> list[object]:
        """
        Reade items from a model_class from file
        """

        file_name = self.create_file_name(model_class)
        _, fields = self.create_dictionary(model_class)

        model_class_list = []

        with open(file_name, encoding=self.encoding, newline="") as file:
            csvReader = DictReader(file, fields)
            next(csvReader)
            for row in csvReader:
                model_instance = model_class.__class__(**row)
                model_class_list.append(model_instance)
        return model_class_list

    def update_file(self, model_class) -> None:
        """
        Update an item in a file
        """

        # Read the file and get all the model classes stored in a list
        old_file = self.read_from_file(model_class)
        file_name = self.create_file_name(model_class)
        fields = [attribute for attribute in vars(model_class)]

        with open(file_name, "w", encoding=self.encoding, newline="") as file:
            writer = DictWriter(file, fieldnames=fields)
            writer.writeheader()

        for item in old_file:
            if item.id == model_class.id:
                self.write_to_file(model_class)
            else:
                self.write_to_file(item)

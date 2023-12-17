from data_base_operations import DataBaseOperations
from models import Dog

data_base_operation = DataBaseOperations()
dog = Dog()

new_dog = Dog()
new_dog.id = "234"
new_dog.name = "Balto"
new_dog.age = 10
new_dog.color = "Gray"

# output = data_base_operation.update_file(dog)
output = data_base_operation.update_file(new_dog)

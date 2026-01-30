monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}
monday_class.add("Grace")
print(f"Monday class: {monday_class}")
print(f"Wednesday class: {wednesday_class}")
print(f"Attended both classes: {monday_class & wednesday_class}") # & = shift + 7
print(f"Attended either class: {monday_class | wednesday_class}") # | = pipe, shift + \
print(f"Only Monday: {monday_class - wednesday_class}")
print(f"Only one class (not both): {monday_class ^ wednesday_class}") # ^ = Caret, shift + 6
all_classes = monday_class | wednesday_class
print("Is Monday subset of all students? ",monday_class <= all_classes) #True
fruits = ["Apple", "Pear", "Orange"]


# TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")


# try:
make_pie(4)
# except IndexError as error_message:
#     print(f"The code fail because of: '{error_message}'")
# else:
#     print("Execution completed successfully")

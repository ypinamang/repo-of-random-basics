def length_of_each(list_of_strings):
    """Takes a list of strings and returns the number of characters for
    each string in a dictionary."""
    char_count = {}  # Dictionary to contain string: char_count
    for string in list_of_strings:
        char_count[string] = len(string)
    return char_count


# example test case
names_of_students = ["Jack", "Aurelia", "Samuel", "Nana Kwame", "Ronaldo"]
names_length = length_of_each(names_of_students)
print(names_length)  # You can print the char length of all student names
print(
    names_length["Nana Kwame"]
)  # You can print the char length of a sing student's name.


# I wonder where this has utility in the real world?

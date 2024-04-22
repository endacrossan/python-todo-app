def get_todos(filepath="store.txt"):  # setting store.txt as default parameter, this can be changed on the fly
    """ Reads txt file and return list
     for each line item
     """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


# write to todos file
def write_todos(todos_local, filepath="store.txt"):  # function with parameters
    """ Write to text file with new list of to do items. """
    with open(filepath, 'w') as file_local:
        todos_local = file_local.writelines(todos_local)


# print(__name__)   # the name is main inside any file that this is directly called from
if __name__ == "__main__":
    print(get_todos())

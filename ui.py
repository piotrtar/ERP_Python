

def print_table(table, title_list):
    """
    Prints table with data. Sample output:
        /-----------------------------------\
        |   id   |      title     |   type  |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table: list of lists - table to display
        title_list: list containing table headers

    Returns:
        This function doesn't return anything it only prints to console.
    """

    table = [title_list] + table
    list_max_elem_col = search_max_width_col(table, title_list)
    sum_list_max = 0
    for elem in list_max_elem_col:
        sum_list_max += elem
    print('/' + '-' * ((5*len(list_max_elem_col)) - 1) + '-' * sum_list_max + '\\')
    print_row_data(table, list_max_elem_col)
    print('\\' + '-' * ((5*len(list_max_elem_col)) - 1) + '-' * sum_list_max + '/')


def print_result(result, label):
    """
    Displays results of the special functions.
    Args:
        result: string, list or dictionary - result of the special function
        label: label of the result
    Returns:
        This function doesn't return anything it only prints to console.
    """

    print(label + ': ')
    if type(result) == str:
        print(result)

    elif type(result) == list:
        print(result)
    elif type(result) == dict:
        for key, value in result.items():
            print(str(key) + ':' + str(value))


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program
    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")
    Returns:
        This function doesn't return anything it only prints to console.
    """
    print(title)
    for i in range(0, len(list_options)):
        print('   ', '(%d) %s' % ((i + 1), list_options[i]))
    print('   ', '(0) %s' % exit_message)


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>
    Args:
        list_labels: list of strings - labels of inputs
        title: title of the "input section"
    Returns:
        List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []
    print(title)
    for question in list_labels:
        user_input = input(question + ": ")
        inputs.append(user_input)
    return inputs


# This function displays an error message. (example: Error: @message)
#
# @message: string - the error message
def print_error_message(message):
    """
    Displays an error message
    Args:
        message(str): error message to be displayed
    Returns:
        This function doesn't return anything it only prints to console.
    """
    print(message)


def search_max_width_col(table, title_list):
    ammount_of_column = len(table[0])

    max_elem_col = 0
    list_max_elem_col = []
    for i in range(ammount_of_column):
        for j in range(len(table)):
            if max_elem_col < len(table[j][i]):
                max_elem_col = len(table[j][i])
        list_max_elem_col += [max_elem_col]
        max_elem_col = 0

    return list_max_elem_col


def print_row_between_row(list_max_elem_col):
    for item in list_max_elem_col:
        print('|' + '-'*(item+4), end='')
    print('|')


def print_row_data(table, list_max_elem_col):
    for j in range(len(table)):
        for i in range(len(list_max_elem_col)):
            print('|' + '  ' + str(table[j][i]) + ' '*(list_max_elem_col[i] - len(table[j][i]) + 2), end='')
        print('|')
        if j == (len(table) - 1):
            break
        print_row_between_row(list_max_elem_col)

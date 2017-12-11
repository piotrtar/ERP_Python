# data structure:
# id: string
#     Unique and randomly generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# email: string
# subscribed: boolean (Is she/he subscribed to the newsletter? 1/0 = yes/not)


# importing everything you need
import os
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """

    name = ''
    len_name = len(__name__)
    for i in range(len_name//2):
        name += __name__[i]

    start_module = 1
    option = '1'
    while start_module > 0 and option != '0':
        try:
            table = data_manager.get_table_from_file('crm/customers.csv')

            list_options = ['show table', 'add product', 'remove product', 'update table',
                            'which year max', 'avg amount']

            ui.print_menu('%s menu' % name, list_options, 'main menu')

            inputs = ui.get_inputs(["Please enter a number: "], "")

            option = inputs[0]
            if option == "1":
                show_table(table)
            elif option == "2":
                add(table)
            elif option == "3":
                remove(table, id_=ui.get_inputs(['Please give me unique id person'], ''))
            elif option == "4":
                update(table, id_=ui.get_inputs(['Please give me unique id person'], ''))
            elif option == "5":
                result = get_longest_name_id(table)
                label = 'Get longest name id: '
                ui.print_result(result, label)
            elif option == "6":
                result = get_subscribed_emails(table)
                label = "Customers who subscribed to the newsletter"
                ui.print_result(result, label)
            elif option == "0":
                start_module = 0
            else:
                raise KeyError("There is no such option.")

        except KeyError as err:
            ui.print_error_message(err)


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """

    title_list = ['id', 'name', 'email', 'subscribed']
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """

    id_ = common.generate_random(table)
    data_to_add = ui.get_inputs(['name', 'email', 'subscribed'], "Please provide your information")
    data_to_add.insert(0, id_)
    table.append(data_to_add)
    data_manager.write_table_to_file('crm/customers.csv', table)
    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table: table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        Table without specified record.
    """

    for lists in table:
        if id_[0] == lists[0]:
            table.remove(lists)

    data_manager.write_table_to_file('crm/customers.csv', table)

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        table with updated record
    """

    for lists in table:
        if id_[0] == lists[0]:
            new_list = ui.get_inputs(['name', 'email', 'subscribed'], "Please provide your personal information")
            lists[1] = new_list[0]
            lists[2] = new_list[1]
            lists[3] = new_list[2]

    data_manager.write_table_to_file("crm/customers.csv", table)

    return table


# special functions:
# ------------------


# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first by descending alphabetical order
def get_longest_name_id(table):
    result = print_longest_id_result(table)
    return result


def maximum_name(table):
    name_array = []
    for i in range(len(table)):
        name = table[i][1]
        name_array.append(name)
    maximum = max([len(x) for x in name_array])
    return maximum

def id_user_from_maximum(table):
    name_arrange = []
    maximum = maximum_name(table)
    for item in table:
        number = len(item[1])
        name = item[1]
        id_user = item[0]
        if number == maximum:
            name_arrange.append(name)
    data_list = name_arrange[0]
    result = []
    for elem in name_arrange:
        if elem < data_list:
            result += [elem]

    return result


def print_longest_id_result(table):
    result = id_user_from_maximum(table)
    first_elem = result[0]
    for element in table:
        name = element[1]
        id_ = element[0]
        result = id_
        if name == first_elem:
            return result

# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    new_array = []
    for i in range(len(table)):
        result = table[i][3]
        mail = table[i][2]
        name = table[i][1]
        separator = ";"
        if result == "1":
            new_array.append(mail + separator + name)
        result = new_array
        return result

# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# manufacturer: string
# purchase_date: number (year)
# durability: number (year)


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
            table = data_manager.get_table_from_file('inventory/inventory.csv')
            list_options = ['show table', 'add product', 'remove product', 'update table',
                            'get available items', 'get average durability by manufacturers']

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
                result = get_available_items(table)
                label = 'Get available items: '
                ui.print_result(result, label)
            elif option == "6":
                result = get_average_durability_by_manufacturers(table)
                label = 'Get average durability by manufacturer: '
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
    title_list = ['id', 'name', 'manufacturer', 'purchase date', 'durability']
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
    data_to_add = ui.get_inputs(['name', 'manufacturer', 'purchase date', 'durability'], "Please provide information")
    data_to_add.insert(0, id_)
    table.append(data_to_add)
    data_manager.write_table_to_file("inventory/inventory.csv", table)

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

    data_manager.write_table_to_file('inventory/inventory.csv', table)

    return table


def update(table, id_):

    for lists in table:
        if id_[0] == lists[0]:
            new_list = ui.get_inputs(['name', 'manufacturer', 'purchase date', 'durability'], "Please provide your information")
            lists[1] = new_list[0]
            lists[2] = new_list[1]
            lists[3] = new_list[2]
            lists[4] = new_list[3]

    data_manager.write_table_to_file("inventory/inventory.csv", table)

    return table


# special functions:
# ------------------

# the question: Which items have not exceeded their durability yet?
# return type: list of lists (the inner list contains the whole row with their actual data types)
#
# @table: list of lists
def get_available_items(table):
    lists_actual_items = []
    actual_date = 2017
    for i in range(len(table)):
        if int(table[i][3]) + int(table[i][4]) >= actual_date:
            table[i][3] = int(table[i][3])
            table[i][4] = int(table[i][4])
            lists_actual_items += [table[i]]

    result = lists_actual_items

    return result

# the question: What are the average durability times for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
#
# @table: list of lists

def get_average_durability_by_manufacturers(table):
    dict_sum = {}
    dict_num = {}
    number_manufact = []


    for i in range(len(table)):
        if table[i][2] in dict_sum:
            dict_sum[table[i][2]] += int(table[i][4])
        elif table[i][2] not in dict_sum:
            dict_sum[table[i][2]] = int(table[i][4])


    for i in range(len(table)):
        number_manufact.append(table[i][2])
    for element in range(len(number_manufact)):
        if number_manufact[element] in dict_num:
            dict_num[number_manufact[element]] += 1
        elif number_manufact[element] not in dict_num:
            dict_num[number_manufact[element]] = 1
    result = {}
    for key in dict_num:
        if key in dict_sum:
            result[key] = dict_sum[key]/dict_num[key]

    return result


def main():
    pass


if __name__ == '__main__':
    main()

# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# manufacturer: string
# price: number (dollars)
# in_stock: number

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

    start_module = 1
    option = '1'
    while start_module > 0 and option != '0':
        try:
            table = data_manager.get_table_from_file('store/games.csv')

            list_options = ['show table', 'add product', 'remove product', 'update table',
                            'get counts by manufacturers', 'get average by manufacturer']

            ui.print_menu('store menu', list_options, 'main menu')

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
                result = get_counts_by_manufacturers(table)
                label = 'Different kinds of game are available of each manufacturer'
                ui.print_result(result,label)
            elif option == "6":
                manufacturers = []
                for i in range(len(table)):
                    manufacturers.append(table[i][2])
                manufacturer = None
                while manufacturer not in manufacturers:
                    manufacturer = ui.get_inputs(['manufacturer'], "Please provide name of the manufacturer: ")[0]
                result = get_average_by_manufacturer(table, manufacturer)
                label = 'Closest to average age persons '
                ui.print_result(str(result), label)
                exit()
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

    title_list = ['id', 'title', 'manufacturer', 'price', 'in stock']
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
    data_to_add = ui.get_inputs(['title', 'manufacturer', 'price', 'in stock'], "Please provide information")
    data_to_add.insert(0, id_)
    table.append(data_to_add)
    data_manager.write_table_to_file("store/games.csv", table)

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

    data_manager.write_table_to_file('store/games.csv', table)

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
            new_list = ui.get_inputs(['title', 'manufacturer', 'price', 'in stock'], "Please provide your information")
            lists[1] = new_list[0]
            lists[2] = new_list[1]
            lists[3] = new_list[2]
            lists[4] = new_list[3]

    data_manager.write_table_to_file("store/games.csv", table)

    return table


# special functions:
# ------------------

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):

    dict_num = {}
    number_manufacturers = []

    for i in range(len(table)):
        number_manufacturers.append(table[i][2])
    for element in range(len(number_manufacturers)):
        if number_manufacturers[element] not in dict_num:
            dict_num[number_manufacturers[element]] = 1
        elif number_manufacturers[element] in dict_num:
            dict_num[number_manufacturers[element]] += 1

    return dict_num


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_average_by_manufacturer(table, manufacturer):


    games_in_stock = 0
    series_of_games = 0
    for i in range(len(table)):
        if table[i][2] == manufacturer:
            games_in_stock += int((table[i][4]))
            series_of_games += 1

    average_num_of_games = games_in_stock/series_of_games
    return average_num_of_games

def main():
    pass

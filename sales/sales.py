# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# price: number (the actual sale price in $)
# month: number
# day: number
# year: number
# month,year and day combined gives the date the sale was made

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
            table = data_manager.get_table_from_file('sales/sales.csv')

            list_options = ['show table', 'add product', 'remove product', 'update table',
                            'get lowest price item id', 'get items sold between']

            ui.print_menu('%s menu' % name, list_options, 'main menu')

            inputs = ui.get_inputs(["Please enter a number: "], "")

            option = inputs[0]

            if option == "1":
                show_table(table)
            elif option == "2":
                add(table)
            elif option == "3":
                remove(table, id_=ui.get_inputs(['Please gibve me unique id person'], ''))
            elif option == "4":
                update(table, id_=ui.get_inputs(['Please gibve me unique id person'], ''))
            elif option == "5":
                result = get_lowest_price_item_id(table)
                label = 'Get lowest price item: '
                ui.print_result(result, label)
            elif option == "6":
                result = get_items_sold_between(table, 'month_from', 'day_from', 'year_from', 'month_to', 'day_to', 'year_to')
                label = 'Get items sold between: '
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

    title_list = ['id', 'title', 'price', 'month', 'day', 'year']
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
    data_to_add = ui.get_inputs(['title', 'price', 'month', 'day', 'year'], "Please provide information")
    data_to_add.insert(0, id_)
    table.append(data_to_add)
    data_manager.write_table_to_file("sales/sales.csv", table)

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

    data_manager.write_table_to_file('sales/sales.csv', table)

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
            new_list = ui.get_inputs(['title', 'price', 'month', 'day', 'year'], "Please provide your information")
            lists[1] = new_list[0]
            lists[2] = new_list[1]
            lists[3] = new_list[2]
            lists[4] = new_list[3]
            lists[5] = new_list[4]

    data_manager.write_table_to_file("sales/sales.csv", table)

    return table


# special functions:
# ------------------

# the question: What is the id of the item that was sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first by descending alphabetical order
def get_lowest_price_item_id(table):
    id_min = []
    min_price = table[0][2]
    for i in range(len(table)):
        if min_price > table[i][2]:
            min_price = table[i][2]

    for i in range(len(table)):
        if min_price == table[i][2]:
            id_min += [table[i][0]]
    if len(id_min) > 1:
        result = id_min[0]
        for elem in id_min:
            if elem < result:
                result = elem
    else:
        result = id_min[0]

    return result


# the question: Which items are sold between two given dates ? (from_date < sale_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    first_date_sold = ui.get_inputs(['day from', 'month from', 'year form'], "Please provide your start search data, Order is important, example no space 20 5 2017 ")
    last_date_sold = ui.get_inputs(['day to', 'month to', 'year to'], "Please provide your information")
    year_list = []
    all_input_mounth = [first_date_sold[1], last_date_sold[1]]
    all_year = first_date_sold + last_date_sold
    subtraction = int(last_date_sold[2]) - int(first_date_sold[2])
    dict_year = {}
    year_list_without = []
    mounth_list = []
    mounth_list_without = []
    if subtraction > 1:
        for i in range(len(table)):
            for x in range(int(first_date_sold[2]), int(last_date_sold[2])+1):
                if x == int(table[i][-1]) and str(x) not in all_year:
                    year_list += [table[i]]
                elif x == int(table[i][-1]) and str(x) in all_year:
                    year_list_without += [table[i]]

    else:

        for i in range(len(table)):
            if table[i][-1] in all_year:
                year_list += [table[i]]

    mounth_all = 12 + int(last_date_sold[1])
    for x in range(len(year_list_without)):
        for i in range(int(first_date_sold[1]), mounth_all + 1):
            if str(i) == year_list_without[x][3] and str(i) in all_input_mounth:
                mounth_list += [year_list_without[x]]
            elif str(i) == year_list[x][3] and str(i) not in all_input_mounth:
                mounth_list_without += [year_list[x]]

    if subtraction == 0:
        for x in range(len(year_list)):
            for i in range(int(first_date_sold[1]), int(last_date_sold[1])+1):
                if str(i) == year_list[x][3] and str(i) in all_input_mounth:
                    mounth_list += [year_list[x]]
                elif str(i) == year_list[x][3] and str(i) not in all_input_mounth:
                    mounth_list_without += [year_list[x]]

    last_day = 30 + int(last_date_sold[0])
    day_list = []
    j = 0
    for x in range(len(mounth_list)):
        for i in range(int(first_date_sold[0]), last_day + 1):
            if i > 30:
                j += 1
                if j == int(mounth_list[x][4]) and mounth_list[x][4] not in day_list:
                    day_list += [mounth_list[x]]
            elif i == int(mounth_list[x][4]):
                day_list += [mounth_list[x]]

    result = [day_list, mounth_list_without, year_list]

    return result


def main():
    pass


if __name__ == '__main__':
    main()

# data structure:
# id: string
#     Unique and randomly generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string (in = income, out = outcome)
# amount: number (dollar)


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
            table = data_manager.get_table_from_file('accounting/items.csv')

            list_options = ['show table', 'add product', 'remove product', 'update table',
                            'which year max profit', 'get average amount']

            ui.print_menu('%s menu' % name, list_options, 'main menu')

            inputs = ui.get_inputs(["Please enter a number: "], "")

            option = inputs[0]
            if option == "1":
                show_table(table)
            elif option == "2":
                add(table)
            elif option == "3":
                remove(table, id_=ui.get_inputs(['Please give me unique id'], ''))
            elif option == "4":
                update(table, id_=ui.get_inputs(['Please give me unique id'], ''))
            elif option == "5":
                result = which_year_max(table)
                label = 'Year'
                ui.print_result(result, label)
            elif option == "6":
                average_profit = avg_amount(table, year=ui.get_inputs(['Please give me year'], ''))
                label = 'Average (per item) profit in a given year'
                ui.print_result(average_profit, label)
            elif option == "0":
                break
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

    title_list = ['id', 'month', 'day', 'year', 'type', 'amount']
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
    data_to_add = ui.get_inputs(['month', 'day', 'year', 'type', 'amount'], "Please provide your information")
    data_to_add.insert(0, id_)
    table.append(data_to_add)
    data_manager.write_table_to_file("accounting/items.csv", table)
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

    data_manager.write_table_to_file('accounting/items.csv', table)

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
            new_list = ui.get_inputs(['month', 'day', 'year', 'type', 'amount'], "Please provide your personal information")
            lists[1] = new_list[0]
            lists[2] = new_list[1]
            lists[3] = new_list[2]
            lists[4] = new_list[3]
            lists[5] = new_list[4]

    data_manager.write_table_to_file("accounting/items.csv", table)

    return table


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):

    list_in_15 = []
    list_out_15 = []
    list_in_16 = []
    list_out_16 = []
    element_in_15 = []
    element_in_16 = []
    avaidable_date = []
    for i in range(len(table)):
        if table[i][3] not in avaidable_date:
            avaidable_date.append(table[i][3])
    for lists in table:
        if lists[3] == avaidable_date[1]:
            element_in_15.append(lists[3])
            if lists[4] == 'in':
                list_in_15.append(int(lists[5]))
            if lists[4] == 'out':
                list_out_15.append(int(lists[5]))
        if lists[3] == avaidable_date[0]:
            element_in_16.append(lists[3])
            if lists[4] == 'in':
                list_in_16.append(int(lists[5]))
            if lists[4] == 'out':
                list_out_16.append(int(lists[5]))

    profit_15 = sum_list(list_in_15) - sum_list(list_out_15)
    profit_16 = sum_list(list_in_16) - sum_list(list_out_16)

    if profit_15 > profit_16:
        highest_year = avaidable_date[1]
    else:
        highest_year = avaidable_date[0]

    result = int(highest_year)

    return result

def sum_list(grades):
    summ = 0
    for n in grades:
        summ += n
    return summ

# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):

    list_in_15 = []
    list_out_15 = []
    list_in_16 = []
    list_out_16 = []
    element_in_15 = []
    element_in_16 = []
    avaidable_date = []
    for i in range(len(table)):
        if table[i][3] not in avaidable_date:
            avaidable_date.append(table[i][3])
    for lists in table:
        if lists[3] == avaidable_date[1]:
            element_in_15.append(lists[3])
            if lists[4] == 'in':
                list_in_15.append(int(lists[5]))
            if lists[4] == 'out':
                list_out_15.append(int(lists[5]))
        if lists[3] == avaidable_date[0]:
            element_in_16.append(lists[3])
            if lists[4] == 'in':
                list_in_16.append(int(lists[5]))
            if lists[4] == 'out':
                list_out_16.append(int(lists[5]))

    profit_15 = sum_list(list_in_15) - sum_list(list_out_15)
    profit_16 = sum_list(list_in_16) - sum_list(list_out_16)
    year_to_string = year[0]
    if year_to_string == avaidable_date[1]:
        average_profit = profit_15/len(element_in_15)
    elif year_to_string == avaidable_date[0]:
        average_profit = profit_16/len(element_in_16)
    else:
        average_profit = 'No data in this year'

    return str(average_profit)


def main():
    pass


if __name__ == '__main__':
    main()

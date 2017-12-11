# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


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
            table = data_manager.get_table_from_file('hr/persons.csv')
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
                result = get_oldest_person(table)
                label = 'Oldest persons '
                ui.print_result(result, label)
            elif option == "6":
                result = get_persons_closest_to_average(table)
                label = 'Closest to average age persons '
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
    title_list = ['id', 'name', 'birth date']
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
    data_to_add = ui.get_inputs(["Name", "Birth year"], "Please provide information")
    data_to_add.insert(0, id_)
    table.append(data_to_add)
    data_manager.write_table_to_file("hr/persons.csv", table)

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

    data_manager.write_table_to_file('hr/persons.csv', table)

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
            new_list = ui.get_inputs(['name', 'birth date'], "Please provide your information")
            lists[1] = new_list[0]
            lists[2] = new_list[1]

    data_manager.write_table_to_file("hr/persons.csv", table)

    return table


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):
    oldest_persons = []
    id_, name, year = min(table, key=lambda item: int(item[2]))
    for i in range(len(table)):
        if table[i][2] == str(year):
            oldest_persons.append(table[i][1])

    return oldest_persons



# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):
    years_from_table = []
    for i in range(len(table)):
        years_from_table.append(int(table[i][2]))

    sum_of_years = 0
    for i in range(len(years_from_table)):
        sum_of_years += int(years_from_table[i])

    average = (sum_of_years/len(table))

    first_step = abs(years_from_table[0]-average)
    for i in range(len(years_from_table)):
        minimum = abs(years_from_table[i] - average)
        if minimum <= first_step:
            first_step = minimum
            year = years_from_table[i]
    name_closest_to_average = []
    for i in range(len(table)):
        if table[i][2] == str(year):
            name_closest_to_average.append(table[i][1])

    return name_closest_to_average



def main():
    pass


if __name__ == '__main__':
    main()

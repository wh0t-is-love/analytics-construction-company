import sys
from my_requests import object_profit, number_of_tools, \
      richest_customer, technic_life, unsold_apartments, \
      sold_apartments, construction_stage, select_all_from_table


def parser(name_request: str):
    if name_request.lower() == 'object_profit':
        return object_profit
    elif name_request.lower() == 'number_of_tools':
        return number_of_tools
    elif name_request.lower() == 'richest_customer':
        return richest_customer
    elif name_request.lower() == 'technic_life':
        return technic_life
    elif name_request.lower() == 'unsold_apartments':
        return unsold_apartments
    elif name_request.lower() == 'sold_apartments':
        return sold_apartments
    elif name_request.lower() == 'construction_stage':
        return construction_stage
    elif name_request.lower() == 'select':
        return select_all_from_table
    raise ValueError("There is no request with name {}".format(name_request))


if __name__ == "__main__":
    argv = sys.argv
    if argv[1] == '-h' or argv[1] == '--help' or argv[1] == 'h':
        print("Options:\n\
    -h or --help or h - manual\n\
    object_profit - profit from objects\n\
    number_of_tools (optional: object name) - necessary tools for"
        " construction\n\
    richest_customer (optional: int or none) - customers,"
        " who pay more than other (top n)\n\
    technic_life - how much time to changing technic\n\
    unsold_apartments - unsolved apartments info\n\
    sold_apartments - sold apartments info\n\
    construction_stage (optional: object name) - construction stage\n\
    select (name of table) - select all info from this table\n\
    \n\
    if second flag is csv -> output will be saved in file output.csv\n\
    _________________________________________________________________\n")
    else:
        i = 1
        if argv[1] == 'csv':
            i += 1
        func = parser(argv[i])
        if len(argv) > i + 1:
            result = func(argv[i + 1])
        else:
            result = func()
        if argv[1] == 'csv':
            result.to_csv('output.csv')
        else:
            print(result)

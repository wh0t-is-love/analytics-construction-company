import sys
from my_requests import object_profit, number_of_tools, \
      richest_customer, technic_life, unsold_apartments, \
        sold_apartments, construction_stage
from utils import select_all_from_table


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
        print("")
    else:
        print(argv)
        func = parser(argv[1])
        if len(argv) > 2:
            tmp = func(argv[2])
        else:
            tmp = func()
        for x in tmp:
            print(x)

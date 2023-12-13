import sys
from my_requests import object_profit, number_of_tools, \
      richest_customer, technic_life, unsold_apartments, \
        sold_apartments, construction_stage


def parser(name_request):
    if name_request == 'object_profit':
        return object_profit
    elif name_request == 'number_of_tools':
        return number_of_tools
    elif name_request == 'richest_customer':
        return richest_customer
    elif name_request == 'technic_life':
        return technic_life
    elif name_request == 'unsold_apartments':
        return unsold_apartments
    elif name_request == 'sold_apartments':
        return sold_apartments
    elif name_request == 'construction_stage':
        return construction_stage
    raise ValueError("There is no request with name {}".format(name_request))


if __name__ == "__main__":
    argv = sys.argv
    func = parser(argv[1])
    if len(argv) > 2:
        tmp = func(argv[2:])
    else:
        tmp = func()
    for x in tmp:
        print(x)

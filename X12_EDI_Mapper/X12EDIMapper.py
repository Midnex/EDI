#! /usr/bin/python3

get_type = input('EDI File type: ')

if get_type == '940':
    from X12940 import parser
elif get_type == '943':
    from X12943 import parser
else:
    print(f"{get_type} not supported yet or invalid.")
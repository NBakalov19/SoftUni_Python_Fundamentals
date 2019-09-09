distance = float(input())
input_unit = input()
output_unit = input()

result = None

if input_unit == 'm':
    if output_unit == 'mm':
        result = distance * 1000
    elif output_unit == 'cm':
        result = distance * 100
    elif output_unit == 'mi':
        result = distance * 0.000621371192
    elif output_unit == 'in':
        result = distance * 39.3700787
    elif output_unit == 'km':
        result = distance * 0.001
    elif output_unit == 'ft':
        result = distance * 3.2808399
    elif output_unit == 'yd':
        result = distance * 1.0936133
# TODO

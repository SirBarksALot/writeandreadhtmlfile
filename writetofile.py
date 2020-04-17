from html5print import HTMLBeautifier

# test
WORKING_PATH = '/home/filiplez18/writeandreadhtmlfile/'


def operation_on_file(*args):
    file_path = WORKING_PATH + args[0]
    if len(args) > 1:
        operation = 'w+'
    else:
        operation = 'r'

    with open(file_path, operation) as operation_place:
        if len(args) > 1:
            operation_place.write(args[1])
        else:
            return HTMLBeautifier.beautify(''.join(operation_place.readlines()))


strin = operation_on_file('toread.html')
operation_on_file('towrite.html', strin)

#  *args allows a function to accept any number of arguments :-
''' The asterisk * tells Python to collect the extra positional arguments into one tuple.

Important: args is just a conventional name. The asterisk is what matters. You could write *numbers instead. '''

def add(*number):
    total =0

    for i in number:
        total += i

    return total

print(add(20,5,5,10))
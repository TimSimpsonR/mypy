# This is defined as returning an integer elsewhere.
def function_a():
    return 5

# Argument 'a' is defined as str elsewhere and "go" returns an integer.
def do_something(a):
    print(a)

# Error: Argument 1 to "do_something" has incompatible type "int"
do_something(function_a())

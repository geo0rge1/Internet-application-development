def print_result(func):
    def decorated_func(*args):
        print(func.__name__)
        return_value = func(*args)
        if isinstance(return_value, list):
            for value in return_value:
                print(str(value))
        elif isinstance(return_value, dict):
            for key in return_value.keys():
                print(str(key) + ' = ' + str(return_value[key]))
        else:
            print(return_value)
        return return_value
    return decorated_func

def test_print_result():
    @print_result
    def test_1():
        return 5


    @print_result
    def test_2():
        return 'Hello World!'


    @print_result
    def test_3():
        return {'a': 3, 'b': 10}


    @print_result
    def test_4():
        return [1, 2]

    print('Task 5:\n')
    test_1()
    test_2()
    test_3()
    test_4()

def main():
    test_print_result()

if __name__ == "__main__":
    main()

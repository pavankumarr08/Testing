def do_test(num=0):
    try:
        if num:
            return int(num) + 5
        else:
            return "please enter a number"
    except ValueError as err:
        return err
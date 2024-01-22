#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    final_list = []
    for k in range(list_length):
        try:
            final = my_list_1[k] / my_list_2[k]
        except TypeError:
            print("wrong type")
            final = 0
        except ZeroDivisionError:
            print("division by 0")
            final = 0
        except IndexError:
            print("out of range")
            final = 0
        finally:
            final_list.append(final)
    return (final_list)

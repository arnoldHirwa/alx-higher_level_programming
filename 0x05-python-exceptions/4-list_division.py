#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    array = []
    for i in range(list_length):
        result = 0
        try:
            result = my_list_1[i] / my_list_2[i]
        except ValueError:
            print("wrong type")
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            array.append(result)
    return array

#Bright Djogatse
#!/usr/bin/python3


def commacode(my_list):
    """
    function that takes a list as an argument
    and returns a string
    """
    if len(my_list) == 0:
        return ""
    elif len(my_list) == 1:
        my_list[0]
    else:
        last = "and " + my_list[-1]
        final_list = ", " .join(my_list[:1]
        return f"{final_list} ,{last}"

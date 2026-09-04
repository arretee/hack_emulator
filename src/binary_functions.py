from src.hack_config import MAX_POSITIVE_VALUE



def convert_bin_to_dec(binary_list: list) -> int:
    """
        Function converts binary list to decimal value of hack CPU.
        Uses 2s completion on bit 16

        :param binary_list: list by size of 16 with 0 or 1 values that represents bits

        :return: integer value
    
    """

    dec = 0
    for val in binary_list[1:]:
        dec = dec * 2 + val

    if binary_list[0]:
        dec = dec - MAX_POSITIVE_VALUE - 1

    return dec


def convert_dec_to_bin(decimal: int) -> list:
    """
        Function converts decimal to binary list.
        Uses 2s completion on bit 16

        :param decimal: value to convert into a bin list.
        
        :return: list by size of 16 with 0 or 1 values that represents bits


    """
    bin_list = [0 for _ in range(16)]

    if decimal < 0:
        bin_list[0] = 1
        decimal = MAX_POSITIVE_VALUE + (-decimal)

        for i in range(15):
            bin_list[15 - i] = int(not(decimal % 2))
            decimal = decimal // 2

    else: 
        for i in range(15):
            bin_list[15 - i] = decimal % 2
            decimal = decimal // 2



    return bin_list


def Not16(binary_list: list) -> list:
    """
        Function converts binary list to a not binary list.
        
        :param binary_list: list by size of 16 with 0 or 1 values that represents bits
    
        :return: list by size of 16 with 0 or 1 values that represents bits of negative input list.
        
    """
    not_list = [0 for i in range(16)]

    for i, bit in enumerate(binary_list):
        not_list[i] = int(not(bit))

    return not_list


def Add16(x: list, y: list) -> list:
    """
        Function add 2 binary lists by adding each bit. x + y 

        :param x: list by size of 16 with 0 or 1 values that represents bits
        :param y: list by size of 16 with 0 or 1 values that represents bits
    
        :return: list by size of 16 with 0 or 1 values that represents new value.
    """

    add_list = [0 for i in range(16)]
    carry = 0

    for i in range(15, -1, -1):
        add_list[i] = (x[i] + y[i] + carry) % 2
        carry =  (x[i] + y[i] + carry) // 2 

    return add_list


def And16(x: list, y: list) -> list:
    """
        Function And between 2 binary lists. x and y 

        :param x: list by size of 16 with 0 or 1 values that represents bits
        :param y: list by size of 16 with 0 or 1 values that represents bits
    
        :return: list by size of 16 with 0 or 1 values that represents new value.
    """

    and_list = [0 for i in range(16)]

    for i in range(16):
        and_list[i] = int(x[i] and y[i])


    return and_list


def Or16(x: list, y: list) -> list:
    """
        Function And between 2 binary lists. x and y 

        :param x: list by size of 16 with 0 or 1 values that represents bits
        :param y: list by size of 16 with 0 or 1 values that represents bits
    
        :return: list by size of 16 with 0 or 1 values that represents new value.
    """

    or_list = [0 for i in range(16)]

    for i in range(16):
        or_list[i] = int(x[i] or y[i])


    return or_list




def karatsuba( x, y):

    if( x < 10 or y < 10 ):
        return x * y


    x_str = str(x)
    y_str = str(y)

    str_max_length = max( len(x_str), len(y_str) )

    middle_index = str_max_length//2

    x_high, x_low = int(x_str[ : -middle_index]), int(x_str[ -middle_index : ] )
    y_high, y_low = int(y_str[ : -middle_index]), int(y_str[ -middle_index : ] )

    # low part = x_low * y_low
    z_0 = karatsuba( x_low, y_low )

    # middle part = x_low + x_high * y_low + y_high - high part - low part * ( 10^middle_index )
    z_1 = karatsuba( x_low + x_high, y_low + y_high )

    # high part = x_high * y_high
    z_2 = karatsuba( x_high, y_high )

    # value of multipliation =  x * y
    multiplication_value = z_2 * 10 ** (2*middle_index) + (z_1 - z_2 - z_0) * 10 ** (middle_index) + z_0

    return multiplication_value



def test_bench():
    num1 = 12
    num2 = 16

    result = karatsuba( num1, num2)

    print( str(num1) + " * " + str(num2) + " = \n" + str(result) )



def main():

    # small size test bench
    # test_bench()


    num1 = int( input("\nPlease input a value for number1\n") )
    num2 = int( input("\nPlease input a value for number2\n") )

    result = karatsuba( num1, num2)

    print( str(num1) + " * " + str(num2) + " = \n" + str(result) )

    return






if __name__ == '__main__':
    main()
    
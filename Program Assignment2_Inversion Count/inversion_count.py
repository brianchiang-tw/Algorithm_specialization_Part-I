import random
import sys
import os



def mergesort_with_inv_count( input_series):

    # get the length of input series
    length = len(input_series)

    # create a list, named output serise, of the same length with input series, default value is None
    output_series = [None] * length
    return _mergesort(input_series, output_series, 0, length-1 )

    
def _mergesort(input_series, output_series, left, right):
    # print("_entry of _mergesort")
    # print("left : " + str(left) + " ,right : " + str(right) )
    # print("input_series" + str(input_series) )
    # print("output_series" + str(output_series) )

    # counter for inversion
    inversion_count = 0

    # tmp
    tmp = None

    # boundary check
    if( right > left ):

        # update mid point
        mid = ( left + right ) // 2

        # print("\n\n divide left half")
        # print("left : " + str(left) + " ,mid : " + str(mid) )

        tmp, inv_count = _mergesort( input_series, output_series, left, mid)
        inversion_count += inv_count

        #print("divide right half")
        #print("mid+1 : " + str(mid+1) + " ,right : " + str(right) )

        tmp, inv_count = _mergesort( input_series, output_series, mid+1, right)
        inversion_count += inv_count

        #print("merge")
        #print("left : " + str(left) + " ,mid+1 : " + str(mid+1), " , right : " + str(right) )
        inv_count = _merge(input_series, output_series, left, mid+1, right)
        inversion_count += inv_count
        #print("output series: ", str(output_series) )

    return output_series, inversion_count



def _merge(input_series, output_series, left, mid, right):
    #print("merge")

    left_sentry = left
    right_sentry = mid 
    output_sentry = left

    # counter for inversion
    inversion_count = 0

    while( left_sentry <= (mid-1) and right_sentry <= right):

        # pick smaller element from eihter left half or right half
        if( input_series[left_sentry] <= input_series[right_sentry] ):
            output_series[output_sentry] = input_series[left_sentry]

            # update index
            left_sentry += 1
            output_sentry += 1
        else:
            output_series[output_sentry] = input_series[right_sentry]

            # update index
            right_sentry += 1
            output_sentry += 1

            # if right half's leading element is smaller than left half's, 
            # it means there is (mid - left_sentry) inversions in current iteration
            inversion_count += ( mid - left_sentry )

    # right half is empty, then put all elements of left half to output series in order
    while( left_sentry <= mid-1 ):
        output_series[output_sentry] = input_series[left_sentry]
        left_sentry += 1
        output_sentry += 1
    

    # left half is empty, then put all elements of right half to output series in order
    while( right_sentry <= right ):
        output_series[output_sentry] = input_series[right_sentry]
        right_sentry += 1
        output_sentry += 1
    


    # update input series in each merge call
    for i in range(left, right+1, 1) :
        input_series[i] = output_series[i]

    return inversion_count


def test_bench():

    series = list( [4,3,2,1] )

    print("\nCall function mergesort_with_inv_count()\n")
    result, inversion_count = mergesort_with_inv_count( series )

    print("inversion count:")
    print( inversion_count )

    # expected output
    '''
    6

    Hint:
    total iversions:
    (4,3)
    (4,2)
    (4,1)
    (3,2)
    (3,1)
    (2,1)
    '''

    return 

def main():

    # small size test bench
    # test_bench()

    series = list()

    current_working_dir = os.getcwd()
    print( current_working_dir )

    file_handle = open(".\Program Assignment2_Inversion Count\Week2_IntegerArray.txt")

    str_oneline = file_handle.readline()

    while str_oneline:

        # add one new element from input text file to integer list: series
        series.append( int(str_oneline) )

        # read next line until End-of-file
        str_oneline = file_handle.readline()

    file_handle.close()

    print("\n length of series : " +  str( len(series) ) )

    #print("series before sorting : ")
    #print( series )

    print("\nCall function mergesort_with_inv_count()\n")
    result, inversion_count = mergesort_with_inv_count( series )


    #print("series after sorting : ")
    #print( result ) 

    print("inversion count:")
    print( inversion_count )

    return



if __name__ == '__main__':
    
    main()
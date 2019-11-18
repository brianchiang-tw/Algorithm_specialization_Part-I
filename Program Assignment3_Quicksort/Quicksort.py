
import os
import sys
import statistics
import copy

def swap(array, x, y):
    temp = array[x]
    array[x] = array[y]
    array[y] = temp
    return



def partition( array, left, right, mode="First"):

    if "Last" == mode:

        # swap array[left], array[right]
        # Use last element as pivot
        swap( array, left, right)


    elif "Median_of_three" == mode:
        
        middle_index = ( right + left )//2

        # three: left most element, right most element, middle element
        three = [ array[left], array[middle_index], array[right] ]
       

        median_of_three = statistics.median( three )

        # print("median: ", median_of_three)

        if array[left] == median_of_three:

            # just the same, no need to swap
            # array[left], array[left] = array[left], array[left]
            pass

        elif array[middle_index] == median_of_three:
            # swap array[middle_index], array[left]
            # array[middle_index], array[left] = array[left], array[middle_index]
            swap( array, left, middle_index)

        else:
            # swap array[right], array[left]
            # array[right], array[left] = array[left], array[right]
            swap( array, left, right)


    elif "First" == mode:

        # default pivot is first element, no need to swap
        pass


    else:
        print("Wrong mode option")
        raise (Exception,"Wrong mode option")
        

    # pick pivot element as first element in array
    pivot = array[left]

    # index of elements smaller than pivot
    i = left+1

    for j in range (left+1, right+1):

        if array[j] < pivot:
            # because element j is smaller than pivot
            # swap element j and element i
            array[i], array[j] = array[j], array[i]

            # update index i
            i += 1

    # after checking and smaller element rearrangement
    # swap pivot and array[i-1]
    array[left], array[i-1] = array[i-1], array[left]

    # i-1 is partition index
    # this index split array into 3 part
    # left part, pivot, right part
    return (i-1)



def quicksort(array, left, right, mode="First"):

    if left < right :

        # divide it into left part, pivot, right part


        # conquer pivot
        partition_index = partition( array, left, right, mode)

        # conquer left part
        left_comparison_count = quicksort(array, left, partition_index-1, mode)

        # conquer right part
        right_comparison_count = quicksort(array, partition_index+1, right, mode)

        # update comparison count
        total_comparison_count = left_comparison_count + right_comparison_count + (right-left)

        return (total_comparison_count)

    else:
        total_comparison_count = 0
        return (total_comparison_count)
    


def test_bench():

    # test case:
    array = [5,4,1,3,2]
    print("before sorting")
    print( array )
 
    comprison_count = quicksort(array, 0 , len(array)-1, "First" )
    print( "\ncomparison_count with first element as pivot: ")
    print( comprison_count )

    print("\nafter sorting")
    print( array )
 
    #expected output:
    '''
    before sorting
    [5, 4, 1, 3, 2]

    comparison_count with first element as pivot:
    8

    after sorting
    [1, 2, 3, 4, 5]
    '''



def main():

    current_work_dir = os.getcwd()
    print( current_work_dir )

    filename = current_work_dir + "\Quicksort\QuickSort.txt"

    # other test txt file are offered to help tracing and debugging
    # filename = current_work_dir + "\Quicksort\\test1.txt"

    # create an array to collect integer from input text file
    array = list()

    # open input file
    file_handle = open(filename)

    str_buffer = file_handle.readline()
    while str_buffer :

        number = int(str_buffer)

        # add integer into arrahy
        array.append( number )

        # read next line
        str_buffer = file_handle.readline()

    # close input file
    file_handle.close()

    # backup input (unsorted) array
    backup = copy.deepcopy(array)


    
    # Because python default recursion depth is 1000
    # this could cuase error in run-time as following
    # RecursionError: maximum recursion depth exceeded in comparison

    # Thus, weset one million as recursion depth
    sys.setrecursionlimit( 10000000 )

    # '''
    comprison_count = quicksort(array, 0 , len(array)-1, "First" )
    print( "comparison_count with first element as pivot: ")
    print( comprison_count )
    # '''


    # '''
    array = copy.deepcopy(backup)
    comprison_count = quicksort(array, 0 , len(array)-1, "Last" )
    print( "comparison_count with last element as pivot: ")
    print( comprison_count )
    # '''
    

    array = copy.deepcopy(backup)
    comprison_count = quicksort(array, 0 , len(array)-1, "Median_of_three" )
    print( "comparison_count with Median_of_three as pivot: ")
    print( comprison_count )

    return



if __name__ == '__main__':

    #test_bench()
    main()
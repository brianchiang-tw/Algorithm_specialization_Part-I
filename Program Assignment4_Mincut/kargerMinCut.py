import sys
import os
import math
import random
from datetime import datetime
import copy



def edge_contraction( adj_list_dict, vertex_u, vertex_v):

    # contract edge(u, v)
    # keep vertex u, and update u's adjacency list from appending vertex v's
    adj_list_dict[ vertex_u] = adj_list_dict[ vertex_u ] + adj_list_dict[ vertex_v ]

    # remove v's adjacency list from global adjacency list
    adj_list_dict.pop( vertex_v )

    # update each edge(x, v) redircting to edge(x, u)
    for i in adj_list_dict:
        for j in range( len(adj_list_dict[i] ) ):

            if adj_list_dict[i][j] == vertex_v:
                adj_list_dict[i][j] = vertex_u


    # eliminate all self-loop edges during current edge contraction
    adj_list_dict[ vertex_u ] = list( filter(lambda vertex: vertex != vertex_u, adj_list_dict[vertex_u] ) )

    # return updated adjacency list dictionary
    return adj_list_dict



def karger_min_cut( graph_with_adj_list_dict ):

    

    if len(graph_with_adj_list_dict) == 2:
        # Base case and stop condition
        
        list_of_all_edge = list( graph_with_adj_list_dict.values() )
        # the remaining count of edge is min cut
        return len( list_of_all_edge[0] )

    else:
        # Inductive step:
        # Keep conducting karger algorithm until only 2 verteices remain.


        # list of all vertex (key value of "graph_with_adj_list_dict" )
        list_of_all_vertex_in_graph = list( graph_with_adj_list_dict.keys() )

        # randomly choose one edge with two end points, vertex_u and vertex v
        # vertex u
        vertex_u = random.choice( list_of_all_vertex_in_graph )
        

        # vertex v
        vertex_v = random.choice( graph_with_adj_list_dict[vertex_u] )

        # conduct edge contraction on edge E = (u, v)
        # update graph with adjacency list dictionary
        #graph_with_adj_list_dict = edge_contraction( graph_with_adj_list_dict, vertex_u, vertex_v)

        # keep ruuning karger algorithm until graph has two vertices only
        min_cut = karger_min_cut( edge_contraction( graph_with_adj_list_dict, vertex_u, vertex_v) )

        # the remaining count of edge is min cut
        return min_cut







def main():

    current_work_directory = os.getcwd()
    filename = current_work_directory + "\Program Assignment4_Mincut\kargerMinCut.txt"

    with open( filename) as file_handle:

        # graph is a dictionay, on the basis of adjacency list
        # key : vertex i
        # value : those verteices connected to vertex i
        graph = {}

        for one_line in file_handle:

            # each line in input text file is well separated by tab, i.e., the "\t"
            one_adjacency_list = list(    map(int, one_line.strip().split("\t") )   )

            # get vertex index as dictionay's key
            vertex_i = one_adjacency_list.pop(0)
            # print("vertex i : ", vertex_i )

            # get adjacency list, excluding the first one value(key), as dictionary's value
            graph[vertex_i] = one_adjacency_list

        
        # get size of graph ( the number of vertex)
        size_of_graph = len(graph)

        v_square = size_of_graph ** 2

        # min_cut initialization with |V|^2
        min_cut = v_square

        # upper_bound initialization with |V|^2 * log |V|
        upper_bound = int( v_square*math.log(size_of_graph) )

        for i in range( upper_bound ):

            

            new_graph = copy.deepcopy( graph )

            current_min_cut = karger_min_cut( new_graph )
            
            
            '''
            print( "\n iteration counter: ", i)
            print( "current min cut: ", current_min_cut )
            print( "minimal min cut so far", min_cut )
            '''

            if( current_min_cut < min_cut ):
                min_cut = current_min_cut
                print("min cut updated in this iteration: ", min_cut)

        print("\n final min cut value:", min_cut)
    return



if __name__ == "__main__":
    main()

import numpy as np
import random

def randomNum(smallest, largest):
    num = random.randint(smallest,largest)
    int_num = num
    return int_num
    
def getArray(size,large_rela,small_rela):
    array = np.zeros([size,size],dtype=np.uint64)
    for x in range(size):
        for y in range(size):
            randomVal = randomNum(small_rela,large_rela)
            array[x][y] = randomVal
            array[y][x] = randomVal
            array[x][x] = largest_const
            #Stop the loop since all value is assigned, 
            #this break condition is included to allow formation of a symetrical matrix
            if x == size-1 or y == size-1:
                break
    return array

#Get Valid Input from user
getInput = True

while getInput:
    print("Please enter number of person, person is represented in number, the number of person should be more than or equal to 3: ")
    arr_size = input()
    
    if arr_size.isnumeric():
        if int(arr_size) < 3:
            print("Please enter 3 or more person.\n")
        else:
            getInput = False
    else:
        print("Please enter a positive integer only.\n")
        
getInput = True
while getInput:
    print("Please enter largest relationship value: ")
    rel_largest = input()
    
    if rel_largest.isnumeric():
        if int(rel_largest) < 3:
            print("Largest relationship value must be more than or equal to 3.\n")
        else:
            getInput = False
    else:
        print("Please enter a positive integer only.\n")

getInput = True
while getInput:    
    print("Please enter smallest relationship value: ")
    rel_smallest = input()
    
    if rel_smallest.isnumeric():
        if int(rel_smallest) > int(rel_largest):
            print("Smallest relationship value must higher than largest relationship value.\n")
            
        elif int(rel_smallest)-int(rel_largest) == 0:
            print("Smallest relationship value must have difference between largest relationship value.\n")
            
        else:
            getInput = False
    else:
        print("Please enter a positive integer only.\n")
    
largest_const = int(rel_largest) + 100


#Generating Random Array with random values
relation_table_init = getArray(int(arr_size),int(rel_largest),int(rel_smallest))
z = 0
allCost = []
all_solution = []

# Nearest Neighbor Algorithm
while z < len(relation_table_init):
    
    relation_table_original = relation_table_init.copy()
    
    relation_table = relation_table_init.copy()
    
    #initial node 
    initial_state = z
    
    current_state = initial_state
    visited = []
    solution = []
    x = 0
    count = 1
    found_goal = False
    
    while not found_goal:
        shortest_to_next = min(relation_table[current_state])
        
        #Delete the current_state from the table left only those unvisited
        temp = relation_table[current_state].tolist()
        
        #Add current state to visited state. (Will eventually become solution at the end)
        solution.append([current_state,shortest_to_next])
        
        #Get Coordinates of matrix
        current_state_temp = current_state
        current_state = temp.index(shortest_to_next)
        
        #Display each column slowly replace with largest number
        #print(relation_table)
        x += 1
        count += 1
        # print("Visited:")
        # print(solution)
        # print("Current:")
        # print(current_state)
        
        if x < len(relation_table):
            # "Remove" visited by making the column largest number
            relation_table[:,current_state_temp] = largest_const
            if count == int(arr_size):
                all_solution.append(solution)
                count = 0
                print("COunt = " + str(count))
            continue
        else:
            found_goal = True
            z += 1
            # Get the last node coordinate
            last_node = solution[len(relation_table)-1][0]
            # Change the cost of the last node to the cost return initial node to get final solution.
            solution[len(relation_table)-1][1] = relation_table_original[initial_state][last_node]
            # print(relation_table_original[initial_state])
            # Display last node back to initial node cost
            # print(relation_table_original[last_node][initial_state])
            
            #Reset values with orignal values
            print("Solution for starting point: " + str(initial_state))
            print(solution)
            totalCost = 0
            for path in solution:
                totalCost += path[1]
            allCost.append(totalCost)
            print("Total Cost (Initial State: " + str(initial_state) + " )= "+ str(int(totalCost)) +" ")
            print("====================\n")


optimalPath = min(allCost)
print("\n")
print("Final Optimal Path Cost:" + str(int(optimalPath)))



    


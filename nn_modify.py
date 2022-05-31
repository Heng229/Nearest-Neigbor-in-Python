import numpy as np
import random
import math

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

def getDifference(arr):
    #Is the array size even or odd
    even = True if int(arr_size) % 2 == 0 else False
    count = 0
    left = 0
    right = 0
    
    #Even and odd list size have different formula for calculating Z value.
    if even:
        half = int(arr_size)/2
        while count <= int(arr_size):
            if count == 0: 
                count += int(half)
                for x in range (count):
                    # print(arr[x][1])
                    left += arr[x][1]
            else:
                for x in range (count,int(arr_size)):
                    # print(arr[x][1])
                    right += arr[x][1]
                count += int(half)
    else:
        half = math.ceil(int(arr_size)/2)
        while count <= int(arr_size):
            if count == 0: 
                count += int(half)
                for x in range (count):
                    # print("Left")
                    # print(arr[x][1])
                    left += arr[x][1]
            else:
                for x in range (count-1,int(arr_size)):
                    # print("Right")
                    # print(arr[x][1])
                    right += arr[x][1]
                count += int(half)
    
    z = abs(left-right)
    print("~~~~~~")
    print("Z Value Calculation")
    print("~~~~~~")
    print("Initial State : " + str(arr[0][0]))
    print("Left : " + str(left))
    print("Right: " + str(right))
    print("Z: " + str(z))
    print("~~~~~~\n")
    return z

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
    
#Largest value for removing from comparison
largest_const = int(rel_largest) + 100

#Generating Random Array(list) with random values
relation_table_init = getArray(int(arr_size),int(rel_largest),int(rel_smallest))
z = 0
allCost = []
all_solution_and_cost = []

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
    found_solution = False
    
    while not found_solution:
        shortest_to_next = min(relation_table[current_state])
        
        #Delete the current_state from the table left only those unvisited
        temp = relation_table[current_state].tolist()
        
        #Add current state to visited state. (Will eventually become solution at the end)
        solution.append([current_state,shortest_to_next])
        
        #Get Coordinates of matrix
        current_state_temp = current_state
        current_state = temp.index(shortest_to_next)
        
        x += 1
        
        if x < len(relation_table):
            # "Remove" visited by making the column largest number
            relation_table[:,current_state_temp] = largest_const
            continue
        else:
            print("Solution " + str(z+1))
            print("`````````")
            found_solution = True
            z += 1
            # Get the last node coordinate
            last_node = solution[len(relation_table)-1][0]
            # Change the cost of the last node to the cost return initial node to get final solution.
            solution[len(relation_table)-1][1] = relation_table_original[initial_state][last_node]
            
            #Reset values with orignal values
            print("Solution for starting point: " + str(initial_state))
            print(solution)
            totalCost = 0
            for path in solution:
                totalCost += path[1]
            print("Total Cost (Initial State: " + str(initial_state) + " )= "+ str(int(totalCost)) +" ")
            print(".............\n")
            
            #All solution and their total cost in a list.
            all_solution_and_cost.append([solution,totalCost])
            allCost.append(totalCost)

#Z value (Difference between left and right)
#Get index of all solution with same lowest cost
indices_lowest_cost = [i for i, x in enumerate(allCost) if x == min(allCost)]
#Get Z value for each equal lowest cost solution
z_value = []
for x in indices_lowest_cost:
    z_value.append([getDifference(all_solution_and_cost[x][0]),x])

#Choose lowest Z value solution with min()
final_chosen_solution_index = z_value.index(min(z_value))
final_chosen_solution = all_solution_and_cost[z_value[final_chosen_solution_index][1]]


#Final Solution details output
string_solution = ""
print("Final Optimal Solution Chosen")
print("==================")
print("Solution : ")
for x in range(len(final_chosen_solution[0])):
    if x < len(final_chosen_solution[0]):
        string_solution += "Person " + str(final_chosen_solution[0][x][0]) + "\t(Optimal Cost to next person :" + str(final_chosen_solution[0][x][1]) + "\t) ->\n"
    if x+1 == len(final_chosen_solution[0]):
        string_solution += "Person " + str(final_chosen_solution[0][0][0]) + "\t(Back to starting person.)"
print(string_solution)
print("Cost : ")
print(final_chosen_solution[1])
print("Z Value : ")
print(int(min(z_value)[0]))
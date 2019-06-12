#you wanted a funny comment so here u go, 5 extra credit points pls and thank u
import itertools
# file input
with open('input4.txt') as line:
  inputs = [line.split() for line in line]

# declaration of relevant variables 
values = list(map(int, inputs[1]))
weights = list(map(int, inputs[2]))
n = len(values)
weightCapacity = int(inputs[0][0])

# adding an array of all 0s in index 0 to be able to access other memo indexes without having to subtract 1
#0s are also added as a first index from second array on in order to have a fitting base case
memo = [[0]*(weightCapacity + 1)] + [[0] + [-1 for i in range(weightCapacity + 1)] for j in range(n + 1)]

# functions

def knapsackSolution(n,weightCapacity):
  # if answer table does not have a value, then add a value to it
  if memo[n][weightCapacity] == -1:
    
    # if there is no enough space to put n weight in knapsack, move on
    if weightCapacity < weights[n - 1]:
      result = knapsackSolution(n - 1,weightCapacity)
    else:
      # check to see if adding the current element to the list is viable by using max 
      option1 = knapsackSolution(n - 1,weightCapacity)  
      option2 = values[n - 1] + knapsackSolution(n - 1,weightCapacity - weights[n - 1])  
      result = max(option1, option2)
      memo[n][weightCapacity] = result
  else: 
    result = memo[n][weightCapacity]
  return result

def main():
  print(knapsackSolution(n,weightCapacity)) 

main()
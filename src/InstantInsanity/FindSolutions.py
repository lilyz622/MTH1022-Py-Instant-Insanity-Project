'''
Created on Mar 10, 2017

@author: yzhan265
'''
if __name__ == '__main__':
    pass

class Cube(object):
    def __init__(self,front,back,up,down,left,right):
        self.pairs = ((front,back),(up,down),(left,right))

cubes =[]

cubes.append(Cube('B','R','G','G','R','G'))
cubes.append(Cube('G','R','R','B','B','B'))
cubes.append(Cube('B','R','G','R','R','R'))
cubes.append(Cube('W','W','R','R','W','W'))

def get_hash(color):
    hash_colors = {'R':1,'W':2,'G':3,'B':5}
    return hash_colors[color]
    

def print_cubes(cubes):
    j=1
    for i in cubes:
        print(j,":",[(c1,c2) for c1,c2 in i.pairs])
        j+=1

print_cubes(cubes)
valid_subgraphs=[]
# all_subgraphs = []

def find_valid_subgraphs(cubes, num_cubes_remaining, vertices_degrees, current_pairs):
    if num_cubes_remaining == 0:
#         all_subgraphs.append((current_pairs[:], vertices_degrees))
        if vertices_degrees == (1*2*3*5)**2:
            valid_subgraphs.append(current_pairs[:])
        vertices_degrees = 1
        return
    else:
        pass
    counter = 0
    for pair in cubes[num_cubes_remaining-1].pairs:
        vertices_degrees *= get_hash(pair[0])*get_hash(pair[1])
        current_pairs[num_cubes_remaining-1] = counter
        find_valid_subgraphs(cubes, (num_cubes_remaining-1),vertices_degrees, current_pairs)
        vertices_degrees /= get_hash(pair[0])*get_hash(pair[1])
        counter += 1

current_pairs = [0,0,0,0]
find_valid_subgraphs(cubes, 4, 1, current_pairs)
# print (all_subgraphs)
# print (len(all_subgraphs))
print ('number of valid subgraphs:',len(valid_subgraphs))

def find_solutions(subgraphs):
    solutions = []
    i = 0
    while (i<len(subgraphs)):
        j=i+1
        while (j<len(subgraphs)):
            found_solution = True
            index = 0
            # compare corresponding index values in both subgraphs
            while (index<len(subgraphs[i])):
                s1 = subgraphs[i][index]
                s2 = subgraphs[j][index]
                # if index values point to the same pair on a given cube,
                # the subgraph combination is invalid
                if s1 == s2:
                    found_solution = False
                index +=1
            if found_solution:
                solutions.append((subgraphs[i],subgraphs[j]))
            j+=1
        i+=1
    return solutions
solutions = find_solutions(valid_subgraphs)
print(solutions)
print(len(solutions))
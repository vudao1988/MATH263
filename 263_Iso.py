from itertools import permutations 
from copy import deepcopy

#this method is used to transform matrix to swap a pair vertices
def swap_matrix(M,a,b):
    #matrix size always must be nxn
    size = len(M)
    #swap column a <-> column b
    for i in range(size):
        temp = M[i][a]
        M[i][a] = M[i][b]
        M[i][b] = temp
    #swap row a <-> row b
    for j in range(size):
        temp = M[a][j]
        M[a][j] = M[b][j]
        M[b][j] = temp

#this method is used to swap vertices postition in working(base) case 
def swap(L,a,b):
    temp = L[a]
    L[a] = L[b]
    L[b] = temp

#this method is used to check if 2 matrices are identical
def cmp_matrix(A,B):
    size = len(A)
    for i in range(size):
        for j in range(size):
            if(A[i][j]!=B[i][j]):
                return False
    return True

#this method is used to check Isomorphic with 2 input vars : A = AdjM(A) and B = AdjM(B)
def Iso(A,B):
    print("A = ",A)
    print("B = ",B)
    size = len(A)
    #l : list of all possible vertices swaping cases.
    #ex : size = 3 , V = {0,1,2} , l = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
    l = list(permutations(range(size)))
    #run loop to do exhausted check for all of possibility
    for i in range(0,len(l)):
        #Copying matrix data & possible cases to new working instances
        mt = deepcopy(A)
        base_case = list(l[0])
        cmp_case = list(l[i])
        for m in range(size):
            #compare base_case and cmp_case
            #if vertices are diffrent, proceed swapping.
            if(base_case[m] != cmp_case[m]):
                n = m + 1
                while(n < size):
                    if(base_case[n] == cmp_case[m]):
                        break;
                    n = n+1
                #end while n
                swap_matrix(mt,m,n)
                swap(base_case,m,n)
            #end if(base_case[m] != cmp_case[m])
        #end for m
                
        if cmp_matrix(mt,B) == True:
            #result = True
            #matrix transform is the pattern it used to transform A -> B
            print("matrix transform : ",l[0]," -> ",l[i])
            print("Iso(A,B) = True")
            return True
    print("Iso(A,B) = False")
    return False

# TESTING AREA
A = [[1,0,0,1],
     [0,1,0,0],
     [1,1,1,0],
     [0,1,0,1]]
B = [[1,1,1,0],
     [0,1,0,0],
     [0,0,1,1],
     [0,1,0,1]]
Iso(A,B)
        
A= [[0,1,1],[0,0,1],[0,0,0]]
B= [[0,0,0],[1,0,0],[1,1,0]]
Iso(A,B)

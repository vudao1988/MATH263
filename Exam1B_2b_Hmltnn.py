import networkx as nx
import pydot
import itertools
import scipy as sp


def isSafe(self, v, pos, path): 
	# Check if current vertex and last vertex  
	# in path are adjacent 
    if self[ path[pos-1] ][v] <= 0: 
        return False
    
    self[ path[pos-1] ][v] = self[ path[pos-1] ][v] - 1
    self[v][ path[pos-1] ] = self[v][ path[pos-1] ] - 1
    
	# Check if current vertex not already in path
    for vertex in path: 
        if vertex == v:
            return False

    return True

# A recursive utility function to solve  
# hamiltonian cycle problem 
def hamCycleUtil(self, path, pos,V): 

	# base case: if all vertices are  
	# included in the path 
	if pos == V: 
		# Last vertex must be adjacent to the  
		# first vertex in path to make a cyle 
		if self[ path[pos-1] ][ path[0] ] >= 1: 
			return True
		else: 
			return False

	# Try different vertices as a next candidate  
	# in Hamiltonian Cycle. We don't try for 0 as  
	# we included 0 as starting point in in hamCycle() 
	for v in range(1,V): 

		if isSafe(self,v, pos, path) == True: 

			path[pos] = v
			#step[pos-1] = ()

			if hamCycleUtil(self, path, pos+1, V) == True: 
				return True

			# Remove current vertex if it doesn't  
			# lead to a solution 
			path[pos] = -1

	return False

def hamCycle(self, V,start): 
    path = [-1] * V 
    #step = [[-1,-1,-1]] * (V - 1)
    '''Let us put vertex 0 as the first vertex
        in the path. If there is a Hamiltonian Cycle,  
        then the path can be started from any point 
        of the cycle as the graph is undirected '''
    path[0] = 0

    if hamCycleUtil(self,path,1,V) == False: 
		#print ("Solution does not exist\n")
        return False

    print("\nFollowing is one Hamiltonian Cycle SbGrph")
    return True

if __name__ == "__main__":
    G = nx.MultiGraph()
    G.add_nodes_from([0,1,2])
    
    G.add_edge(0, 0, parallel_idx=0, label='000')
    G.add_edge(1, 1, parallel_idx=0, label='110')
    G.add_edge(2, 2, parallel_idx=0, label='220')
    G.add_edge(0, 1, parallel_idx=0, label='010')
    G.add_edge(0, 1, parallel_idx=1, label='011')
    G.add_edge(1, 2, parallel_idx=0, label='120')
    G.add_edge(1, 2, parallel_idx=1, label='121')
    G.add_edge(2, 0, parallel_idx=0, label='020')
    G.add_edge(2, 0, parallel_idx=1, label='021')
    edge_labels = dict([((u,v,), d['label']) for u, v, d in G.edges(data = True)])
    nx.draw_networkx_edge_labels(G,pos=nx.spring_layout(G),edge_labels=edge_labels)
    
    edg = G.edges.data('parallel_idx',default=0)
    i = 0
    for n in range(1,len(edg)):
        E = list(itertools.combinations(edg,n))
        print('===================')
        print('Groups from %d vertices'%(n))
        print('===================')
        for e in E:
            IsHam = False
            sg = G.edge_subgraph(e)
            A = nx.adjacency_matrix(sg)
            B = A.todense()
            C = [[]]
            lenth = 0
            if(len(B) == 1):
                C = [[B[0,0]]]
                lenth = B[0,0]
            elif(len(B) == 2):
                C = [ [ B[0,0],B[0,1] ], [ B[1,0],B[1,1] ]]
                lenth = B[0,0] + B[0,1] + B[1,1]
            elif(len(B) == 3):
                C = [ [ B[0,0],B[0,1],B[0,2] ],
                      [ B[1,0],B[1,1],B[1,2] ],
                      [ B[2,0],B[2,1],B[2,2] ]]
                lenth = B[0,0] + B[0,1] + B[0,2] + B[1,1] + B[1,2] + B[2,2]
                
            if( hamCycle(C,len(C),list(sg.nodes)[0]) == True):
                print('\t Vertices : ',list(sg.nodes))
                print('\t Edges : ',list(sg.edges))

                #save graph files
                #fn = 'ham_img\Ham_%d.dot'%i
                #nx.drawing.nx_pydot.write_dot(sg,fn)
                
                i = i + 1
            
    print('Total Hamitonian SbGraph = %d'%(i))

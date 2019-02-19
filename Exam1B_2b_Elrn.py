import networkx as nx
import pydot
import itertools

if __name__ == "__main__":
    G = nx.MultiGraph()
    G.add_nodes_from([0,1,2])
    
    G.add_edge(0, 0, parallel_idx=0, label='000' )
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
            sg = G.edge_subgraph(e)
            if(nx.is_eulerian(sg)):
                print(list(e))
                print('\t Vertices : ',list(sg.nodes))
                print('\t Edges : ',list(sg.edges))
                print('\t ElrnCycle : ',list(nx.eulerian_circuit(sg)))
                
                #save graph files
                #fn = 'img\Elrn_%d.dot'%i
                #nx.drawing.nx_pydot.write_dot(sg,fn)

                i = i + 1
   
    print('Total Eulerian SbGraph = %d'%(i))

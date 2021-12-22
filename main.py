from mtree import *
import mtree
from math import sqrt
import pandas as pd
import numpy as np

def cast(cad):
    temp = ""
    for i in cad:
        if(i == ','):
            temp += '.'
        else:
            temp += i
    return float(temp)
    

class point(object):
    def __init__(self,ID,a,b,c,d,e,f,g,h,i,j,k):
        self.ID = ID
        if(a=="negative"):
            self.a = 0
        else:
            self.a = 1

        self.b = b
        self.c = c            
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h
        self.i = i
        self.j = j
        self.k = k

def distance_manhat(p1,p2):   
    result=0
    result = result + abs(p1.a-p2.a)
    result = result + abs(p1.b-p2.b)
    result = result + abs(p1.c-p2.c)
    result = result + abs(p1.d-p2.d)
    result = result + abs(p1.e-p2.e)
    result = result + abs(p1.f-p2.f)
    result = result + abs(p1.g-p2.g)
    result = result + abs(p1.h-p2.h)
    result = result + abs(p1.i-p2.i)
    result = result + abs(p1.j-p2.j)
    result = result + abs(p1.k-p2.k)
    return result
    

def node_objs(node,k):
    if isinstance(node, mtree.InternalNode):
        result = []
        for n in node.entries:
            print("     "*k,"[ radio:",n.radius,"]")
            result.extend(node_objs(n.subtree,k+1))
        return result
    else:
        for i in node.entries:
            print("     "*k,"[",i.obj.ID,"]")
        return list(map(lambda e: e.obj, node.entries))

def tree_objs(tree):
    return node_objs(tree.root,0)

def main():

    mtree = MTree(distance_manhat , max_node_size = 12)

    dataset = pd.read_csv('Pandas.csv')
    Pacient_ID = dataset.iloc[:, [0]].values
    SARS = dataset.iloc[:, [1]].values
    Age_quantile = dataset.iloc[:, [2]].values
    Hematocrit = dataset.iloc[:, [3]].values
    Platelets = dataset.iloc[:, [4]].values
    Platelet_volume = dataset.iloc[:, [5]].values
    MCHC = dataset.iloc[:, [6]].values
    Leukocytes = dataset.iloc[:, [7]].values
    Basophils = dataset.iloc[:, [8]].values
    Eosinophils = dataset.iloc[:, [9]].values
    Monocytes = dataset.iloc[:, [10]].values
    Proteina_C = dataset.iloc[:, [11]].values

    puntos = []
    for i in range(len(Pacient_ID)):
        for j in range(len(Pacient_ID[i])):

            ##Hematocritos c)
            _Hematocrit=1
            if(not pd.isnull(Hematocrit[i][j])):
                _Hematocrit = cast(Hematocrit[i][j]) 

            ##Platelets d)
            _Platelets=0
            if(not pd.isnull(Platelets[i][j])):
                _Platelets = cast(Platelets[i][j])

            ##Platelet_volume e)
            _Platelet_volume=0
            if(not pd.isnull(Platelet_volume[i][j])):
                _Platelet_volume = cast(Platelet_volume[i][j])    
                      
            ##MCHC f)
            _MCHC=0
            if(not pd.isnull(MCHC[i][j])):
                _MCHC = cast(MCHC[i][j])  

            ##Leukocytes g)
            _Leukocytes=0
            if(not pd.isnull(Leukocytes[i][j])):
               _Leukocytes = cast(Leukocytes[i][j])   

            ##Basophils h)
            _Basophils=0
            if(not pd.isnull(Basophils[i][j])):
               _Basophils = cast(Basophils[i][j])  

            ##Eosinophils i)
            _Eosinophils=0
            if(not pd.isnull(Eosinophils[i][j])):
                _Eosinophils = cast(Eosinophils[i][j])  

            ##_Monocytes j)
            _Monocytes=0
            if(not pd.isnull(Monocytes[i][j])):
                _Monocytes = cast(Monocytes[i][j])  
                 
            ##_Proteina_C k)
            _Proteina_C=0
            if(not pd.isnull(Proteina_C[i][j])):
                _Proteina_C = cast(Proteina_C[i][j])     
                
            puntos.append(point(Pacient_ID[i][j],SARS[i][j],float(Age_quantile[i][j]),_Hematocrit,_Platelets,_Platelet_volume,_MCHC,_Leukocytes,_Basophils,_Eosinophils,_Monocytes,_Proteina_C))
        

    for objects in puntos:
        mtree.add(objects)
    tree_objs(mtree)


    print("####################### RANGE QUERIES ###############################")
    radio = float(input("Ingrese el radio:\t"))
    new_point_paciente = point(Pacient_ID[i][j],SARS[i][j],float(Age_quantile[i][j]),_Hematocrit,_Platelets,_Platelet_volume,_MCHC,_Leukocytes,_Basophils,_Eosinophils,_Monocytes,_Proteina_C)
    querie = mtree.search_in_radius(new_point_paciente,radio)
    for obj in querie:
        print(obj)
    print(len(querie),'object found')
    
main()
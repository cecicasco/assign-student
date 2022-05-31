from pymoo.core.problem import ElementwiseProblem
import data
from constraint import validateConstraints
from geopy import distance
from random import randrange
from pymoo.core.repair import Repair
from objetivefunctions import f1,f2,f3

#Initialize
data.init()

class ADEEProblem(ElementwiseProblem):

    def __init__(self, **kwargs):
        super().__init__(n_var=data.PERSON_SIZE, n_obj=data.N_OBJ,
                         n_constr=data.N_CONSTR, xl=0, xu=data.CLASS_SIZE-1, type_var=int,**kwargs)

    def _evaluate(self, x, out, *args, **kwargs):
        e=[f1(x)*-1, f2(x), f3(x)*-1]
        print(e)
        out["F"] = e #For minimization context, with multiply *-1
        out["G"] = validateConstraints(x)

class AEEEFeacible(Repair):

    def _do(self, problem, pop, **kwargs):

        print("Start repair")

        # the packing plan for the whole population (each row one individual)
        Z = pop.get("X")

        # now repair each indvidiual zi
        for zi in range(len(Z)):
            # the packing plan for zi
            z = Z[zi]

            valid=validateConstraints(z)
            
            if valid[0]==0 and valid[1]==0:
                continue

            #All the class available are for the same grade
            class_assigments = [0] * data.CLASS_SIZE

            for j in range(len(z)):
                if z[j] :
                    class_index = z[j]
                    #if the student is assigned to a diferent grade
                    if data.P[j][3] != data.C[class_index][0] :
                        z[j] = -1
                        continue

                    class_assigments[class_index] = class_assigments[class_index] + 1
                    #if the maximum capacity was reached
                    if data.C[class_index][5] > class_assigments[class_index] :
                        z[j] = -1
                        continue

                #without assigment
                else:
                    z[j] = -1

            #searh over the students with not assignments
            for j in range(len(z)):
                if z[j]==-1:
                    i = randrange(len(class_assigments))
                    ocupation = class_assigments[i]
                    ##check the capacity
                    if data.C[i][5] > ocupation and data.P[j][3] == data.C[i][0]:
                        class_assigments[i] = class_assigments[i] + 1
                        z[j] = i





       # set the design variables for the population
        pop.set("X", Z)
        print("End repair")
        return pop

def generate_ind(name,q): 
    print("Start generate ind "+str(name))
    ind=[-1]*data.PERSON_SIZE

    # All the classes availables are for the same grade
    class_assigments = [0] * data.CLASS_SIZE


    for p in range(data.PERSON_SIZE):

        for c in range(len(class_assigments)):
            ##check the capacity
            if data.C[c][5] > class_assigments[c] and data.P[p][3] == data.C[c][0]:
                class_assigments[c] = class_assigments[c] + 1
                ind[p] = c
                break;

    print("Ind added by process: "+str(name))
    q.put(ind)
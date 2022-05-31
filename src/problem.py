from pymoo.core.problem import ElementwiseProblem
import datadb as data
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
                class_index = z[j]
                # if the student is assigned to a diferent grade
                if data.P[j][3] != data.C[class_index][0]:
                    z[j] = -1
                    continue

                # if the maximum capacity was reached
                if data.C[class_index][5] > class_assigments[class_index]:
                    z[j] = -1
                    continue

                class_assigments[class_index] = class_assigments[class_index] + 1


            classes=[]
            for i in range(len(class_assigments)):
                classes.append({"id":i, "ocupation":class_assigments[i]})

            print(len(classes))
            #searh over the students with not assignments
            for j in range(len(z)):
                if len(classes) == 0 :
                    break;

                if z[j]==-1:

                    i = randrange(len(classes))
                    single_class = classes[i]
                    ocupation = single_class['ocupation']
                    class_index = single_class['id']

                    classes.remove(single_class)

                    ##check the capacity
                    if data.C[class_index][5] > ocupation and data.P[j][3] == data.C[class_index][0]:
                        ocupation = ocupation + 1
                        z[j] = class_index
                        if data.C[class_index][5] > ocupation:
                            classes.append({"id": class_index, "ocupation": ocupation})

       # set the design variables for the population
        pop.set("X", Z)
        print("End repair")
        return pop

def generate_ind(name,q): 
    print("Start generate ind "+str(name))
    ind=[-1]*data.PERSON_SIZE

    # All the classes availables are for the same grade


    print("Ind added by process: "+str(name))
    q.put(ind)
import datadb as data

#Compute all restrictions
def validateConstraints(X):    
    valid_c1=0
    valid_c2 = 0
    valid_c3 = 0
    n_p=len(data.P)
    for j in range(n_p):
        c=1
        class_index = X[j]
        if (data.P[j][3] != data.C[class_index][0]):  # The class should be the same grade as the student requered
            valid_c1 = 1
            break
        if not X[j] : #All the students should be assign
            valid_c2 = 1
        for l in range(n_p):
          if(j!=l and X[j]==X[l]):
              c=c+1
              if(c>=10 and c<=40): #The number of assigments should be less  40 and more than 10
                  valid_c3=1
                  break


    return [valid_c1, valid_c2, valid_c3]

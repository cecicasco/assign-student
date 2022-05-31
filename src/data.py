def init():
    global C, P, E, CLASS_SIZE, PERSON_SIZE, ESTABLISMENT_SIZE, N_OBJ, N_CONSTR
    #Class
    C = [
        [1,1,1,1,1,3],
        [1,1,1,2,2,3],
        [1,2,1,3,3,3],
        [1,2,1,1,1,3],
        [1,2,1,2,2,3],
        [1,1,1,3,3,3]
    ]

    #Students
    P=[
        [1,3,4,1],
        [2,0,9,1],
        [3,4,3,1],
        [4,0,4,1],
        [5,2,6,1],
        [6,2,8,1],
        [7,9,1,1],
        [8,10,5,1],
        [9,1,10,1],
        [10,0,6,1],
        [11,3,3,1],
        [12,2,6,1],
        [13,3,4,1],
        [14,8,9,1],
        [15,7,3,1],
        [16,5,4,1]

    ]

    #Establishment
    E=[
        [1,1,5,8,1,15],
        [2,3,7,15,3,1],
        [3,9,2,9,11,62]
    ]

    # Configure size
    CLASS_SIZE = len(C)
    PERSON_SIZE = len(P)
    ESTABLISMENT_SIZE = len(E)
    print(CLASS_SIZE)
    print(PERSON_SIZE)
    print(ESTABLISMENT_SIZE)
    N_OBJ = 3
    N_CONSTR = 2
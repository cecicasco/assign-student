# data of Problem Assign Studen
import psycopg2


def init():
    global  C, P, E, CLASS_SIZE, PERSON_SIZE, ESTABLISMENT_SIZE, N_OBJ, N_CONSTR

    # Class
    conn = psycopg2.connect("host=192.168.0.121, dbname=postgres user=postgres password=postgres port=5432")
    cur = conn.cursor()

    C = []
    cur.execute("select * from tesis.vm_cursos ")
    for row in cur:
        C.append([row[0], row[1], row[2], row[3], row[4], row[5]])

    # Persons
    P = []
    cur.execute("select * from tesis.vm_personas order by 1")
    for row in cur:
        P.append([row[0], row[1], row[2], row[3]])

    # Establishment
    E = []
    cur.execute("select * from tesis.vm_establecimientos order by 1")
    for row in cur:
        E.append([row[0], row[1], row[2], row[3], row[4], row[5]])

    # Configure size
    CLASS_SIZE = len(C)
    PERSON_SIZE = len(P)
    ESTABLISMENT_SIZE = len(E)
    print(CLASS_SIZE)
    print(PERSON_SIZE)
    print(ESTABLISMENT_SIZE)
    N_OBJ = 3
    N_CONSTR = 2

    cur.close()
    conn.close()
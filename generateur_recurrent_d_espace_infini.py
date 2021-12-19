from find import find
import threading

dimension = []
mutex = threading.Lock()

def generateur_recurrent_d_espace(dimension0=[], dimension_units=[], coordonnee = "", dimension_length = 0):
    global dimension
    if isinstance(dimension0, list):
        if len(coordonnee)+1 < dimension_length:
            for i in dimension_units:
                mutex.acquire()
                dimension0.append([coordonnee+str(i)])
                mutex.release()
            for x in dimension0:
                y = threading.Thread(target=generateur_recurrent_d_espace, args=(x, dimension_units, x[0], dimension_length,))
                y.run()
        elif len(coordonnee)+1 == dimension_length:
            for i in dimension_units:
                mutex.acquire()
                dimension0.append([coordonnee+str(i)])
                mutex.release()

def generateur_recurrent_d_espace_infini():
    global dimension
    i = 0
    while True:
        dimension = []
        i = i +1
        x = threading.Thread(target=generateur_recurrent_d_espace, args=(dimension, range(0, i), "", i,))
        x.start()
        x.join()
        print(dimension)
generateur_recurrent_d_espace_infini()

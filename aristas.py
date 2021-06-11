G = {
     "a" : ['c'],
     "b" : ['c', 'e'],
     "c" : ['a','b','d','e'],
     "d" : ['c'],
     "e" : ['c', 'b'],
     "f" : []
}
def run():
    
    opcion = input(""" Elija una de las siguiente entradas
                       a
                       b
                       c
                       d
                       e
                       f
                        """)
    
    for llave in G:
        if llave == opcion:
            print(len(G[llave]))
            break

    
if __name__ == "__main__":
    while(True):
        run()
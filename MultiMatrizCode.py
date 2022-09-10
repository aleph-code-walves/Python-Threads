import threading as th 
import os 
import time

MatrizA = [[12,7,3],
           [4 ,5,6],
           [7 ,8,9]]

MatrizB = [[5,8,1,2],
          [6,7,3,0],
          [4,5,9,1]]

#matrix Zerarada
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

def thread_function(X, Y, result):
    tempo_ini = time.perf_counter()

    print(f'\nTask iniciou em {tempo_ini}')
    
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]

    print("Resultado de ordenação:\n")
    ImprimeMatriz(result)

    tempo_fim = time.perf_counter()
    print(f'\nTask finalizou em {tempo_fim}')
    print(f'Task durou {tempo_fim - tempo_ini}\n')


def ImprimeMatriz(M):
    for r in M:
        print(r)         

if __name__ == '__main__':

    task = th.Thread(target=thread_function, args=(MatrizA,MatrizB,result), name='thread_function')
    task.start()
    time.sleep(1)
    task.join()

    print("Nome da Thread rodando: {}".format(th.current_thread().name))
    print("ID da task do programa: {}".format(os.getpid()))
    print("Nome da Thread do programa: {}".format(task.name))
    print("ID thread_function:", task.ident)
   

    
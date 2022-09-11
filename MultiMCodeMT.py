import threading
import os 
import time

MatrizA = [[12,7,3],
           [4 ,5,6],
           [7 ,8,9]]

MatrizB = [[5,8,1,2],
          [6,7,3,0],
          [4,5,9,1]]

result = [[0, 0, 0], 
          [0, 0, 0], 
          [0, 0, 0]]


class task_Thread1(threading.Thread):
    def __init__(self, id, nome):
        threading.Thread.__init__(self)
        self.id = id
        self.name = nome

    def run(self):
        tempo_ini = time.perf_counter()
        print (self.name, f'Iniciou em {tempo_ini} segundos')
        

        vetor_3x1a = [MatrizA[0][0], MatrizA[1][0], MatrizA[2][0]]
        vetor_1x3b = [MatrizB[0][0], MatrizB[0][1], MatrizB[0][2]]

        result[0][0] += vetor_3x1a[0] * vetor_1x3b[0]
        result[0][1] += vetor_3x1a[0] * vetor_1x3b[1]
        result[0][2] += vetor_3x1a[0] * vetor_1x3b[2]

        result[1][0] += vetor_3x1a[1] * vetor_1x3b[0]
        result[1][1] += vetor_3x1a[1] * vetor_1x3b[1]
        result[1][2] += vetor_3x1a[1] * vetor_1x3b[2]

        result[2][0] += vetor_3x1a[2] * vetor_1x3b[0]
        result[2][1] += vetor_3x1a[2] * vetor_1x3b[1]
        result[2][2] += vetor_3x1a[2] * vetor_1x3b[2]

        tempo_fim = time.perf_counter()
        print(f'{self.name} finalizou em {tempo_fim} segundos, e durou:{tempo_fim - tempo_ini} segundos\n')


class task_Thread2(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        tempo_ini = time.perf_counter()
        print (self.name, f'Iniciou em {tempo_ini} segundos')

        vetor_3x1a = [MatrizA[0][1], MatrizA[1][1], MatrizA[2][1]]
        vetor_1x3b = [MatrizB[1][0], MatrizB[1][1], MatrizB[1][2]]

        result[0][0] += vetor_3x1a[0] * vetor_1x3b[0]
        result[0][1] += vetor_3x1a[0] * vetor_1x3b[1]
        result[0][2] += vetor_3x1a[0] * vetor_1x3b[2]

        result[1][0] += vetor_3x1a[1] * vetor_1x3b[0]
        result[1][1] += vetor_3x1a[1] * vetor_1x3b[1]
        result[1][2] += vetor_3x1a[1] * vetor_1x3b[2]

        result[2][0] += vetor_3x1a[2] * vetor_1x3b[0]
        result[2][1] += vetor_3x1a[2] * vetor_1x3b[1]
        result[2][2] += vetor_3x1a[2] * vetor_1x3b[2]

        tempo_fim = time.perf_counter()
        print(f'{self.name} finalizou em {tempo_fim} segundos, e durou:{tempo_fim - tempo_ini} segundos\n')


class task_Thread3(threading.Thread):
    def __init__(self, id, nome):
        threading.Thread.__init__(self)
        self.id = id
        self.name = nome

    def run(self):
        tempo_ini = time.perf_counter()
        print (self.name, f'Iniciou em {tempo_ini} segundos')

        vetor_3x1a = [MatrizA[0][2], MatrizA[1][2], MatrizA[2][2]]
        vetor_1x3b = [MatrizB[2][0], MatrizB[2][1], MatrizB[2][2]]

        result[0][0] += vetor_3x1a[0] * vetor_1x3b[0]
        result[0][1] += vetor_3x1a[0] * vetor_1x3b[1]
        result[0][2] += vetor_3x1a[0] * vetor_1x3b[2]

        result[1][0] += vetor_3x1a[1] * vetor_1x3b[0]
        result[1][1] += vetor_3x1a[1] * vetor_1x3b[1]
        result[1][2] += vetor_3x1a[1] * vetor_1x3b[2]

        result[2][0] += vetor_3x1a[2] * vetor_1x3b[0]
        result[2][1] += vetor_3x1a[2] * vetor_1x3b[1]
        result[2][2] += vetor_3x1a[2] * vetor_1x3b[2]

        tempo_fim = time.perf_counter()
        print(f'{self.name} finalizou em {tempo_fim} segundos, e durou:{tempo_fim - tempo_ini} segundos\n')

def ImprimeMatriz(M):
    for r in M:
        print(r)      

if __name__ == "__main__":

    tempo_ini = time.perf_counter()

    thread1 = task_Thread1(1, "Thread 1")
    thread2 = task_Thread2(2, "Thread 2")
    thread3 = task_Thread3(3, "Thread 3")

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

    tempo_fim = time.perf_counter()
    print("Tempo de Execução do programa", (tempo_fim - tempo_ini), 'em segundos')

    print("ID da task do programa: {}".format(os.getpid()), '\n')
    print("ID thread_function 1:", thread1.ident)
    print("ID thread_function 2:", thread2.ident)
    print("ID thread_function 3:", thread3.ident,'\n')

    print("Resultado da Multiplicação:")
    ImprimeMatriz(result)


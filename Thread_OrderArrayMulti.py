import threading as th
import time
import logging as log
import numpy as np
import os

tempo_ini = time.perf_counter()
a = [5,51,2,3,5]

def thread_function(array):
    size = len(array)
    
    time_task = time.process_time_ns()

    print("Array Inicial:", array)
    #res = np.sort(array, axis=None, kind='mergesort', order=None)

    for s in range(size):
        min_idx = s
        for i in range(s + 1, size):
             if array[i] < array[min_idx]:
               min_idx = i
 
        # Arranging min at the correct position
        (array[s], array[min_idx]) = (array[min_idx], array[s])

    
    print("Resultado de ordenação por mergesort:")
    print(f'Tempo de execução da task em Nanosegundos:{time_task}')
    print("ID da task: {}".format(os.getpid()), '\n')


def log_Config():
    formato_msg = "%(asctime)s: %(message)s"
    log.basicConfig(format=formato_msg, level=log.INFO, datefmt="%H:%M:%S")


if __name__ == '__main__':
    log_Config()

    print("Nome da Thread rodando: {}".format(th.current_thread().name),'\n')

    task = th.Thread(target=thread_function(a), args=(1,), name='Thread 1')
    task2 = th.Thread(target=thread_function(a), args=(1,), name='Thread 2')

    task.start()
    task2.start()

    task.join()
    task2.join()

    print("Threads ativas:", th.active_count())
    print("Lista de Threads:", th.enumerate())

    tempo_fim = time.perf_counter()
    tempo_exe = tempo_fim - tempo_ini

    #print(f'Thread Ordenação Finalizou, Thread ID: {th.get_native_id()}')
    print(f'tempo de Execução do programa em segundos: {tempo_exe:0.5f}')


#log.info(f'Thread Ordenação Iniciada, Thread ID:{th.get_native_id()}')

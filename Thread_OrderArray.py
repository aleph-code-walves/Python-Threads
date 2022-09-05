#Single Thread Algoritmo de Ordenação
import threading as th
import time
import logging as log
import numpy as np

tempo_ini = time.perf_counter()
a = [5,51,2,3,5]

def thread_function(array):
    time_task = time.process_time_ns()
    print("Array Inicial:", array)
    res = np.sort(array, axis=None, kind='mergesort', order=None)
    print("Resultado de ordenação por mergesort:", res)
    print(f'Tempo de execução da task em Nanosegundos:{time_task}')


def log_Config():
    formato_msg = "%(asctime)s: %(message)s"
    log.basicConfig(format=formato_msg, level=log.INFO, datefmt="%H:%M:%S")


if __name__ == '__main__':
    log_Config()
    task = th.Thread(target=thread_function(a), args=(1,))
    log.info(f'Thread Ordenação Iniciada, Thread ID:{th.get_native_id()}')
    print("Threads ativas:", th.active_count())
    print("Lista de Threads:", th.enumerate())
    task.start()

    tempo_fim = time.perf_counter()
    tempo_exe = tempo_fim - tempo_ini


    log.info(f'Thread Ordenação Finalizou, Thread ID: {th.get_native_id()}')
    print(f'tempo de Execução do programa em segundos: {tempo_exe:0.5f}')

import threading as th
import time
import os


# a = [5,51,2,3,5,18,25,63,84,12,798,4554,78,42,5475,96,214,53,47]
a = [245,480,350,230,405,400,405,160,205,320,260,505,310,330,45,20,150,355,275,500,550,400,350,440,300,515,450,505,365,470,545,75,30,70,140,35,475,350,20,360,200,300,340,255,480,235,140,300,170,90,420,225,215,425,260,5,250,515,75,165,505,35,375,135,315,500,245,250,475,315,525,520,50,215,455,185,475,390,20,120,170,325,180,400,130,345,280,55,65,525,400,440,390,325,475,330,395,40,160,210,240,175,20,245,90,30,245,30,370,100,390,515,175,365,330,425,345,450,460,410,30,180,75,75,455,200,225,380,420,245,285,520,265,145,285,310,230,375,510,260,365,245,505,550,385,115,15,420,550,115,240,305,170,80,60,240,270,295,20,355,60,185,195,500,10,150,230,485,140,315,80,235,150,535,210,125,260,110,275,95,25,365,255,385,320,470,445,260,90,530,100,280,465,510,50,550,130,435,15,180,425]


def thread_function(array):
    size = len(array)
    tempo_ini = time.perf_counter()

    print(f'\nTask iniciou em {tempo_ini}')
    print("Array Inicial:", array)

    for s in range(size):
        min_idx = s
        for i in range(s + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i

        (array[s], array[min_idx]) = (array[min_idx], array[s])

    print("Resultado de ordenação:", array)
    tempo_fim = time.perf_counter()
    print(f'Task finalizou em {tempo_fim}')
    print(f'Task durou {tempo_fim - tempo_ini}\n')


def dividir_Array(array):
    div = len(array)//2
    return array[:div], array[div:]


if __name__ == '__main__':
    b, c = dividir_Array(a)

    print("Nome da Thread rodando: {}".format(th.current_thread().name), '\n')

    task = th.Thread(target=thread_function(b), args=(1,), name='Thread 1')
    task2 = th.Thread(target=thread_function(c), args=(1,), name='Thread 2')

    task.start()
    task2.start()

    task.join()
    task2.join()

    final = b + c
    task3 = th.Thread(target=thread_function(
        final), args=(1,), name='Thread 3')
    task3.start()
    task3.join()

    print("ID da task do programa: {}".format(os.getpid()), '\n')
    print("ID task 1", task.ident)
    print("ID task 2", task2.ident)
    print("ID task 3", task3.ident)

    tempo_fim = time.perf_counter()
    # tempo_exe = tempo_fim - tempo_ini

    #print(f'Thread Ordenação Finalizou, Thread ID: {th.get_native_id()}')
    # print(f'tempo de Execução do programa em segundos: {tempo_exe:0.5f}')


#log.info(f'Thread Ordenação Iniciada, Thread ID:{th.get_native_id()}')

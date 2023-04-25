from queue import PriorityQueue

def h(a, b):
    # Heurística de distância de Manhattan
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

def astar(m, start, goal):
    # Define as pontuações iniciais de g e f para cada célula
    g_score = {cell: float('inf') for cell in m.grid}
    g_score[start] = 0
    f_score = {cell: float('inf') for cell in m.grid}
    f_score[start] = h(start, goal)

    # Inicializa a fila de prioridade com o valor f da célula de início
    open = PriorityQueue()
    open.put((f_score[start], start))
    came_from = {}

    # Executa o loop enquanto houver células na fila de prioridade
    while not open.empty():
        # Obtém a célula com menor valor f da fila de prioridade
        currCell = open.get()[1]

        # Verifica se o objetivo foi alcançado
        if currCell == goal:
            break

        # Percorre as células vizinhas e as adiciona à fila de prioridade se necessário
        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                if d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                if d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                if d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])

                # Calcula as pontuações g e f para a célula atualizada
                temp_g_score = g_score[currCell] + 1
                temp_f_score = temp_g_score + h(childCell, goal)

                # Adiciona a célula à fila de prioridade se sua pontuação f for menor do que a anterior
                if temp_f_score < f_score[childCell]:
                    g_score[childCell] = temp_g_score
                    f_score[childCell] = temp_f_score
                    open.put((temp_f_score, childCell))
                    came_from[childCell] = currCell

    # Cria o caminho a partir do dicionário came_from
    path = []
    cell = goal
    while cell != start:
        path.append(cell)
        cell = came_from[cell]
    path.append(start)
    path.reverse()

    # Retorna o caminho encontrado
    return path

def StarAlgoritmo(m, RANDOM_X_COMECO, RANDOM_Y_COMECO, RANDOM_X_FIM, RANDOM_Y_FIM):
    # Define a posição de início e o objetivo

    start = (RANDOM_X_COMECO, RANDOM_Y_COMECO)
    goal = (RANDOM_X_FIM, RANDOM_Y_FIM)

    print('Posicao Inicial:', RANDOM_X_COMECO, 'x', RANDOM_Y_COMECO)
    print('Posicao Final:', RANDOM_X_FIM, 'x', RANDOM_Y_FIM)

    # Executa o algoritmo A* para encontrar o caminho
    path = astar(m, start, goal)

    # Retorna o caminho encontrado
    return path
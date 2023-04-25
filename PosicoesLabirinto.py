from StarAlgoritmo import StarAlgoritmo

def PosicoesLabirinto(m, RANDOM_X_COMECO, RANDOM_Y_COMECO, RANDOM_X_FIM, RANDOM_Y_FIM):
   
    # Define a posição de início e o objetivo
    start = (RANDOM_X_COMECO, RANDOM_Y_COMECO)
    goal = (RANDOM_X_FIM, RANDOM_Y_FIM)

    print('Posicao Inicial:', RANDOM_X_COMECO, 'x', RANDOM_Y_COMECO)
    print('Posicao Final:', RANDOM_X_FIM, 'x', RANDOM_Y_FIM)

    # Executa o algoritmo A* para encontrar o caminho
    path = StarAlgoritmo(m, start, goal)

    # Retorna o caminho encontrado
    return path





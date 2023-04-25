from GerarLabirinto import GerarLabirinto

if __name__ == '__main__':
    # Obtém as dimensões do labirinto a partir do usuário e cria o objeto maze correspondente
    LARGURA_LABIRINTO = int(input("Digite a largura do labirinto: "))
    ALTURA_LABIRINTO = int(input("Digite a altura do labirinto: "))

    GerarLabirinto(LARGURA_LABIRINTO, ALTURA_LABIRINTO)
# Bibliotecas

from abc import ABC, abstractmethod # Para criação de classes abstratas
import random


class Tabuleiro():

    def __init__(self) -> None:

        '''
        Inicializa um tabuleiro 3x3 como uma lista de listas vazias.
        Cada casa começa vazia como uma string vazia('')
        '''

        self.casas = []  # Atributo da classe

        for lista in range(3):
            linha = []
            for casa in range(3):
                linha.append('')  # Adiciona uma string vazia para cada casa
            self.casas.append(linha)  # Adiciona a linha no tabuleiro

    def pegar_tabuleiro(self) -> list[list[str]]:

        '''
        Retorna o tabuleiro atual como uma lista de listas.
        Return: Lista de listas de str representando o tabuleiro.
        '''
        return self.casas

    def marcar_casa(self, pos: tuple[int, int], simbolo: str) -> bool:

        '''
        Marca uma casa no tabuleiro com o símbolo do jogador.

        Args: pos (tuple[int, int]): A posição (linha, coluna) da casa a ser marcada.
              simbolo (str): O símbolo do jogador que está fazendo a jogada.

        Returns: bool: Retorna True se a casa foi marcada com sucesso;
                       Retorna False se a casa já estiver ocupada.
        '''

        # Verifica se a casa na posição especificada está vazia
        if self.casas[pos[0]][pos[1]] == '':
            # Marca a casa com o símbolo do jogador
            self.casas[pos[0]][pos[1]] = simbolo
            return True  # Retorna True para indicar que a jogada foi bem-sucedida

        else:
            return False  # Retorna False se a casa já estiver ocupada

    def imprimir_tabuleiro(self) -> None:

        """
        Mostra o tabuleiro visualmente.

        O tabuleiro tem separadores entre casas e linhas.
        Cada casa pode estar com algum simbolo de algum jogador ou estar vazia.
        """

        print('-' * 13)  # Separador superior
        for i, linha in enumerate(self.casas):
            for casa in linha:
                print(f'| {casa if casa else ' ' } ', end='')  # Exibe espaço vazio se a casa estiver vazia
            print('|')  # Finaliza a linha do tabuleiro
            print('-' * 13)  # Separador entre as linhas


class Jogador(ABC):

    def __init__(self, nome: str, simbolo:str) -> None:

        '''
        Inicializa um objeto Jogador com um nome e um símbolo.

        Args: nome: O nome do jogador.
              simbolo: O símbolo que representa o jogador (ex: 'X' ou 'O').
        '''

        self.nome = nome
        self.simbolo = simbolo

    @abstractmethod # Define a próxima função como abstrata
    def fazer_jogada(self, tabuleiro: Tabuleiro) -> tuple[int,  int]:

        '''
        Método abstrato que deve ser implementado por subclasses
        para definir como o jogador vai fazer uma jogada.

        Args:
            tabuleiro: O objeto da classe Tabuleiro onde a jogada vai acontecer.

        Returns: Tuple[int, int]: A posição escolhida pelo jogador, representada
                como uma tupla (linha, coluna).
        '''

        pass


class JogadorHumano(Jogador):

    def fazer_jogada(self, tabuleiro: Tabuleiro) -> tuple[int, int]:

        '''
        Solicita a um jogador humano que insira uma linha e uma coluna onde ele deseja jogar.

        Args: tabuleiro (Tabuleiro): O objeto Tabuleiro onde a jogada vai acontecer.

        Returns: tuple[int, int]: As coordenadas (linha, coluna) da jogada que vai ser feita.
        '''

        # Solicita ao jogador a linha para a jogada
        linha = int(input('Em qual linha você quer jogar? (1, 2 ou 3): '))

        # Solicita ao jogador a coluna para a jogada
        coluna = int(input('Em qual coluna você quer jogar? (1, 2 ou 3): '))

        # Retorna as coordenadas da jogada
        return tabuleiro.marcar_casa((linha - 1, coluna - 1), self.simbolo)  # Retorna as coordenadas na forma(linha, coluna)   

lista = [1, 2, 3]
class JogadorMaquina(Jogador):

    def __init__(self, nome: str, simbolo: str, estrategia: str = 'aleatória') -> None:

        '''
        Inicializa um jogador do tipo máquina com uma estratégia.

        Args: nome (str): O nome do jogador.
              simbolo (str): O símbolo que representa o jogador (ex: 'X' ou 'O').
              estrategia (str): A estratégia da máquina. Por padrão ela é aleatória. 
                              Atualmente, a única estratégia implementada é a "aleatória".
        '''

        super().__init__(nome, simbolo)  # Inicializa a classe pai Jogador

        self.estrategia = estrategia.strip().lower()  # Limpa e corrige a string para minúsculas

        # Verifica se a estratégia é válida. Nesse pacote, só teremos a estratégia "aleatorio"
        if estrategia != 'aleatória':
            print(('Essa estratégia não está definida.' +
                   ' Atualmente a única estratégia definida é a "Aleatória".'))

    def fazer_jogada(self, tabuleiro: Tabuleiro) -> tuple[int, int]:

        '''
        Realiza a jogada de um jogador do tipo máquina usando a estratégia 'aleatória'.

        Args: tabuleiro (Tabuleiro): O objeto Tabuleiro onde a jogada vai acontecer.

        Returns: tuple[int, int]: A posição (linha, coluna) onde a jogada vai ser feita.

        A função vai buscar por todas as casas vazias no tabuleiro, se a estratégia for 'aleatória',
        escolhe uma posição vazia aleatoriamente. Depois marca a casa com o símbolo do jogador e se todas
        as casas estuverem ocupadas, mostra uma mensagem e não faz a jogada.
        '''

        casas_vazias = []  # Lista para armazenar as posições das casas vazias

        # Verifica se a estratégia do jogador é 'aleatória'
        if self.estrategia == 'aleatória':

            # "Corre" pelas linhas e colunas do tabuleiro para encontrar as casas vazias
            for i, linha in enumerate(tabuleiro.casas):
                for j, casa in enumerate(linha):

                    if casa == '':  # Se a casa estiver vazia, adiciona à lista
                        casas_vazias.append((i, j))

         # Verifica se ainda tem casas disponíveis para jogar
        if len(casas_vazias) == 0:
            return print('Todas as casas estão ocupadas. Não há mais jogadas possíveis.')

        else:
            # Escolhe uma casa aleatoriamente da lista de casas vazias e marca no tabuleiro
            return tabuleiro.marcar_casa(random.choice(casas_vazias), self.simbolo)


class JogoVelha():

    def __init__(self, jogador1: Jogador, jogador2: Jogador) -> None:

        '''
        Inicializa uma nova partida de Jogo da Velha.

        Args: jogador1 (Jogador): O primeiro jogador da partida.
              jogador2 (Jogador): O segundo jogador da partida.
        '''

        self.jogadores = [jogador1, jogador2]    # Cria uma lista com os jogadores.
        self.tabuleiro = Tabuleiro()    # Inicializa um tabuleiro.
        self.turno = random.choice([0, 1])    # Define o turno inicial sendo 0 ou 1 para garantir a 
                          # aleatoriedade da jogada inicial.

    def jogador_atual(self, turno: int) -> Jogador:

        '''
        Retorna o jogador atual com base no turno.

        Args: turno (int): O número do turno atual.

        Returns: Jogador: O jogador correspondente ao turno (alternando entre jogador 1 e 2).
        '''

        return self.jogadores[turno%2]

    def checar_fim_de_jogo(self) -> str | None:

        '''
        Verifica se o jogo terminou com a vitória de algum jogador.

        Esta função verifica as condições de vitória:
        Diagonal principal
        Diagonal secundária
        Linhas
        Colunas

        Se houver uma condição de vitória, imprime uma mensagem de vitória e diz em qual caso se enquadra.
        Se não houver vitória, retorna None.

        Returns: str | None: Mensagem de vitória se um jogador vencer, ou None se ninguém vencer.
        '''

        # Verifica a diagonal principal
        if self.tabuleiro.casas[0][0] != '' and self.tabuleiro.casas[0][0] == self.tabuleiro.casas[1][1] == self.tabuleiro.casas[2][2]:
            return f'Vitória! O jogador preencheu a diagonal principal!'

        # Verifica a diagonal secundária
        if self.tabuleiro.casas[0][2] != '' and self.tabuleiro.casas[0][2] == self.tabuleiro.casas[1][1] == self.tabuleiro.casas[2][0]:
            return f'Vitória! O jogador preencheu a diagonal secundária!'

        # Verifica as linhas
        for linha in range(0, 3):
            if self.tabuleiro.casas[linha][0] != '' and self.tabuleiro.casas[linha][0] == self.tabuleiro.casas[linha][1] == self.tabuleiro.casas[linha][2]:
                return f'Vitória! O jogador preencheu a linha {linha+1}!'

        # Verifica as colunas
        for i in range(0, 3):
            if self.tabuleiro.casas[0][i] != '' and self.tabuleiro.casas[0][i] == self.tabuleiro.casas[1][i] == self.tabuleiro.casas[2][i]:
                return f'Vitória! O jogador preencheu a coluna {i + 1}!'

        # Retorna None se não houver condição de vitória atendida.
        else:
            return None

    def jogar(self) -> None:

        '''
        Controla o fluxo do jogo da velha, alternando os turnos entre os jogadores, realizando as jogadas
        e verificando se há um vencedor ou empate. O jogo termina quando há uma vitória ou quando todas 
        as casas estão preenchidas.

        Args: Nenhum argumento é passado, mas o método acessa os atributos do objeto JogoVelha, como os 
              jogadores, o tabuleiro e o turno.

        Returns: None: A função não retorna valor, apenas controla o fluxo do jogo e imprime os
                       resultados no console.
        '''

        print(f'{self.jogadores[self.turno].nome} começa!')

        while True:
            # Obtém o jogador atual baseado no turno
            jogador_atual = self.jogador_atual(self.turno)

            # Imprime quem irá jogar
            print(f'É a sua vez, {jogador_atual.nome}.')

            # Jogador realiza a jogada no tabuleiro
            jogada = jogador_atual.fazer_jogada(self.tabuleiro)

            # Exibe o tabuleiro após a jogada
            self.tabuleiro.imprimir_tabuleiro()
            print('')

            # Verifica se há um vencedor
            resultado = self.checar_fim_de_jogo()

            if resultado is not None:
                # Se houver um vencedor, exibe a mensagem e finaliza o jogo
                print(f'{jogador_atual.nome} venceu! {resultado}')
                print('Fim do jogo')
                break

            # Verifica se o tabuleiro está cheio, indicando um empate
            elif not any('' in linha for linha in self.tabuleiro.casas):
                print('O jogo acabou. Não há mais casas para serem preenchidas.')
                print('Empate!')
                break

            # Caso contrário, continua o jogo e alterna o turno
            print(f'{jogador_atual.nome} jogou!')
            print('')
            self.turno += 1
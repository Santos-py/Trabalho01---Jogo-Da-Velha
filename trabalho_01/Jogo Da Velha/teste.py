from jogovelha.jogo_da_velha import JogadorHumano, JogadorMaquina, JogoVelha, Jogador, Tabuleiro

# Cria os jogadores Sapo e Perereca, um Jogador Maquina e o outro JogadorHumano
# e aqui já trabalhamos e mostramos a validade da classe Jogador.

jogador1 = JogadorMaquina('Sapo', 'X')
jogador2 = JogadorHumano('Perereca', 'O')

# Criamos um JogoVelha, já instanciando um tabuleiro, e trabalhamos com todos
# os métodos de ambas as classes, tabuleiro e JogoVelha.

jogo = JogoVelha(jogador1, jogador2)
jogo.jogar()

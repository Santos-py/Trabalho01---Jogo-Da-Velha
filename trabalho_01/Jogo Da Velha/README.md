# Jogo da Velha

Este é um projeto simples de Jogo da Velha implementado em Python com POO. O jogo permite que um jogador humano jogue contra um jogador computadorizado que utiliza uma estratégia aleatória para jogar, jogos entre dois jogadores humanos ou jogos com jogadores computadorizados.

# Índice

### Descrição
### Funcionalidades
### Como Jogar
### Estrutura do Código
### Relações
### Contribuições
### Licença
### Contatos

# Descrição

O Jogo da Velha é um jogo de tabuleiro para dois jogadores, onde cada jogador alterna sua vez de jogar para marcar uma casa em um tabuleiro 3x3. O primeiro jogador que maracr três símbolos iguais na horizontal, na vertical ou na diagonal, vence o jogo.

# Estrutura do Jogo

 O jogo pode ser jogado por um humano contra uma máquina, entre humanos ou entre máquinas.

 A máquina utiliza uma estratégia aleatória para selecionar suas jogadas.

 O jogo continua até que tenha um vencedor ou um empate, sem casas vazias no tabuleiro.

# Funcionalidades
- Tabuleiro: Representação do tabuleiro de 3x3.
- Jogador Humano: Permite que um jogador humano faça suas jogadas.
- Jogador Máquina: Implementa uma estratégia aleatória para as jogadas da máquina.
- Checagem de Vitória: Verifica se um jogador ganhou ou se o jogo terminou em empate.
- Interface Simples: O jogo é jogado no console com uma interface interativa.

## Como Jogar
1. Copie o repositório ou faça o download do código.
2. Abra um terminal e navegue até a pasta do projeto.
3. Execute o código Python com comando:
   python nome_do_arquivo.py
4. Siga as instruções no prompt para jogar:

 - O jogador humano deve dizer a linha e a coluna onde deseja jogar (de 1 a 3).

 - A máquina vai fazer sua jogada automaticamente.

 - O jogo termina quando um jogador vence ou quando não houver mais nenhuma casa vazia.

# Estrutura do Código
O código é dividido em várias classes que representam as principais funcionalidades do jogo:

- Tabuleiro: Gerencia o estado do tabuleiro e as jogadas.
-  Jogador (Classe Abstrata): Define a interface para os jogadores.
- JogadorHumano: Implementa a lógica para um jogador humano.
- JogadorMaquina: Implementa a lógica para um jogador computadorizado usando uma estratégia aleatória.
- JogoVelha: Controla o fluxo do jogo e alterna os turnos entre os jogadores.

# Relações
Entre as classes que compoõem a biblioteca temos as seguintes relações:

- JogoVelha compõe "Tabuleiro". O tabuleiro é uma parte fundamental do jogo.
- JogoVelha agrega Jogadores. Os jogadores são independentes do jogo, mas são necessários para a sua execução.
- JogadorHumano e JogadorMaquina herdam de Jogador. Herança simples

# Contribuições
Contribuições são sempre necessárias! Fique à vontade para enviar um e-mail para eventuais melhorias ou possíveis correções/simplificações.

# Licença
Este projeto é licenciado sob a Licença MIT. Consulte o arquivo LICENSE para obter mais informações.

# Contatos
Se você tiver dúvidas, sugestões ou feedback sobre o projeto, sinta-se à vontade para entrar em contato!

- Nome: Cauã Santos
- E-mail: caual8634@gmail.com

Agradeço o seu interesse e o seu feedback!
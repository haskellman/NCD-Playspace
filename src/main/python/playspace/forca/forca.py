import pygame
import random
#import pyAlphabetIndicators

letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
          'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
          'U', 'V', 'X', 'W', 'Y', 'Z']

# Cores
green = "#bcd246"
yellow = "#f4ad42"
red = "#c73d52"
grey = "#787c7e"
outline = "#d3d6da"
blue = "#4b8fbd"
blue2 = "#77c6ff"
blue3 = "#144970"
cor_acerto = green
cor_erro = red

class Indicadores:
    def __init__(self, posicao_inicial, espacamento, cor_inicial):
        global letras
        self.letras = letras  # Lista de letras (pode ser o alfabeto)
        self.posicao_inicial = posicao_inicial  # Posição inicial (x, y) na tela
        self.espacamento = espacamento  # Espaçamento entre as letras
        self.cor_inicial = cor_inicial  # Cor inicial das letras

        self.indicadores = []  # Lista de indicadores de letras (letra, cor)
        self.fonte = pygame.font.Font(None, 24)

        # Inicializa os indicadores com as letras e a cor inicial
        for letra in self.letras:
            self.indicadores.append((letra, self.cor_inicial))

    def atualizar(self, chute, palavra):
        global cor_acerto
        global cor_erro
        for i, (letra, cor) in enumerate(self.indicadores):
            if letra == chute:
                # Verifica se o chute é correto e muda a cor
                if chute in palavra:
                    self.indicadores[i] = (letra, cor_acerto)
                else:
                    self.indicadores[i] = (letra, cor_erro)

    def desenhar(self, tela):
        x, y = self.posicao_inicial

        for letra, cor in self.indicadores:
            letra_surface = self.fonte.render(letra, True, cor)
            letra_rect = letra_surface.get_rect()
            letra_rect.topleft = (x, y)
            tela.blit(letra_surface, letra_rect)
            x += self.espacamento


# Inicializando o pygame e criando a janela
pygame.init()
# Tela na proporcao 16:9
TELA_LARGURA = 480
TELA_ALTURA = 854
tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
pygame.display.set_caption("Jogo da Forca")

#Carregando o spritesheet
spritesheet = pygame.image.load("forca/imagens/cid.png")
#Separando o spritesheet
allframes = []
for linha in range(0, spritesheet.get_height(), 400):#percorrendo a largura da spritesheet de 400 em 400 pixels
    for coluna in range(0, spritesheet.get_width(), 400):
        frame = spritesheet.subsurface((coluna, linha, 400, 400))#extraindo os frames da spritesheet
        allframes.append(frame)
#Frames 0 a 5: inicializando
inicializando = True# para habilitar os sprites de inicialização
#Frames 6 e 7, 8 e 9, 10 e 11, 12 e 13, 14 e 15, 16 e 17, por fim 18 e 19 representam as vidas sendo perdidas
#Frame 20 é a derrota.
#Classe SpriteAnimation que herda de pygame.sprite.Sprite
class SpriteAnimation(pygame.sprite.Sprite):
    def __init__(self, frames):
        super().__init__()
        self.frames = frames
        self.frame_atual = 0
        self.image = self.frames[self.frame_atual]
        self.rect = self.image.get_rect()
        self.rect.center = (TELA_LARGURA // 2, 200)

    def update(self):
        global inicializando
        if inicializando:
            self.frame_atual = (self.frame_atual + 1) % len(self.frames)
            self.image = self.frames[self.frame_atual]
            if self.frame_atual == len(self.frames) - 1:
                inicializando = False
        else:
            self.frame_atual = (self.frame_atual + 1) % len(self.frames)
            self.image = self.frames[self.frame_atual]

# Banco de palavras
def carregar_palavras(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            palavras_com_definicao = [linha.strip().split(':') for linha in linhas]
        return palavras_com_definicao
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return []

palavras_com_definicao = carregar_palavras("dictionary/dictionary.txt")


def draw():
    # teste com alteração da cor de fundo
    tela.fill(blue)

def tela_de_derrota(palavra_correta, definicao):
    tela.fill(red)  # Vermelho para indicar a derrota
    fonteg = pygame.font.Font(None, 60)
    fontep = pygame.font.Font(None, 24)
    mensagem = fonteg.render("Você Perdeu o Jogo!", True, (0, 0, 0))
    mensagem2 = fontep.render(f"Palavra correta: {palavra_correta}", True, (0, 0, 0))
    mensagem3 = fontep.render(f"Definição: {definicao}", True, (0, 0, 0))
    mensagem4 = fontep.render("Essa Janela se auto destruirá em 3 segundos!", True, (0, 0, 0))
    mensagem_rect = mensagem.get_rect()
    mensagem2_rect = mensagem2.get_rect()
    mensagem3_rect = mensagem3.get_rect()
    mensagem4_rect = mensagem4.get_rect()
    mensagem_rect.center = (TELA_LARGURA // 2, TELA_ALTURA // 2 - 50)
    mensagem2_rect.center = (TELA_LARGURA // 2, TELA_ALTURA // 2)
    mensagem3_rect.center = (TELA_LARGURA // 2, TELA_ALTURA // 2 + 50)
    mensagem4_rect.center = (TELA_LARGURA // 2, TELA_ALTURA // 2 + 100)
    tela.blit(mensagem, mensagem_rect)
    tela.blit(mensagem2, mensagem2_rect)
    tela.blit(mensagem3, mensagem3_rect)
    tela.blit(mensagem4, mensagem4_rect)
    pygame.display.update()

def tela_acabou_palavras():
    tela.fill(yellow)
    fonteg = pygame.font.Font(None, 60)
    fontep = pygame.font.Font(None, 24)
    mensagem = fonteg.render("Não há mais palavras", True, (0, 0, 0))
    mensagem1 = fonteg.render("a serem adivinhadas", True, (0, 0, 0))
    mensagem2 = fontep.render("Essa Janela se auto destruirá em 5 segundos!", True, (0, 0, 0))
    mensagem_rect = mensagem.get_rect()
    mensagem1_rect = mensagem1.get_rect()
    mensagem2_rect = mensagem2.get_rect()
    mensagem_rect.center = (TELA_LARGURA // 2, TELA_ALTURA // 2 - 50)
    mensagem1_rect.center = (TELA_LARGURA // 2, TELA_ALTURA // 2)
    mensagem2_rect.center = (TELA_LARGURA // 2, TELA_ALTURA // 2 + 50)
    tela.blit(mensagem, mensagem_rect)
    tela.blit(mensagem1, mensagem1_rect)
    tela.blit(mensagem2, mensagem2_rect)
    pygame.display.update()

def tela_de_vitoria(palavra_vitoriosa, definicao):
    tela.fill(green)  # Preencha a tela com verde para indicar a vitória
    fonte_grande = pygame.font.Font(None, 60)
    fonte_pequena = pygame.font.Font(None, 24)
    mensagem_grande = fonte_grande.render("Você Venceu!", True, (0, 0, 0))
    mensagem_grande_rect = mensagem_grande.get_rect()
    mensagem_grande_rect.center = (TELA_LARGURA // 2, TELA_ALTURA // 2 - 50)
    mensagem_pequena = fonte_pequena.render(f"Palavra: {palavra_vitoriosa}", True, (0, 0, 0))
    mensagem_pequena_rect = mensagem_pequena.get_rect()
    mensagem_pequena_rect.center = (TELA_LARGURA // 2, TELA_ALTURA // 2)
    mensagem_definicao = fonte_pequena.render(f"Definição: {definicao}", True, (0, 0, 0))
    mensagem_definicao_rect = mensagem_definicao.get_rect()
    mensagem_definicao_rect.center = (TELA_LARGURA // 2, TELA_ALTURA // 2 + 50)
    mensagem_recomecar = fonte_pequena.render("Pressione R para Recomeçar", True, (0, 0, 0))
    mensagem_recomecar_rect = mensagem_recomecar.get_rect()
    mensagem_recomecar_rect.center = (TELA_LARGURA // 2, TELA_ALTURA // 2 + 100)
    tela.blit(mensagem_grande, mensagem_grande_rect)
    tela.blit(mensagem_pequena, mensagem_pequena_rect)
    tela.blit(mensagem_definicao, mensagem_definicao_rect)
    tela.blit(mensagem_recomecar, mensagem_recomecar_rect)
    pygame.display.update()

def tela_selecao_dificuldade():
    selecao_loop = True
    dificuldade = 0  # Padrão para fácil

    while selecao_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    dificuldade = 2  # Fácil
                    selecao_loop = False
                elif event.key == pygame.K_1:
                    dificuldade = 1  # Difícil
                    selecao_loop = False

        tela.fill(blue)
        fonte_grande = pygame.font.Font(None, 60)
        fonte_pequena = pygame.font.Font(None, 36)

        mensagem_grande = fonte_grande.render("Escolha a Dificuldade", True, (0, 0, 0))
        mensagem_grande_rect = mensagem_grande.get_rect()
        mensagem_grande_rect.center = (TELA_LARGURA // 2, TELA_ALTURA // 2 - 50)

        mensagem_facil = fonte_pequena.render("1 - Dificil", True, (0, 0, 0))
        mensagem_facil_rect = mensagem_facil.get_rect()
        mensagem_facil_rect.center = (TELA_LARGURA // 2, TELA_ALTURA // 2 + 20)

        mensagem_dificil = fonte_pequena.render("2 - Facil", True, (0, 0, 0))
        mensagem_dificil_rect = mensagem_dificil.get_rect()
        mensagem_dificil_rect.center = (TELA_LARGURA // 2, TELA_ALTURA // 2 + 70)

        tela.blit(mensagem_grande, mensagem_grande_rect)
        tela.blit(mensagem_facil, mensagem_facil_rect)
        tela.blit(mensagem_dificil, mensagem_dificil_rect)

        pygame.display.update()
        clock.tick(5)

    return dificuldade



def reinicia_game(repetidas, palavra_e_definicao):
    repetidas.append(palavra_e_definicao)
    palavras_com_definicao.remove(palavra_e_definicao)
    if len(palavras_com_definicao) > 0:
        palavra_e_definicao = random.choice(palavras_com_definicao)
    return palavra_e_definicao

# Posições iniciais para fazer os traços
traco_x_inicial = 100
traco_y = 400
espacamento = 50

def tracoDasLetras(palavra, traco_x, traco_y, espacamento):
    tracos = []
    for i in range(len(palavra)):
        traco = (traco_x, traco_y)
        tracos.append(traco)
        traco_x += espacamento
    return tracos

def desenhar_letras(letras_corretas, tracos):
    fonte = pygame.font.Font(None, 36)
    for i, letra in enumerate(letras_corretas):
        if letra != '_':
            letra_surface = fonte.render(letra, True, (0, 0, 0))
            letra_rect = letra_surface.get_rect()
            letra_rect.center = (tracos[i][0] + espacamento // 2, tracos[i][1] - 30)
            tela.blit(letra_surface, letra_rect)

def desenha_boneco(cid):#inicialmente será representado por um contador de vidas
    tela.blit(cid.image, cid.rect)

def atualiza_boneco(qtdvidas, dificuldade, cid):
    # Lista de índices para os frames
    frames_indices = []

    # 7 vidas para o modo fácil
    # 4 vidas para o modo difícil, 5, 8 e 9, 12 e 13, 16 a 19 e 20 para o fim
    if dificuldade == 1:#dificil
        if qtdvidas == 0:
            frames_indices = [20]  # Derrota
        elif qtdvidas == 1:
            frames_indices = list(range(16, 20))  # inclui o primeiro mas não inclui o segundo limite
        elif qtdvidas == 2:
            frames_indices = list(range(12, 14))
        elif qtdvidas == 3:
            frames_indices = list(range(8, 10))
        else:
            frames_indices = [5]

    elif dificuldade == 2:#Facil
        if qtdvidas == 0:
            frames_indices = [20]  # Derrota
        elif qtdvidas == 1:
            frames_indices = list(range(16, 20))  # inclui o primeiro mas não inclui o segundo limite
        elif qtdvidas == 2:
            frames_indices = list(range(14, 16))
        elif qtdvidas == 3:
            frames_indices = list(range(12, 14))
        elif qtdvidas == 4:
            frames_indices = list(range(10, 12))
        elif qtdvidas == 5:
            frames_indices = list(range(8, 10))
        elif qtdvidas == 6:
            frames_indices = list(range(6, 8))
        else:
            frames_indices = [5]

    # Atualiza os frames do objeto cid com os índices obtidos
    cid.frames = [allframes[i] for i in frames_indices]
# O problema que chashava o jogo acontecia aqui, quando o intervalo de frames era de um frame só a função update de
# SpryteAnimation tentava verificar o tamanhho de um frame e não de uma lista de frames.

clock = pygame.time.Clock()

gameLoop = True
if __name__ == '__main__':
    #escolhe uma palavra do banco de palavras
    palavra_e_definicao = random.choice(palavras_com_definicao)
    palavra, definicao = palavra_e_definicao[0].upper(), palavra_e_definicao[1]
    print(palavra)#com a finalidade de conferencia
    # Cria uma lista inicializada com sublinhados e com numero de elementos igual à quantidade de letras na palavra
    letras_corretas = ['_' for _ in palavra]

    #Seleciona a dificuldade baseado no input da tela de seleção
    dificuldade = tela_selecao_dificuldade()
    #seleciona a quantidade de vidas baseado na dificuldade
    vidas = 1 + 3*dificuldade # 1+3 ou 1+6
    #print(dificuldade)
    #print(vidas)

    # Banco de palavras ja usadas numa secao
    repetidas = []
    indicadores = Indicadores((10, TELA_ALTURA/2 + 100), 15, (10, 10, 10))

    cid = SpriteAnimation(allframes[0:6])

    while gameLoop:
        if(vidas <= 0):
            #Tempo para apresentar o sprite de derrota do boneco
            pygame.time.delay(2000)
            tela_de_derrota(palavra, definicao)
            # Para esperar 3 segundos antes de fechar o programa
            pygame.time.delay(3000)
            gameLoop = False

        #encerra o programa caso não haja mais palavras a serem adivinhadas
        if len(palavras_com_definicao) == 0:
            tela_acabou_palavras()
            # Para esperar 5 segundos antes de fechar o programa
            pygame.time.delay(5000)
            gameLoop = False

        # Verifica se não há mais letras em branco na palavra
        # ou seja, se o jogador ganhou
        if '_' not in letras_corretas:
            tela_de_vitoria(palavra, definicao)
            pygame.display.update()
            winnerloop = True
            while winnerloop:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameLoop = False
                        winnerloop = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            palavra_e_definicao = reinicia_game(repetidas, palavra_e_definicao)
                            palavra, definicao = palavra_e_definicao[0].upper(), palavra_e_definicao[1]
                            letras_corretas = ['_' for _ in palavra]
                            vidas = 1 + 3 * dificuldade
                            #Para resetar a inicialização do cid
                            cid = SpriteAnimation(allframes[0:6])
                            inicializando = True
                            #Assim ele mostra novamente o nome CID se formando toda vez q reinicia
                            indicadores = Indicadores((10, TELA_ALTURA/2 + 100), 15, (10, 10, 10))
                            ganhou = False
                            winnerloop = False
                            gameLoop = True  # Adicionei esta linha para reiniciar o jogo (Conrado)
                        if event.key == pygame.K_q:
                            gameLoop = False
                            restart = False
                            winnerloop = False

        for event in pygame.event.get():
            # Clicaram no X na janela para fechar
            if event.type == pygame.QUIT:
                gameLoop = False

            # O jogador interagiu com o teclado
            elif event.type == pygame.KEYDOWN:
                # A tecla pressionada é uma letra
                if event.unicode.isalpha() and len(event.unicode) == 1:
                    # Conversão para maiúscula
                    chute = event.unicode.upper()
                    print(palavra)
                    print(chute)
                    indicadores.atualizar(chute, palavra)
                    if chute in palavra:
                        for i, letra in enumerate(palavra):
                            if letra == chute:
                                letras_corretas[i] = chute
                    else:
                        vidas-=1
                        #atualiza_boneco(vidas, dificuldade, cid)
        tracos = tracoDasLetras(palavra, traco_x_inicial, traco_y, espacamento)
        draw()

        # Desenhando os traços das letras (tela, cor, inicio, fim, largura)
        for traco in tracos:
            pygame.draw.line(tela, (0, 0, 0), (traco[0], traco_y), (traco[0] + espacamento - 10, traco_y), 2)

        indicadores.desenhar(tela)
        desenhar_letras(letras_corretas, tracos)

        # Muda o intervalo de sprites que deve ser apresentado
        if not inicializando:
            atualiza_boneco(vidas, dificuldade, cid)
            # dessa forma o cid inicializa apenas uma vez, de acordo com o codigo update


        # Troca as sprites dentro de um intervalo especifico
        cid.update()

        # Apresenta um sprite na tela
        desenha_boneco(cid)

        pygame.display.flip()
        clock.tick(5)  # Limite de frames por segundo
        pygame.display.update()

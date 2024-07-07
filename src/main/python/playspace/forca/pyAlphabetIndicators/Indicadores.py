import pygame

class Indicadores:
    def __init__(self, letras, posicao_inicial, espacamento, cor_inicial):
        self.letras = letras  # Lista de letras (pode ser o alfabeto)
        self.posicao_inicial = posicao_inicial  # Posição inicial (x, y) na tela
        self.espacamento = espacamento  # Espaçamento entre as letras
        self.cor_inicial = cor_inicial  # Cor inicial das letras

        self.indicadores = []  # Lista de indicadores de letras (letra, cor)
        self.fonte = pygame.font.Font(None, 36)

        # Inicializa os indicadores com as letras e a cor inicial
        for letra in self.letras:
            self.indicadores.append((letra, self.cor_inicial))

    def atualizar(self, chute, cor_acerto, cor_erro):
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

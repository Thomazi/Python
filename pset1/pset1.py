# IDENTIFICAÇÃO DO ESTUDANTE:
# Preencha seus dados e leia a declaração de honestidade abaixo. NÃO APAGUE
# nenhuma linha deste comentário de seu código!
#
#    Nome completo: Gabriel Thomazi Rosa    
#    Matrícula: 202299883   
#    Turma: CC3m
#    Email: gabrielthomazirosa@outlook.com
#
# DECLARAÇÃO DE HONESTIDADE ACADÊMICA:
# Eu afirmo que o código abaixo foi de minha autoria. Também afirmo que não
# pratiquei nenhuma forma de "cola" ou "plágio" na elaboração do programa,
# e que não violei nenhuma das normas de integridade acadêmica da disciplina.
# Estou ciente de que todo código enviado será verificado automaticamente
# contra plágio e que caso eu tenha praticado qualquer atividade proibida
# conforme as normas da disciplina, estou sujeito à penalidades conforme
# definidas pelo professor da disciplina e/ou instituição.
#


# Imports permitidos (não utilize nenhum outro import!):
import sys
import math
import base64
import tkinter
from io import BytesIO
from PIL import Image as PILImage


# Classe Imagem:
class Imagem:
    def __init__(self, largura, altura, pixels):
        self.largura = largura
        self.altura = altura
        self.pixels = pixels

    def get_pixel(self, x, y):
        if 0 <= x < self.largura and 0 <= y < self.altura:  # Verifica se as coordenadas estão dentro dos limites de altura e largura
            i = y * self.largura + x  # Calcula o índice na lista plana de pixels
            return self.pixels[i]  # Retorna o valor do pixel na posição

        # Trata os pixels fora dos limites como se estivessem na borda estendida da imagem
        # Se 'x' for maior que 'self.largura -1', estendido_x vai ser igual a 'self.largura -1', Caso contrário vai ser igual a 'x'
        # Em seguida a função 'max(0, estendido_x)' garante que 'estendido_x' seja o maior valor entre '0' e 'estendido_x'
        # Logo se 'estendido_x' < '0' (se x < 0), 'estendido_x' será ajustado para '0', caso contrário 'estendido_x' permanecerá o mesmo
        else:
            estendido_x = max(0, min(x, self.largura - 1))
            estendido_y = max(0, min(y, self.altura - 1))
            estendido_i = (self.largura * estendido_y) + estendido_x
            return self.pixels[estendido_i]

    def set_pixel(self, x, y, c):
        i = y * self.largura + x  # Calcula o índice correspondente na lista plana de pixels
        self.pixels[i] = c  # Define o valor do pixel no índice calculado como c

    def aplicar_por_pixel(self, func):
        resultado = Imagem.nova(self.largura, self.altura)  # Cria uma nova imagem com as mesmas dimensões da imagem original
        for x in range(resultado.largura):  # Percorre as coordenadas x da nova imagem
            for y in range(resultado.altura):  # Percorre as coordenadas y da nova imagem
                cor = self.get_pixel(x, y)  # Obtém o valor do pixel na posição (x, y) da imagem original
                nova_cor = func(cor)  # Aplica a função 'func' ao valor do pixel
                resultado.set_pixel(x, y, nova_cor)  # Define o valor do pixel na nova imagem como o resultado da função aplicada ao pixel original
        return resultado  # Retorna a nova imagem resultante

    def invertida(self):
        return self.aplicar_por_pixel(lambda c: 255 - c)  # Aplica uma função lambda para inverter os valores dos pixels

    def borrada(self, n):
        # Cria um kernel de desfoque de caixa n x n
        kernel = [[1 / (n * n) for _ in range(n)] for _ in range(n)] 

        # Obtém as dimensões da imagem de entrada
        largura, altura = self.largura, self.altura

        # Cria uma nova imagem com as mesmas dimensões da imagem de entrada
        nova_imagem = Imagem.nova(largura, altura)

        # Aplica a correlação da imagem com o kernel de desfoque de caixa
        for y in range(altura):
            for x in range(largura):
                soma = 0.0
                for ky in range(n):
                    for kx in range(n):
                        # Obtém o pixel da imagem de entrada usando o deslocamento do kernel
                        pixel = self.get_pixel(x - n // 2 + kx, y - n // 2 + ky)
                        peso = kernel[ky][kx]
                        soma += pixel * peso

                # Define o valor do pixel na nova imagem, arredondando para o valor inteiro mais próximo
                valor_pixel = int(round(soma))
                valor_pixel = max(0, min(valor_pixel, 255))  # Limita o valor do pixel ao intervalo [0, 255]
                nova_imagem.set_pixel(x, y, valor_pixel)

        return nova_imagem

    def focada(self, n):
        imagem_borrada = self.borrada(n)  # Aplica o efeito de desfoque na imagem original e armazena o resultado na variável "imagem_borrada"

        largura, altura = self.largura, self.altura  # Obtém a largura e altura da imagem original e atribui às variáveis "largura" e "altura"
        nova_imagem = Imagem.nova(largura, altura)  # Cria uma nova imagem com a mesma largura e altura da imagem original

        for y in range(altura):  # Loop que percorre as coordenadas y da imagem
            for x in range(largura):  # Loop que percorre as coordenadas x da imagem
                pixel_original = self.get_pixel(x, y)  # Obtém o valor do pixel original na posição (x, y)
                pixel_borrado = imagem_borrada.get_pixel(x, y)  # Obtém o valor do pixel borrado na posição (x, y)
                pixel_nitido = round(2 * pixel_original - pixel_borrado)  # Calcula o valor do pixel nítido usando a fórmula de nitidez
                pixel_nitido = max(min(pixel_nitido, 255), 0)  # Limita o valor do pixel nítido entre 0 e 255
                nova_imagem.set_pixel(x, y, pixel_nitido)  # Define o valor do pixel nítido na nova imagem

        return nova_imagem  # Retorna a nova imagem com os pixels nítidos

    def bordas(self):
        largura, altura = self.largura, self.altura
        nova_imagem = Imagem.nova(largura, altura)

        # Definir os kernels Kx e Ky corretamente
        Kx = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
        Ky = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]

        # Aplicar a correlação com Kx e Ky
        Ox = self.correlacao_imagem_kernel(Kx)
        Oy = self.correlacao_imagem_kernel(Ky)

        for y in range(altura):
            for x in range(largura):
                # Obter os valores de Ox e Oy
                Ox_valor = Ox.get_pixel(x, y)
                Oy_valor = Oy.get_pixel(x, y)

                # Calcular a magnitude do gradiente
                magnitude = math.sqrt(pow(Ox_valor, 2) + pow(Oy_valor, 2))
                magnitude = round(magnitude)
                magnitude = max(min(magnitude, 255), 0)
                nova_imagem.set_pixel(x, y, magnitude)

        return nova_imagem

    def correlacao_imagem_kernel(self, kernel):
        # Obtém as dimensões da imagem de entrada
        largura, altura = self.largura, self.altura
    
        # Cria uma nova imagem com as mesmas dimensões da imagem de entrada
        nova_imagem = Imagem.nova(largura, altura)
    
        # Aplica a correlação da imagem com o kernel
        for y in range(altura):
            for x in range(largura):
                soma = 0.0
                for ky in range(len(kernel)):
                    for kx in range(len(kernel[0])):
                        # Obtém o pixel da imagem de entrada usando o deslocamento do kernel
                        pixel = self.get_pixel(x - len(kernel[0]) // 2 + kx, y - len(kernel) // 2 + ky)
                        peso = kernel[ky][kx]
                        soma += pixel * peso
                nova_imagem.set_pixel(x, y, int(soma))
    
        return nova_imagem

    # Abaixo deste ponto estão utilitários para carregar, salvar e mostrar
    # as imagens, bem como para a realização de testes.

    def __eq__(self, other):
        return all(getattr(self, i) == getattr(other, i)
                   for i in ('altura', 'largura', 'pixels'))

    def __repr__(self):
        return "Imagem(%s, %s, %s)" % (self.largura, self.altura, self.pixels)

    @classmethod
    def carregar(cls, nome_arquivo):
        """
        Carrega uma imagem do arquivo fornecido e retorna uma instância dessa
        classe representando essa imagem. Também realiza a conversão para tons
        de cinza.

        Invocado como, por exemplo:
           i = Imagem.carregar('test_images/cat.png')
        """
        with open(nome_arquivo, 'rb') as guia_para_imagem:
            img = PILImage.open(guia_para_imagem)
            img_data = img.getdata()
            if img.mode.startswith('RGB'):
                pixels = [round(.299 * p[0] + .587 * p[1] + .114 * p[2]) for p in img_data]
            elif img.mode == 'LA':
                pixels = [p[0] for p in img_data]
            elif img.mode == 'L':
                pixels = list(img_data)
            else:
                raise ValueError('Modo de imagem não suportado: %r' % img.mode)
            l, a = img.size
            return cls(l, a, pixels)

    @classmethod
    def nova(cls, largura, altura):
        """
        Cria imagens em branco (tudo 0) com a altura e largura fornecidas.

        Invocado como, por exemplo:
            i = Imagem.nova(640, 480)
        """
        return cls(largura, altura, [0 for i in range(largura * altura)])

    def salvar(self, nome_arquivo, modo='PNG'):
        """
        Salva a imagem fornecida no disco ou em um objeto semelhante a um arquivo.
        Se o nome_arquivo for fornecido como uma string, o tipo de arquivo será
        inferido a partir do nome fornecido. Se nome_arquivo for fornecido como
        um objeto semelhante a um arquivo, o tipo de arquivo será determinado
        pelo parâmetro 'modo'.
        """
        saida = PILImage.new(mode='L', size=(self.largura, self.altura))
        saida.putdata(self.pixels)
        if isinstance(nome_arquivo, str):
            saida.save(nome_arquivo)
        else:
            saida.save(nome_arquivo, modo)
        saida.close()

    def gif_data(self):
        """
        Retorna uma string codificada em base 64, contendo a imagem
        fornecida, como uma imagem GIF.

        Função utilitária para tornar show_image um pouco mais limpo.
        """
        buffer = BytesIO()
        self.salvar(buffer, modo='GIF')
        return base64.b64encode(buffer.getvalue())

    def mostrar(self):
        """
        Mostra uma imagem em uma nova janela Tk.
        """
        global WINDOWS_OPENED
        if tk_root is None:
            # Se Tk não foi inicializado corretamente, não faz mais nada.
            return
        WINDOWS_OPENED = True
        toplevel = tkinter.Toplevel()
        # O highlightthickness=0 é um hack para evitar que o redimensionamento da janela
        # dispare outro evento de redimensionamento (causando um loop infinito de
        # redimensionamento). Para maiores informações, ver:
        # https://stackoverflow.com/questions/22838255/tkinter-canvas-resizing-automatically
        tela = tkinter.Canvas(toplevel, height=self.altura,
                              width=self.largura, highlightthickness=0)
        tela.pack()
        tela.img = tkinter.PhotoImage(data=self.gif_data())
        tela.create_image(0, 0, image=tela.img, anchor=tkinter.NW)

        def ao_redimensionar(event):
            # Lida com o redimensionamento da imagem quando a tela é redimensionada.
            # O procedimento é:
            #  * converter para uma imagem PIL
            #  * redimensionar aquela imagem
            #  * obter os dados GIF codificados em base 64 (base64-encoded GIF data)
            #    a partir da imagem redimensionada
            #  * colocar isso em um label tkinter
            #  * mostrar a imagem na tela
            nova_imagem = PILImage.new(mode='L', size=(self.largura, self.altura))
            nova_imagem.putdata(self.pixels)
            nova_imagem = nova_imagem.resize((event.largura, event.altura), PILImage.NEAREST)
            buffer = BytesIO()
            nova_imagem.save(buffer, 'GIF')
            tela.img = tkinter.PhotoImage(data=base64.b64encode(buffer.getvalue()))
            tela.configure(height=event.altura, width=event.largura)
            tela.create_image(0, 0, image=tela.img, anchor=tkinter.NW)

        # Por fim, faz o bind da função para que ela seja chamada quando a tela
        # for redimensionada:
        tela.bind('<Configure>', ao_redimensionar)
        toplevel.bind('<Configure>', lambda e: tela.configure(height=e.altura, width=e.largura))

        # Quando a tela é fechada, o programa deve parar
        toplevel.protocol('WM_DELETE_WINDOW', tk_root.destroy)


# Não altere o comentário abaixo:
# noinspection PyBroadException
try:
    tk_root = tkinter.Tk()
    tk_root.withdraw()
    tcl = tkinter.Tcl()


    def refaz_apos():
        tcl.after(500, refaz_apos)


    tcl.after(500, refaz_apos)
except:
    tk_root = None

WINDOWS_OPENED = False

if __name__ == '__main__':
    # O código neste bloco só será executado quando você executar
    # explicitamente seu script e não quando os testes estiverem
    # sendo executados. Este é um bom lugar para gerar imagens, etc.
    imagem_original = Imagem.carregar("test_images/construct.png")
    imagem_borda = imagem_original.bordas()

    imagem_original.mostrar()
    imagem_borda.mostrar()
    imagem_borda.salvar("construcao.png")

    pass

    # O código a seguir fará com que as janelas de Imagem.mostrar
    # sejam exibidas corretamente, quer estejamos executando
    # interativamente ou não:
    if WINDOWS_OPENED and not sys.flags.interactive:
        tk_root.mainloop()

import random
import time
from graphics import *

class digito:
    def __init__(self, ponto):
        self.X = ponto.getX()
        self.Y = ponto.getY()
        self.ponto = ponto
    
    def desenhar(self, janela):
        digito = Rectangle(Point(self.X+50, self.Y+70), Point(self.X-50, self.Y-70))
        digito.setWidth(15)
        digito.draw(janela)
        self.D = Text(self.ponto, "7")
        self.D.setSize(30)
        self.D.setFill("red")
        self.D.draw(janela)
        
    def animar(self, n, opcoes):
        self.D.undraw()
        self.D = Text(self.ponto, opcoes[n%7])
        self.D.setSize(30)
        self.D.setFill("red")
        self.D.draw(janela)
        
    def mudar(self, valor):
        self.D.undraw()
        self.D = Text(self.ponto, valor)
        self.D.setSize(30)
        self.D.setFill("red")
        self.D.draw(janela)
        

opcoes = ["--", "0", "A", "J", "Q", "K", "7"]
pesos = [50,40,30,20,10,5,1]
ganho = [5, 10, 20, 70, 200, 1_000, 100_000]

def base():    
    dinheiro = float(input("Quantos créditos quer depositar? "))
    if dinheiro<=0:
        print("tente de novo")
        dinheiro = base()
    return(dinheiro)

def clicar():
    p = janela.getMouse()
    if not(635<p.getX()<725 and 55<p.getY()<145):
        p = clicar()
    return(p)

def apostar(dinheiro):
    aposta1 = Entry(Point(300,50), 5)
    aposta1.setText("00")
    aposta1.setSize(20)
    aposta1.draw(janela)
    clicar()
    aposta = float(aposta1.getText())
    if aposta>dinheiro or 0>=aposta:
        print("aposta inválida")
        aposta = apostar(dinheiro)
    return(aposta)

dinheiro = base()

janela = GraphWin("Slot Machine", 760, 400)
janela.setBackground(color_rgb(200, 200, 200))

Aviso = Text(Point(300, 15), "quantos creditos quer apostar?")
Aviso.setSize(13)
Aviso.draw(janela)

linha = Line(Point(680, 100), Point(680, 300))
linha.setWidth(10)
linha.draw(janela)

Bola = Circle(Point(680, 100), 45)
Bola.setFill("red")
Bola.draw(janela)

Texto = Text(Point(680, 30), "Jogar!")
Texto.setSize(15)
Texto.draw(janela)

Dinheiro = Text(Point(300, 350), dinheiro)
Dinheiro.setSize(15)
Dinheiro.draw(janela)

espaço = 200
controle = []
for i in range(3):
    D = digito(Point((i)*espaço + (espaço/2), 200))
    D.desenhar(janela)
    controle.append(D)

while dinheiro>0:
    aposta=apostar(dinheiro)
    
    dinheiro -= aposta
    ds = []
    
    for i in range(3):
        ds.append(random.choices(opcoes, pesos)[0]) 
        
    for i in range(25):
        t = time.time()
        for i2 in controle:
            i2.animar(i, opcoes)
        Bola.move(0,4)
        time.sleep(t - time.time() + 0.04)
    controle[0].mudar(ds[0])
    
    for i in range(30):
        t = time.time()
        for i2 in controle[1:3]:
            i2.animar(i, opcoes)
        if i<25:
            Bola.move(0,4)
        else:
            Bola.move(0,-4)
        time.sleep(t - time.time() + 0.04)
    controle[1].mudar(ds[1])
    
    for i in range(45):
        t = time.time()
        controle[2].animar(i, opcoes)
        Bola.move(0,-4)
        time.sleep(t - time.time() + 0.04)
    controle[2].mudar(ds[2])


    a = True
    b = ds[0]
    for i in ds[1:len(ds)]:
        if i!=b:
            a = False
            break
    if a:
        print("PARABÉNS!!")
        dinheiro += aposta*ganho[opcoes.index(ds[0])]
    Dinheiro.undraw()
    Dinheiro = Text(Point(300, 350), dinheiro)
    Dinheiro.setSize(15)
    Dinheiro.draw(janela)
    
janela.close()
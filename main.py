from browser import document, window
import random

def sketch(p):

    def setup():
        p.createCanvas(700, 410)
        p.background(255)
        p.rectMode(p.CENTER)

    def draw():
        colorlist = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black']
        p.noStroke()
        p.fill(random.choice(colorlist))
        p.ellipse(p.mouseX, p.mouseY, 50, 50)

    def mousePressed():
        p.background(0)

    def keyPressed():
        if p.key == ' ':
            print("ALOHA!!")

    p.setup = setup
    p.draw = draw
    p.mousePressed = mousePressed
    p.keyPressed = keyPressed

window.p5.new(sketch)

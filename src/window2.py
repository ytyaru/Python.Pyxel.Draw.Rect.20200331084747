#!/usr/bin/env python3
# coding: utf8
import pyxel
class App:
    def __init__(self):
        pyxel.init(256, 256, border_width=0)
        pyxel.run(self.update, self.draw)
    def update(self): pass
    def draw(self):
        pyxel.cls(0)
        pyxel.rect(0, 0, 64, 64, 8) # x, y, w, h, col

App()

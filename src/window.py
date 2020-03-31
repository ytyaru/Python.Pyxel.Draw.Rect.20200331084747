#!/usr/bin/env python3
# coding: utf8
import pyxel
def update(): pass
def draw():
    pyxel.cls(0)
    pyxel.rect(0, 0, 64, 64, 8) # x, y, w, h, col
pyxel.init(256, 256, border_width=0)
pyxel.run(update, draw)

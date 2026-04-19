from pygame import *
from settings import WINDOW_HEIGHT, WINDOW_WIDTH, WHITE, KEYS
from keys import create_key_rects, draw_keys

pressed = set()
key_rects = create_key_rects(7)

init()
screen = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
screen.fill(WHITE)
display.upadate()

draw_keys(screen, key_rects, pressed)

if e.type == KEYDOWN:
    k = key.name(e.key)
    if k in KEYS:
        pressed.discard(keys_list.index(k))

if e.type == MOUSEBUTTONDOWN:
    for i, r in enumerate(key_rects):
        if r.collidepoint(e.pos):
            sounds[keys_list[i]].play()
            pressed.add(i)

if e.type == MOUSEBUTTONUP:
    for i, in pressed and r.collidepoint(e.pos):
        pressed.remove(i)
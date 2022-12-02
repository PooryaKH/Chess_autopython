import chess
import chess.engine
import value as value
import pyautogui
import time
from PIL import ImageGrab
from pynput import keyboard
from ahk import AHK
import ctypes  # An included library with Python install.
import tkinter as tk

engine = chess.engine.SimpleEngine.popen_uci(r"C:\Anechka008.exe")

board = chess.Board()

ahk = AHK()
lx = [0, 0]
ly = [0, 0]
length_x = (lx[1] - lx[0]) / 8
length_y = (ly[1] - ly[0]) / 8


ahk.send_input('{Alt Down}{Tab}{Alt Up}')
time.sleep(0.3)
px = ImageGrab.grab().load()
for x in range(0, 960):
    for y in range(0, 540):
        color = px[x, y]

        if color[0] == 238 and color[1] == 238 and color[2] == 210:
            lx[0] = x
            ly[0] = y
            break
    if y < 539:
        break

y = ly[0]
for x in range(lx[0], 1920):
    color = px[x, y]

    if not ((color[0] == 238 and color[1] == 238 and color[2] == 210) or (
            color[0] == 118 and color[1] == 150 and color[2] == 86)):
        lx[1] = x - 1
        break

x = lx[0]
for y in range(ly[0], 1080):
    color = px[x, y]

    if not ((color[0] == 238 and color[1] == 238 and color[2] == 210) or (
            color[0] == 118 and color[1] == 150 and color[2] == 86)):
        ly[1] = y - 1
        break

print("Board detected successfully!", lx, ly)
length_x = (lx[1] - lx[0]) / 8
length_y = (ly[1] - ly[0]) / 8

flag = False
s_cord = [0,0]
d_cord = [0,0]
move = ""

for x in range(1, 9):
    for y in range(1, 9):
        color = px[lx[0] + length_x * x - 5, ly[0] + length_y * y - 5]

        if (color[0] == 186 and color[1] == 202 and color[2] == 43) or (
            color[0] == 246 and color[1] == 246 and color[2] == 105):
            color = px[lx[0] + length_x * x - 5 - length_x / 2, ly[0] + length_y * y - 15]
            flag = True
            if not ((color[0] == 238 and color[1] == 238 and color[2] == 210) or (
                color[0] == 118 and color[1] == 150 and color[2] == 86) or (
                        color[0] == 186 and color[1] == 202 and color[2] == 43) or (
                        color[0] == 246 and color[1] == 246 and color[2] == 105)):
                d_cord[0] = x
                d_cord[1] = 9 - y
            else:
                s_cord[0] = x
                s_cord[1] = 9 - y
if flag:
    print("Your Black")
    move = chr(s_cord[0] + 96) + str(s_cord[1]) + chr(d_cord[0] + 96) + str(d_cord[1])
    board.push(chess.Move.from_uci(move))
    print("Push Move:", move)
    result = engine.play(board, chess.engine.Limit(depth=7))
    move = str(result.move)
    board.push(chess.Move.from_uci(move))
    print(move)

else:
    print("Your White")
    move = "b1a3"
    print("Push Move:", move)
    board.push(chess.Move.from_uci(move))


ahk.mouse_move(lx[0] + length_x * (ord(move[0]) - 97) + 5, ly[0] + length_y * (8-int(move[1])) + 5, 0, blocking=True)
time.sleep(0.1)
ahk.mouse_drag(lx[0] + length_x * (ord(move[2]) - 97) + 5, ly[0] + length_y * (8-int(move[3])) + 5,blocking=True)
time.sleep(0.3)


while True:
    while True:
        px = ImageGrab.grab().load()
        flag = False
        s_cord = [0, 0]
        d_cord = [0, 0]
        for x in range(1, 9):
            for y in range(1, 9):
                color = px[lx[0] + length_x * x - 5, ly[0] + length_y * y - 5]
                #ahk.mouse_move(lx[0] + length_x * x - 5, ly[0] + length_y * y - 5, blocking=True)
                if (color[0] == 186 and color[1] == 202 and color[2] == 43) or (
                        color[0] == 246 and color[1] == 246 and color[2] == 105):
                    color = px[lx[0] + length_x * x - 5 - length_x / 2, ly[0] + length_y * y - 15]
                    time.sleep(0.2)
                    if (color[0] == 186 and color[1] == 202 and color[2] == 43) or (color[0] == 246 and color[1] == 246 and color[2] == 105):
                        s_cord[0] = x
                        s_cord[1] = 9 - y
                    else:
                        d_cord[0] = x
                        d_cord[1] = 9 - y


                    flag = True
        if flag and not (d_cord[0] == 0 or d_cord[1] == 0 or s_cord[1] == 0 or s_cord[0] == 0):
            if move != chr(s_cord[0] + 96) + str(s_cord[1]) + chr(d_cord[0] + 96) + str(d_cord[1]):
                move = chr(s_cord[0] + 96) + str(s_cord[1]) + chr(d_cord[0] + 96) + str(d_cord[1])
                break
    print("Push Move:", move)
    board.push(chess.Move.from_uci(move))
    result = engine.play(board, chess.engine.Limit(depth=4))
    move = str(result.move)
    board.push(chess.Move.from_uci(move))
    print(result)
    ahk.mouse_move(lx[0] + length_x * (ord(move[0])-97) + 5, ly[0] + length_y * (8-int(move[1])) + 5,0,blocking=True)
    ahk.mouse_drag(lx[0] + length_x * (ord(move[2])-97) + 5, ly[0] + length_y * (8-int(move[3])) + 5,blocking=True)


    while True:
        px = ImageGrab.grab().load()
        color = px[lx[0] + length_x * (ord(move[0])-96) - 5, ly[0] + length_y * (9-int(move[1])) - 5]
        if not ((color[0] == 186 and color[1] == 202 and color[2] == 43) or (
        color[0] == 246 and color[1] == 246 and color[2] == 105)):
            break
        color = px[lx[0] + length_x * (ord(move[2])-96) - 5, ly[0] + length_y * (9-int(move[3])) - 5]
        if not ((color[0] == 186 and color[1] == 202 and color[2] == 43) or (
        color[0] == 246 and color[1] == 246 and color[2] == 105)):
            break




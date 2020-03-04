import time
import random
from random import shuffle
a1 = " "
a2 = " "
a3 = " "
a4 = " "
a5 = " "
b1 = " "
b2 = " "
b3 = " "
b4 = " "
b5 = " "
c1 = " "
c2 = " "
c3 = " "
c4 = " "
c5 = " "
d1 = " "
d2 = " "
d3 = " "
d4 = " "
d5 = " "
e1 = " "
e2 = " "
e3 = " "
e4 = " "
e5 = " "
c_a1 = " "
c_a2 = " "
c_a3 = " "
c_a4 = " "
c_a5 = " "
c_b1 = " "
c_b2 = " "
c_b3 = " "
c_b4 = " "
c_b5 = " "
c_c1 = " "
c_c2 = " "
c_c3 = " "
c_c4 = " "
c_c5 = " "
c_d1 = " "
c_d2 = " "
c_d3 = " "
c_d4 = " "
c_d5 = " "
c_e1 = " "
c_e2 = " "
c_e3 = " "
c_e4 = " "
c_e5 = " "
t = "  "
board0 = """
   a  b  c  d  e\n"""
board1 = "1  " +a1+t+b1+t+c1+t+d1+t+e1+"\n"
board2 = "2  "+a2+t+b2+t+c2+t+d2+t+e2+"\n"
board3 = "3  "+a3+t+b3+t+c3+t+d3+t+e3+"\n"
board4 = "4  "+a4+t+b4+t+c4+t+d4+t+e4+"\n"
board5 = "5  "+a5+t+b5+t+c5+t+d5+t+e5+"\n"
board = board0 + board1 + board2 + board3 + board4 + board5
print(board)

ship1 = input("Where would you like to place your first battleship?\n")

ship1 = ship1.strip(' ').lower()

if ship1[0] == 'a':
  if int(ship1[1]) == 1:
    a1 = 'S'
  elif int(ship1[1]) == 2:
    a2 = 'S'
  elif int(ship1[1]) == 3:
    a3 = 'S'
  elif int(ship1[1]) == 4:
    a4 = 'S'
  elif int(ship1[1]) == 5:
    a5 = 'S'
elif ship1[0] == 'b':
  if int(ship1[1]) == 1:
    b1 = 'S'
  elif int(ship1[1]) == 2:
    b2 = 'S'
  elif int(ship1[1]) == 3:
    b3 = 'S'
  elif int(ship1[1]) == 4:
    b4 = 'S'
  elif int(ship1[1]) == 5:
    b5 = 'S'
elif ship1[0] == 'c':
  if int(ship1[1]) == 1:
    c1 = 'S'
  elif int(ship1[1]) == 2:
    c2 = 'S'
  elif int(ship1[1]) == 3:
    c3 = 'S'
  elif int(ship1[1]) == 4:
    c4 = 'S'
  elif int(ship1[1]) == 5:
    c5 = 'S'
elif ship1[0] == 'd':
  if int(ship1[1]) == 1:
    d1 = 'S'
  elif int(ship1[1]) == 2:
    d2 = 'S'
  elif int(ship1[1]) == 3:
    d3 = 'S'
  elif int(ship1[1]) == 4:
    d4 = 'S'
  elif int(ship1[1]) == 5:
    d5 = 'S'
elif ship1[0] == 'e':
  if int(ship1[1]) == 1:
    e1 = 'S'
  elif int(ship1[1]) == 2:
    e2 = 'S'
  elif int(ship1[1]) == 3:
    e3 = 'S'
  elif int(ship1[1]) == 4:
    e4 = 'S'
  elif int(ship1[1]) == 5:
    e5 = 'S'


cboard0 = """
   a  b  c  d  e\n"""
cboard1 = "1  " +c_a1+t+c_b1+t+c_c1+t+c_d1+t+c_e1+"\n"
cboard2 = "2  " +c_a2+t+c_b2+t+c_c2+t+c_d2+t+c_e2+"\n"
cboard3 = "3  " +c_a3+t+c_b3+t+c_c3+t+c_d3+t+c_e3+"\n"
cboard4 = "4  " +c_a4+t+c_b4+t+c_c4+t+c_d4+t+c_e4+"\n"
cboard5 = "5  " +c_a5+t+c_b5+t+c_c5+t+c_d5+t+c_e5+"\n"
cboard = cboard0 + cboard1 + cboard2 + cboard3 + cboard4 + cboard5

board0 = """
   a  b  c  d  e\n"""
board1 = "1  " +a1+t+b1+t+c1+t+d1+t+e1+"\n"
board2 = "2  "+a2+t+b2+t+c2+t+d2+t+e2+"\n"
board3 = "3  "+a3+t+b3+t+c3+t+d3+t+e3+"\n"
board4 = "4  "+a4+t+b4+t+c4+t+d4+t+e4+"\n"
board5 = "5  "+a5+t+b5+t+c5+t+d5+t+e5+"\n"
board = board0 + board1 + board2 + board3 + board4 + board5

print(board)
ship2 = input("Where would you like to place your second battleship?\n")


if ship2 == ship1:
  print(t)
  input("You already placed a ship there. Try again.")
  time.sleep(0.5)
  ship2 = input("Where would you like to place your second battleship?\n")

ship2 = ship2.strip(' ').lower()

if ship2[0] == 'a':
  if int(ship2[1]) == 1:
    a1 = 'S'
  elif int(ship2[1]) == 2:
    a2 = 'S'
  elif int(ship2[1]) == 3:
    a3 = 'S'
  elif int(ship2[1]) == 4:
    a4 = 'S'
  elif int(ship2[1]) == 5:
    a5 = 'S'
elif ship2[0] == 'b':
  if int(ship2[1]) == 1:
    b1 = 'S'
  elif int(ship2[1]) == 2:
    b2 = 'S'
  elif int(ship2[1]) == 3:
    b3 = 'S'
  elif int(ship2[1]) == 4:
    b4 = 'S'
  elif int(ship2[1]) == 5:
    b5 = 'S'
elif ship2[0] == 'c':
  if int(ship2[1]) == 1:
    c1 = 'S'
  elif int(ship2[1]) == 2:
    c2 = 'S'
  elif int(ship2[1]) == 3:
    c3 = 'S'
  elif int(ship2[1]) == 4:
    c4 = 'S'
  elif int(ship2[1]) == 5:
    c5 = 'S'
elif ship2[0] == 'd':
  if int(ship2[1]) == 1:
    d1 = 'S'
  elif int(ship2[1]) == 2:
    d2 = 'S'
  elif int(ship2[1]) == 3:
    d3 = 'S'
  elif int(ship2[1]) == 4:
    d4 = 'S'
  elif int(ship2[1]) == 5:
    d5 = 'S'
elif ship2[0] == 'e':
  if int(ship2[1]) == 1:
    e1 = 'S'
  elif int(ship2[1]) == 2:
    e2 = 'S'
  elif int(ship2[1]) == 3:
    e3 = 'S'
  elif int(ship2[1]) == 4:
    e4 = 'S'
  elif int(ship2[1]) == 5:
    e5 = 'S'

board0 = """
   a  b  c  d  e\n"""
board1 = "1  "+a1+t+b1+t+c1+t+d1+t+e1+"\n"
board2 = "2  "+a2+t+b2+t+c2+t+d2+t+e2+"\n"
board3 = "3  "+a3+t+b3+t+c3+t+d3+t+e3+"\n"
board4 = "4  "+a4+t+b4+t+c4+t+d4+t+e4+"\n"
board5 = "5  "+a5+t+b5+t+c5+t+d5+t+e5+"\n"
board = board0 + board1 + board2 + board3 + board4 + board5

print(board)

ship3 = input("Where would you like to place your third battleship?\n")

if ship3 == ship2:
  print(t)
  input("You already placed a ship there. Try again.")
  time.sleep(0.5)
  ship3 = input("Where would you like to place your third battleship?\n")
elif ship3 == ship1:
  print(t)
  input("You already placed a ship there. Try again.")
  time.sleep(0.5)
  ship3 = input("Where would you like to place your third battleship?\n")


ship3 = ship3.strip("").lower()

if ship3[0] == 'a':
  if int(ship3[1]) == 1:
    a1 = 'S'
  elif int(ship3[1]) == 2:
    a2 = 'S'
  elif int(ship3[1]) == 3:
    a3 = 'S'
  elif int(ship3[1]) == 4:
    a4 = 'S'
  elif int(ship3[1]) == 5:
    a5 = 'S'
elif ship3[0] == 'b':
  if int(ship3[1]) == 1:
    b1 = 'S'
  elif int(ship3[1]) == 2:
    b2 = 'S'
  elif int(ship3[1]) == 3:
    b3 = 'S'
  elif int(ship3[1]) == 4:
    b4 = 'S'
  elif int(ship3[1]) == 5:
    b5 = 'S'
elif ship3[0] == 'c':
  if int(ship3[1]) == 1:
    c1 = 'S'
  elif int(ship3[1]) == 2:
    c2 = 'S'
  elif int(ship3[1]) == 3:
    c3 = 'S'
  elif int(ship3[1]) == 4:
    c4 = 'S'
  elif int(ship3[1]) == 5:
    c5 = 'S'
elif ship3[0] == 'd':
  if int(ship3[1]) == 1:
    d1 = 'S'
  elif int(ship3[1]) == 2:
    d2 = 'S'
  elif int(ship3[1]) == 3:
    d3 = 'S'
  elif int(ship3[1]) == 4:
    d4 = 'S'
  elif int(ship3[1]) == 5:
    d5 = 'S'
elif ship3[0] == 'e':
  if int(ship3[1]) == 1:
    e1 = 'S'
  elif int(ship3[1]) == 2:
    e2 = 'S'
  elif int(ship3[1]) == 3:
    e3 = 'S'
  elif int(ship3[1]) == 4:
    e4 = 'S'
  elif int(ship3[1]) == 5:
    e5 = 'S'

board0 = """
   a  b  c  d  e\n"""
board1 = "1  " +a1+t+b1+t+c1+t+d1+t+e1+"\n"
board2 = "2  "+a2+t+b2+t+c2+t+d2+t+e2+"\n"
board3 = "3  "+a3+t+b3+t+c3+t+d3+t+e3+"\n"
board4 = "4  "+a4+t+b4+t+c4+t+d4+t+e4+"\n"
board5 = "5  "+a5+t+b5+t+c5+t+d5+t+e5+"\n"
board = board0 + board1 + board2 + board3 + board4 + board5

print(board)
print("Ok. These are where your ships are. They are at "+ship1.title()+", "+ship2.title()+", and "+ship3.title()+".")
print(t)



cspot = ["a1","a2","a3","a4","a5","b1","b2","b3","b4","b5","c1","c2","c3","c4","c5","d1","d2","d3","d4","d5","e1","e2","e3","e4","e5"]
cs_left = 3
ps_left = 3
cship1 = random.choice(cspot)
shuffle(cspot)
cspot.remove(cship1)
cship2 = random.choice(cspot)
shuffle(cspot)
cspot.remove(cship2)
cship3 = random.choice(cspot)
shuffle(cspot)
cspot.remove(cship3)
c_attack = random.choice(cspot)
shuffle(cspot)
cspot.append(cship1)
cspot.append(cship2)
cspot.append(cship3)
cships = [cship1, cship2, cship3]
p_atks = []
proxy = 0
input("The game will now begin. Press enter to continue.")
while cs_left > 0 and ps_left > 0:
  print(t)
  print(cboard)
  p_attack =input("Your move. Where would you like to attack?\n")
  print()
  p_attack = p_attack.strip(" ").lower()
  if p_attack == cship1:
    cs_left -= 1
    print('You found a ship! The ship was at '
    +p_attack.title() +  ". There are "+str(cs_left)+' ships left.')
    p_atks.append(p_attack)
    cships.remove(cship1)
    if cship1 == "a1":
      c_a1 = "O"
    elif cship1 == "a2":
      c_a2 = "O"
    elif cship1 == "a3":
      c_a3 = "O"
    elif cship1 == "a4":
      c_a4 = "O"
    elif cship1 == "a5":
      c_a5 = "O"
    elif cship1 == "b1":
      c_b1 = "O"
    elif cship1 == "b2":
      c_b2 = "O"
    elif cship1 == "b3":
      c_b3 = "O"
    elif cship1 == "b4":
      c_b4 = "O"
    elif cship1 == "b5":
      c_b5 = "O"
    elif cship1 == "c1":
      c_c1 = "O"
    elif cship1 == "c2":
      c_c2 = "O"
    elif cship1 == "c3":
      c_c3 = "O"
    elif cship1 == "c4":
      c_c4 = "O"
    elif cship1 == "c5":
      c_c5 = "O"
    elif cship1 == "d1":
      c_d1 = "O"
    elif cship1 == "d2":
      c_d2 = "O"
    elif cship1 == "d3":
      c_d3 = "O"
    elif cship1 == "d4":
      c_d4 = "O"
    elif cship1 == "d5":
      c_d5 = "O"
    elif cship1 == "e1":
      c_e1 = "O"
    elif cship1 == "e2":
      c_e2 = "O"
    elif cship1 == "e3":
      c_e3 = "O"
    elif cship1 == "e4":
      c_e4 = "O"
    elif cship1 == "e5":
      c_e5 = "O"

  elif p_attack == cship2:
    cs_left -= 1
    print('You found a ship! The ship was at '
    +p_attack.title() +  ". There are "+str(cs_left)+' ships left.')
    p_atks.append(p_attack)
    cships.remove(cship2)
    if cship2 == "a1":
      c_a1 = "O"
    elif cship2 == "a2":
      c_a2 = "O"
    elif cship2 == "a3":
      c_a3 = "O"
    elif cship2 == "a4":
      c_a4 = "O"
    elif cship2 == "a5":
      c_a5 = "O"
    elif cship2 == "b1":
      c_b1 = "O"
    elif cship2 == "b2":
      c_b2 = "O"
    elif cship2 == "b3":
      c_b3 = "O"
    elif cship2 == "b4":
      c_b4 = "O"
    elif cship2 == "b5":
      c_b5 = "O"
    elif cship2 == "c1":
      c_c1 = "O"
    elif cship2 == "c2":
      c_c2 = "O"
    elif cship2 == "c3":
      c_c3 = "O"
    elif cship2 == "c4":
      c_c4 = "O"
    elif cship2 == "c5":
      c_c5 = "O"
    elif cship2 == "d1":
      c_d1 = "O"
    elif cship2 == "d2":
      c_d2 = "O"
    elif cship2 == "d3":
      c_d3 = "O"
    elif cship2 == "d4":
      c_d4 = "O"
    elif cship2 == "d5":
      c_d5 = "O"
    elif cship2 == "e1":
      c_e1 = "O"
    elif cship2 == "e2":
      c_e2 = "O"
    elif cship2 == "e3":
      c_e3 = "O"
    elif cship2 == "e4":
      c_e4 = "O"
    elif cship2 == "e5":
      c_e5 = "O"
  elif p_attack == cship3:
    cs_left -= 1
    print('You found a ship! The ship was at '
    +p_attack.title() +  ". There are "+str(cs_left)+' ships left.')
    p_atks.append(p_attack)
    cships.remove(cship3)
    if cship3 == "a1":
      c_a1 = "O"
    elif cship3 == "a2":
      c_a2 = "O"
    elif cship3 == "a3":
      c_a3 = "O"
    elif cship3 == "a4":
      c_a4 = "O"
    elif cship3 == "a5":
      c_a5 = "O"
    elif cship3 == "b1":
      c_b1 = "O"
    elif cship3 == "b2":
      c_b2 = "O"
    elif cship3 == "b3":
      c_b3 = "O"
    elif cship3 == "b4":
      c_b4 = "O"
    elif cship3 == "b5":
      c_b5 = "O"
    elif cship3 == "c1":
      c_c1 = "O"
    elif cship3 == "c2":
      c_c2 = "O"
    elif cship3 == "c3":
      c_c3 = "O"
    elif cship3 == "c4":
      c_c4 = "O"
    elif cship3 == "c5":
      c_c5 = "O"
    elif cship3 == "d1":
      c_d1 = "O"
    elif cship3 == "d2":
      c_d2 = "O"
    elif cship3 == "d3":
      c_d3 = "O"
    elif cship3 == "d4":
      c_d4 = "O"
    elif cship3 == "d5":
      c_d5 = "O"
    elif cship3 == "e1":
      c_e1 = "O"
    elif cship3 == "e2":
      c_e2 = "O"
    elif cship3 == "e3":
      c_e3 = "O"
    elif cship3 == "e4":
      c_e4 = "O"
    elif cship3 == "e5":
      c_e5 = "O"
  else:
    print('You did not hit your target.')
    p_attack.split()
    if p_attack[0] == "a":
      if p_attack[1] == "1":
        c_a1 = "X"
      elif p_attack[1] == "2":
        c_a2 = "X"
      elif p_attack[1] == "3":
        c_a3 = "X"
      elif p_attack[1] == "4":
        c_a4 = "X"
      elif p_attack[1] == "5":
        c_a5 = "X"
      else:
        proxy += 1
    elif p_attack[0] == "b":
      if p_attack[1] == "1":
        c_b1 = "X"
      elif p_attack[1] == "2":
        c_b2 = "X"
      elif p_attack[1] == "3":
        c_b3 = "X"
      elif p_attack[1] == "4":
        c_b4 = "X"
      elif p_attack[1] == "5":
        c_b5 = "X"
      else:
        proxy += 1
    elif p_attack[0] == "c":
      if p_attack[1] == "1":
        c_c1 = "X"
      elif p_attack[1] == "2":
        c_c2 = "X"
      elif p_attack[1] == "3":
        c_c3 = "X"
      elif p_attack[1] == "4":
        c_c4 = "X"
      elif p_attack[1] == "5":
        c_c5 = "X"
      else:
        proxy += 1
    elif p_attack[0] == "d":
      if p_attack[1] == "1":
        c_d1 = "X"
      elif p_attack[1] == "2":
        c_d2 = "X"
      elif p_attack[1] == "3":
        c_d3 = "X"
      elif p_attack[1] == "4":
        c_d4 = "X"
      elif p_attack[1] == "5":
        c_d5 = "X"
      else:
        proxy += 1
    elif p_attack[0] == "e":
      if p_attack[1] == "1":
        c_e1 = "X"
      elif p_attack[1] == "2":
        c_e2 = "X"
      elif p_attack[1] == "3":
        c_e3 = "X"
      elif p_attack[1] == "4":
        c_e4 = "X"
      elif p_attack[1] == "5":
        c_e5 = "X"
      else:
        proxy += 1
    else:
      print("That isn't even on the board.\n")
  cboard0 = """
   a  b  c  d  e\n"""
  cboard1 = "1  " +c_a1+t+c_b1+t+c_c1+t+c_d1+t+c_e1+"\n"
  cboard2 = "2  " +c_a2+t+c_b2+t+c_c2+t+c_d2+t+c_e2+"\n"
  cboard3 = "3  " +c_a3+t+c_b3+t+c_c3+t+c_d3+t+c_e3+"\n"
  cboard4 = "4  " +c_a4+t+c_b4+t+c_c4+t+c_d4+t+c_e4+"\n"
  cboard5 = "5  " +c_a5+t+c_b5+t+c_c5+t+c_d5+t+c_e5+"\n"
  cboard = cboard0 + cboard1 + cboard2 + cboard3 + cboard4 + cboard5
  print(t)
  print("The opponent will now attack.")
  time.sleep(1)
  if c_attack == ship1:
    ps_left -= 1
    print("The enemy sunk your ship! The ship was found at "+ship1.title()+". You have "+str(ps_left)+" ships left.")
  elif c_attack == ship2:
    ps_left -= 1
    print("The enemy sunk your ship! The ship was found at "+ship2.title()+". You have "+str(ps_left)+" ships left.")
  elif c_attack == ship3:
    ps_left -= 1
    print("The enemy sunk your ship! The ship was found at "+ship3.title()+". You have "+str(ps_left)+" ships left.")
  else:
    print("The enemy missed.")
  shuffle(cspot)
  cspot.remove(c_attack)
  c_attack = random.choice(cspot)
if cs_left == 0 and ps_left > 0:
  print("You sunk all of their ships. You win!")
  quit()
elif cs_left > 0 and ps_left == 0:
  print("All of your ships were sunk. You lose!")
  quit()

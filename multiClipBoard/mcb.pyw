#!python3
#mcb.pyw - saves and loads pieces of text to the clipboard

#Usage: py.exe mcb.pyw save <keyword> - saves clpbrd to kw
#                   py.exe mcb.pw <<keyword> loads keyword to clipboard
#                   py.exe mcb.pyw list - loads all kw to clipboard

import shelve as sv
import pyperclip as pc
import sys

mcbShelf = sv.open('mcb') #creates a new file to store stuff in

#TODO: Save clipboard content
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pc.paste()
    elif sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]

elif len(sys.argv) == 2:

    #TODO: List keywords and load content
    if sys.argv[1].lower() == 'list':
        pc.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
    # elif sys.argv[1] in mcbShelf:
    #     pc.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()

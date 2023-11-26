'''
This module make

Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2022//
Ending 2022//

'''

import os
import sys
import inspect
from termcolor import cprint

# Text colors: grey red green yellow blue magenta cyan white
# Text highlights: on_grey on_red on_green on_yellow on_blue on_magenta on_cyan on_white
# Attributes: bold dark underline blink reverse concealed
# template --> cprint(f'{}' , 'red', attrs=['bold'])

# Shows which module is currently running
# cprint('='*20 + ' >> ' + inspect.stack()[0][0].f_code.co_name +
# ' << '+'='*20, 'red', attrs=['bold'])


NAME_PROJECT = '****** Your project name '
cprint(os.getcwd(), 'green')
path_prj = os.getcwd().split(NAME_PROJECT)[0] + NAME_PROJECT + '/'
cprint(path_prj, 'blue')
sys.path.append(path_prj)


def step1(name_file: str):
    '''AI is creating summary for prog1
    '''
    cprint('='*20 + ' >> ' + inspect.stack()[0][0].f_code.co_name +
           ' << '+'='*20, 'red', attrs=['bold'])
    with open(name_file, 'r', encoding="utf_8") as i_f:
        data_tex = i_f.read()
        list_link = data_tex.split('>>')
    for art in list_link:
        # cprint(art, 'red')
        dd = art.split(")")
        if len(dd) > 1:
            print(dd[0])
            a_l = dd[0].split('.')
            aut = dd[0][len(a_l[0]) + 1:].split(',')
            print(aut)
            cprint(dd[1], 'green')
        cprint('='*20, 'blue')
        print()


def prog2():
    '''AI is creating summary for prog2
    '''
    cprint('='*20 + ' >> ' + inspect.stack()[0][0].f_code.co_name +
           ' << '+'='*20, 'red', attrs=['bold'])


if __name__ == '__main__':
    NAME = '/home/al/Projects_My/bio_cell/doc/РИБОСОМА КАК АЛЛОСТЕРИЧЕСКИ ЛИтература.txt'
    step1(NAME)
    prog2()

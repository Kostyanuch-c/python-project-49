#!/usr/bin/env python3.10
import curses
from brain_games.enginy_curses import game_engine
from brain_games.games import calc, gcd, prime, progression, even

GAMES = {
    '49': even,
    '50': gcd,
    '51': calc,
    '52': prime,
    '53': progression,
}


def main():
    stdscr = curses.initscr()
    curses.cbreak()

    stdscr.border()
    welcome_win = curses.newwin(11, 11, curses.LINES // 2, curses.COLS // 2)
    welcome_win.addstr('May I have your name? ')
    name = welcome_win.getstr().decode()

    curses.noecho()
    help_win = curses.newwin(9, curses.COLS - 1, 10, 1)
    help_win.addstr(1, 1, "Help: ", curses.A_BOLD)
    help_win.addstr(2, 1, "q - quit")
    help_win.addstr(3, 1, "1 - brain-even")
    help_win.addstr(4, 1, "2 - brain-gcd")
    help_win.addstr(5, 1, "3 - brain-calc")
    help_win.addstr(6, 1, "4 - brain-prime")
    help_win.addstr(7, 1, "5 - brain-progression")
    help_win.bkgd('.')
    help_win.box()

    done = False
    while not done:
        curses.noecho()
        stdscr.addstr(1, 1, 'Welcome to the Brain Games!')
        stdscr.addstr(2, 1, f'hello, {name}!')

        stdscr.refresh()
        welcome_win.refresh()
        help_win.refresh()

        choise = stdscr.getch()
        curses.echo()
        if choise == ord('q') or choise == ord('й'):
            done = True
        else:
            game_module = GAMES.get(str(choise), None)
            if game_module:
                game_engine(game_module, name)

    curses.endwin()


if __name__ == '__main__':
    main()

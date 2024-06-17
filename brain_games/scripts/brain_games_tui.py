#!/usr/bin/env python3.10
import curses
from brain_games.enginy_curses import game_engine
from brain_games.games import calc, gcd, prime, progression, even
from brain_games.statistics import statistic

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
    help_win = curses.newwin(9, int(curses.COLS - 1), 12, 1)
    help_win.addstr(1, 1, "Help: ", curses.A_BOLD)
    help_win.addstr(2, 1, "q - quit")
    help_win.addstr(3, 1, "1 - brain-even")
    help_win.addstr(4, 1, "2 - brain-gcd")
    help_win.addstr(5, 1, "3 - brain-calc")
    help_win.addstr(6, 1, "4 - brain-prime")
    help_win.addstr(7, 1, "5 - brain-progression")
    help_win.bkgd('.')
    help_win.box()

    stat_win = curses.newwin(int(curses.LINES * 0.23),
                             int(curses.COLS * 0.3),
                             int(curses.LINES * 0),
                             int(curses.COLS * 0.25))
    stat_win.addstr(1, int(stat_win.getmaxyx()[1] * 0.3), 'Current statistics')

    stat_win.box()

    while True:
        stat_win.addstr(2, 1, f'brain-even: {statistic.get_stat_even()}')
        stat_win.addstr(3, 1, f'brain-gcd: {statistic.get_stat_gcd()}')
        stat_win.addstr(4, 1, f'brain-calc: {statistic.get_stat_calc()}')
        stat_win.addstr(5, 1, f'brain-prime: {statistic.get_stat_prime()}')
        stat_win.addstr(6, 1, f'brain-progression: '
                              f'{statistic.get_stat_progression()}')
        stat_win.addstr(7, 1, f'Total: {statistic.get_total_stat()[0]}')
        stat_win.addstr(8, 1, f'       {statistic.get_total_stat()[1]}')
        curses.noecho()
        stdscr.addstr(1, 1, 'Welcome to the Brain Games!')
        stdscr.addstr(2, 1, f'Hello, {name}! Choose a game!')

        stdscr.refresh()
        welcome_win.refresh()
        stat_win.refresh()
        help_win.refresh()

        choice_chr = stdscr.getch()
        curses.echo()
        if choice_chr == ord('q') or choice_chr == ord('й'):
            break
        else:
            game_module = GAMES.get(str(choice_chr), None)
            if game_module:
                result = game_engine(game_module, name)
                statistic.make_statistic(str(game_module).split()[1], result)

    curses.endwin()


if __name__ == '__main__':
    main()

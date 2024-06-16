CURRENT_GAMES_RESULTS = {
    'even': {'win': 0, 'lose': 0},
    'calc': {'win': 0, 'lose': 0},
    'gcd': {'win': 0, 'lose': 0},
    'prime': {'win': 0, 'lose': 0},
    'progression': {'win': 0, 'lose': 0},
}


def make_statistic(game_module: str, result: bool):
    if game_module.endswith(".even'"):
        add_result_game('even', result)
    elif game_module.endswith(".calc'"):
        add_result_game('calc', result)
    elif game_module.endswith(".gcd'"):
        add_result_game('gcd', result)
    elif game_module.endswith(".prime'"):
        add_result_game('prime', result)
    elif game_module.endswith(".progression'"):
        add_result_game('progression', result)


def add_result_game(key, result):
    if result:
        CURRENT_GAMES_RESULTS[key]['win'] += 1
    else:
        CURRENT_GAMES_RESULTS[key]['lose'] += 1


def get_stat_even():
    win_even = CURRENT_GAMES_RESULTS["even"]["win"]
    lose_even = CURRENT_GAMES_RESULTS["even"]["lose"]
    suma = win_even + lose_even
    if not suma:
        suma = 1
    percent = round(float(win_even / suma * 100), 2)
    return f'{win_even} / 'f'{lose_even}   {percent}%'


def get_stat_calc():
    win_calc = CURRENT_GAMES_RESULTS["calc"]["win"]
    lose_calc = CURRENT_GAMES_RESULTS["calc"]["lose"]
    suma = win_calc + lose_calc
    if not suma:
        suma = 1
    percent = round(float(win_calc / suma * 100), 2)
    return f'{win_calc} / 'f'{lose_calc}   {percent}%'


def get_stat_prime():
    win_prime = CURRENT_GAMES_RESULTS["prime"]["win"]
    lose_prime = CURRENT_GAMES_RESULTS["prime"]["lose"]
    suma = win_prime + lose_prime
    if not suma:
        suma = 1
    percent = round(float(win_prime / suma * 100), 2)
    return f'{win_prime} / 'f'{lose_prime}   {percent}%'


def get_stat_progression():
    win_progr = CURRENT_GAMES_RESULTS["progression"]["win"]
    lose_progr = CURRENT_GAMES_RESULTS["progression"]["lose"]
    suma = win_progr + lose_progr
    if not suma:
        suma = 1
    percent = round(float(win_progr / suma * 100), 2)
    return f'{win_progr} / 'f'{lose_progr}   {percent}%'


def get_stat_gcd():
    win_gcd = CURRENT_GAMES_RESULTS["gcd"]["win"]
    lose_gcd = CURRENT_GAMES_RESULTS["gcd"]["lose"]
    suma = win_gcd + lose_gcd
    if not suma:
        suma = 1
    percent = round(float(win_gcd / suma * 100), 2)
    return f'{win_gcd} / 'f'{lose_gcd}   {percent}%'


def get_total_stat():
    total_games = 0
    total_games_win = 0
    total_games_lose = 0
    for games_name, value in CURRENT_GAMES_RESULTS.items():
        win = value['win']
        lose = value['lose']
        suma = win + lose
        total_games += suma
        total_games_win += win
        total_games_lose += lose
    suma = total_games_win + total_games_lose
    if not suma:
        suma = 1
    percent = round(float(total_games_win / suma * 100), 2)

    return (f'number of games - {total_games}',
            f'{total_games_win} / 'f'{total_games_lose}'
            f' Win percentage: {percent}%  ')

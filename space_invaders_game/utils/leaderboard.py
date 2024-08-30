from .. import *

import pygame
from datetime import datetime
from json import load, dump


def load_leaderboard() -> list:
    """
    Загружает таблицу лидеров из файла

    Возвращает:
        Список записей таблицы лидеров. Если файл не найден, возвращает пустой список.
    """
    try:
        with open(LEADERBOARD_PATH, 'r') as file:
            return load(file)
    except FileNotFoundError:
        return []

def get_max_score() -> int:
    """
    Возвращает максимальный счёт из таблицы лидеров

    Возвращает:
        Максимальный счёт из таблицы лидеров. Если таблица пуста, возвращает 0.
    """
    leaderboard = load_leaderboard()
    return max(entry['score'] for entry in leaderboard) if leaderboard else 0

def update_leaderboard(current_score: int, current_level: int) -> None:
    """
    Добавляет переданную запись в таблицу лидеров, если это новый рекорд

    Аргументы:
        current_score (int): Счёт игрока
        current_level (int): Уровень, на котором остановился игрок
    """
    leaderboard = load_leaderboard()
    time = datetime.now().strftime("%H:%M, %d.%m")
    new_score = {
        "name": PLAYER_NAME_IN_LEADERBOARD,
        "time": time,
        "score": current_score,
        "level": current_level
    }
    leaderboard.append(new_score)
    leaderboard.sort(key=lambda x: x['score'], reverse=True)
    leaderboard = leaderboard[:3]

    with open(LEADERBOARD_PATH, 'w') as file:
        dump(leaderboard, file, indent=4)

def draw_leaderboard(screen: pygame.Surface) -> None:
    """
    Рисует таблицу лидеров на экране
    """
    leaderboard = load_leaderboard()
    font = pygame.font.Font(FONT_PATH, LEADERBOARD_FONT_SIZE)
    title_text = font.render("HIGH SCORES: ", True, LEADERBOARD_FONT_COLOR)
    screen.blit(title_text, ((SCREEN_WIDTH - title_text.get_width()) / 2, LEADERBOARD_START_POS_Y))

    pos_y = LEADERBOARD_START_POS_Y + 50
    for index, entry in enumerate(leaderboard):
        name = entry.get('name')
        time = entry.get('time')
        score = entry.get('score')
        level = entry.get('level')

        index_text = f"{index + 1:>1}."
        name_text = f"{name:>4}"
        time_text = f"({time})"
        score_text = f"{score:>5}"
        level_text = f"(level {level:>2})"
        record_text = f"{index_text} {name_text} {time_text} {score_text} {level_text}"

        text_surface = font.render(record_text, True, LEADERBOARD_FONT_COLOR)
        screen.blit(text_surface, ((GAME_AREA_WIDTH - text_surface.get_width() + OFFSET) / 2, pos_y))
        pos_y += 40

from .. import *

from pygame.font import Font
from datetime import datetime
from json import load, dump


def load_leaderboard():
    try:
        with open(LEADERBOARD_PATH, 'r') as file:
            return load(file)
    except FileNotFoundError:
        return []

def get_max_score():
    leaderboard = load_leaderboard()
    return max(entry['score'] for entry in leaderboard) if leaderboard else 0

def update_leaderboard(current_score, current_level):
    leaderboard = load_leaderboard()
    time = datetime.now().strftime("%H:%M, %d.%m")
    new_score = {"name": PLAYER_NAME_IN_LEADERBOARD, "time": time,"score": current_score, "level": current_level}
    leaderboard.append(new_score)
    leaderboard.sort(key=lambda x: x['score'], reverse=True)
    leaderboard = leaderboard[:3]

    with open(LEADERBOARD_PATH, 'w') as file:
        dump(leaderboard, file, indent=4)

def draw_leaderboard(screen):
    leaderboard = load_leaderboard()
    font = Font(FONT_PATH, LEADERBOARD_FONT_SIZE)
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
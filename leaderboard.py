from pygame.font import Font
from constants import *
from json import load, dump


def load_leaderboard():
    try:
        with open("leaderboard.json", 'r') as file:
            return load(file)
    except FileNotFoundError:
        return []

def get_max_score():
    leaderboard = load_leaderboard()
    return max(entry['score'] for entry in leaderboard) if leaderboard else 0

def update_leaderboard(current_score):
    leaderboard = load_leaderboard()

    new_score = {"name": "You", "score": current_score}
    leaderboard.append(new_score)
    leaderboard.sort(key=lambda x: x['score'], reverse=True)
    leaderboard = leaderboard[:3]

    with open("leaderboard.json", 'w') as file:
        dump(leaderboard, file, indent=4)

def draw_leaderboard(screen):
    leaderboard = load_leaderboard()
    font = Font('Assets/Font/monogram.ttf', 50)
    title_text = font.render("HIGH SCORES: ", True, (255, 255, 255))
    screen.blit(title_text, ((SCREEN_WIDTH - title_text.get_width() + OFFSET) / 2, 550))

    pos_y = 600
    for index, entry in enumerate(leaderboard):
        name = entry.get('name')
        score = entry.get('score')

        index_text = f"{index + 1:>1}."
        name_text = f"{name:>8}"
        score_text = f"{score:>6}"

        record_text = f"{index_text} {name_text} {score_text}"

        text_surface = font.render(record_text, True, (255, 255, 255))
        screen.blit(text_surface, ((SCREEN_WIDTH - text_surface.get_width() + OFFSET)/2, pos_y))
        pos_y += 40
TITLE = "Python Space Invaders"

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
GAME_AREA_WIDTH = 750
GAME_AREA_HEIGHT = 700
OFFSET = 50
LIVES_COUNT = 3

START_FPS = 45
GAME_MUSIC_VOLUME = 0.8

LEADERBOARD_FONT_SIZE = 46
LEADERBOARD_FONT_COLOR = (255, 255, 255)
LEADERBOARD_START_POS_Y = 550

GAME_OVER_FONT_SIZE = 80
GAME_INTERFACE_FONT_SIZE = 40
GREY = (29, 29, 27)
GREEN = (57, 255, 20)
BLUE = (4, 217, 255)
VIOLET = (188, 19, 254)
YELLOW = (255, 234, 25)
RED = (255, 7, 58)
LEVEL_COLORS = [BLUE, GREEN, VIOLET, RED, YELLOW]

OBSTACLE_GRID = [
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]]

LASER_HEIGHT = 15
LASER_WIDTH = 4
SHELTERS_OFFSET_Y = 100

BASIC_ALIEN_SCORE = 5
MYSTERY_SHIP_SCORE = 20
LEVEL_UP_SCORE = 10

ALIEN_SPEED = 2
ALIEN_FLEET_ROWS = 5
ALIEN_FLEET_COLUMNS = 11
ALIENS_LASER_SPEED = -12
MYSTERY_SHIP_SPEED = 6

PLAYER_SHIP_SPEED = 12
PLAYER_SHIP_SHOOT_DELAY = 300
PLAYER_SHIP_SHOT_SPEED = 12

MENU_BACKGROUND_IMAGE_PATH = "space_invaders_game/assets/graphics/UI/background.png"
START_BUTTON_IMAGE_PATH = "space_invaders_game/assets/graphics/UI/start_button.png"
FONT_PATH = "space_invaders_game/assets/font/monogram.ttf"
SHOOT_SOUND_PATH = "space_invaders_game/assets/audio/shoot.ogg"
EXPLOSION_SOUND_PATH = "space_invaders_game/assets/audio/explosion.ogg"

GAME_MUSIC_PATH = "space_invaders_game/assets/audio/game_music.mp3"
MENU_MUSIC_PATH = "space_invaders_game/assets/audio/menu_music.mp3"

PLAYER_SHIP_IMAGE_PATH = "space_invaders_game/assets/graphics/game_objects/player_ship.png"
MYSTERY_SHIP_IMAGE_PATH = "space_invaders_game/assets/graphics/game_objects/mystery_ship.png"

GAME_OVER_SOUND_PATH = "space_invaders_game/assets/audio/game_over.mp3"
LEVEL_UP_SOUND_PATH = "space_invaders_game/assets/audio/level_up.mp3"
GET_DAMAGE_SOUND_PATH = "space_invaders_game/assets/audio/get_damage.mp3"

LEADERBOARD_PATH = "space_invaders_game/leaderboard.json"

PLAYER_NAME_IN_LEADERBOARD = "You"
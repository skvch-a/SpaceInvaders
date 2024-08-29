TITLE = "Python Space Invaders"

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700
OFFSET = 50
LIVES_COUNT = 3

START_FPS = 60
GAME_MUSIC_VOLUME = 0.8

LEADERBOARD_FONT_SIZE = 46
LEADERBOARD_FONT_COLOR = (255, 255, 255)
LEADERBOARD_START_POS_Y = 550

GAME_INTERFACE_FONT_SIZE = 40
GREY = (29, 29, 27)
GREEN = (57, 255, 20)
BLUE = (4, 217, 255)
VIOLET = (188, 19, 254)
YELLOW = (255, 234, 25)
LEVEL_COLORS = [BLUE, GREEN, VIOLET, YELLOW]

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

BASIC_ALIEN_SCORE = 100
MYSTERY_SHIP_SCORE = 500

ALIEN_FLEET_ROWS = 5
ALIEN_FLEET_COLUMNS = 11
ALIENS_MOVE_DOWN_SPEED = 10
ALIENS_LASER_SPEED = -6

PLAYER_SHIP_SPEED = 6
PLAYER_SHIP_SHOOT_DELAY = 300
PLAYER_SHIP_SHOT_SPEED = 5

MENU_BACKGROUND_IMAGE_PATH = "Assets/Graphics/UI/Background.png"
START_BUTTON_IMAGE_PATH = "Assets/Graphics/UI/StartButton.png"
FONT_PATH = "Assets/Font/monogram.ttf"
SHOOT_SOUND_PATH = "Assets/Audio/shoot.ogg"
EXPLOSION_SOUND_PATH = "Assets/Audio/explosion.ogg"
GAME_MUSIC_PATH = "Assets/Audio/game_music.mp3"
PLAYER_SHIP_IMAGE_PATH = "Assets/Graphics/GameObjects/player_ship.png"
MYSTERY_SHIP_IMAGE_PATH = "Assets/Graphics/GameObjects/mystery_ship.png"
GAME_OVER_SOUND_PATH = "Assets/Audio/game_over.mp3"

PLAYER_NAME_IN_LEADERBOARD = "You"
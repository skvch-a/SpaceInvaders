# Space Invaders
### Вариант классической аркадной игры

### Автор: Сакевич Алексей

### Запуск:
`python3 -m space_invaders_game`

### Требования:
- python (рекомендуется версия не ниже 3.8)
- pygame (рекомендуется версия 2.6.0)

### Управление:
- Стрелки влево/вправо - передвижение
- Пробел - стрельба
- ESC - выход в меню

### Особенности:
- лучшие попытки сохраняются в файле leaderboard.json и отображаются в меню.
- благодаря вынесенным в файл constants.py константам, можно легко экпериментировать с геймплеем, меняя баланс игры
- с каждый уровнем сложность возрастает, так как игра ускоряется
- в игре бесконечное количество уровней
- присутствует 5 вариантов цветового оформления уровня (бирюзовый, зеленый, фиолетовый, красный, желтый), они чередуются по ходу игры
- присутствуют 'бункеры' и 'mystery ship'
- в игре 3 типа пришельцев (не считая 'mystery ship')
- за попадание в разные типы пришельцев игрок получает разное количество очков
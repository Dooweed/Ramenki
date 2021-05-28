CONDITIONS = (
    ("editing", "Редактирование"),
    ("pending", "Ожидание"),
    ("published", "Опубликовано"),
)
MONTHS = ("января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря")
RESERVED_CATEGORIES = ("all", "archive")
ARTICLES_PER_PAGE = 11
MEDIA_PER_PAGE = 15
VIDEOS_PER_PAGE = 17
GALLERIES_PER_PAGE = 15

ARTICLE_DESCRIPTION_LENGTH = 200

ARCHIVING_DAYS_LIMIT = 60  # How many days should have passed to make article "Archived"

DEFAULT_ARTICLE_IMAGES = ('img/content/news-thumb-01.png',
                          'img/content/news-thumb-01.png',
                          'img/content/news-thumb-02.png',
                          'img/content/news-thumb-02.png',
                          'img/content/news-thumb-02.png',
                          'img/content/news-thumb-03.png',
                          'img/content/news-thumb-03.png',
                          'img/content/news-thumb-04.png',
                          'img/content/news-thumb-04.png',
                          'img/content/news-thumb-05.png',
                          'img/content/news-thumb-05.png',)  # News section

DEFAULT_MEDIA_IMAGES = ('img/content/media-thumb-01.png',
                        'img/content/media-thumb-02.png',
                        'img/content/media-thumb-03.png',
                        'img/content/media-thumb-04.png',
                        'img/content/media-thumb-05.jpg',
                        'img/content/media-thumb-06.jpg',
                        'img/content/media-thumb-07.jpg',
                        'img/content/media-thumb-08.jpg',
                        'img/content/media-thumb-04.png',
                        'img/content/media-thumb-05.jpg',
                        'img/content/media-thumb-06.jpg',
                        'img/content/media-thumb-02.png',
                        'img/content/media-thumb-01.png',
                        'img/content/media-thumb-04.png',
                        'img/content/media-thumb-03.png',
                        'img/content/media-thumb-04.png',
                        'img/content/media-thumb-03.png',
                        'img/content/media-thumb-08.jpg',
                        'img/content/media-thumb-04.png',
                        'img/content/media-thumb-05.jpg',
                        'img/content/media-thumb-06.jpg',
                        'img/content/media-thumb-02.png',
                        'img/content/media-thumb-01.png',
                        'img/content/media-thumb-04.png',)

NEWS_BLOCK_DEFAULT_ARTICLE_IMAGES = ('img/content/news-thumb-01.png',
                                     'img/content/news-thumb-01.png',
                                     'img/content/news-thumb-02.png',
                                     'img/content/news-thumb-02.png',)  # News block

POSITIONS = (
    ("head-president", "Президент клуба"),
    ("vice-president", "Вице-президент клуба"),
    ("judiciary", "Судейский корпус"),
    ("single-coach", "Инструктор"),
    ("coach-committee", "Тренерский комитет"),
    ("methodical-certification-committee", "Методический и аттестационный комитет"),
    ("physical-mass-committee", "Физкультурно-массовый комитет"),
    ("administration", "Администрация"),
    ("parental-committee", "Родительский комитет"),
)

KINDS_OF_SPORTS = (
    ("karate", "Каратэ"),
    ("taekwondo", "Тхэквондо"),
)

DANS = (
    (1, "1 дан"),
    (2, "2 дан"),
    (3, "3 дан"),
    (4, "4 дан"),
    (5, "5 дан"),
    (6, "6 дан"),
    (7, "7 дан"),
    (8, "8 дан"),
    (9, "9 дан"),
    (10, "10 дан"),
)

BRANCH_NUMBERS = (
    (0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10),
    (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20),
    (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30),
    (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40),
    (41, 41), (42, 42), (43, 43), (44, 44), (45, 45), (46, 46), (47, 47), (48, 48), (49, 49), (50, 50),
)

QUALIFICATION_TYPES = (("KU", "КЮ"), ("DAN", "Дан"))

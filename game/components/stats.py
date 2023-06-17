import pygame
from game.components.menu import Menu
from game.utils.constants import FONT_STYLE, ICON


class Stats:
    def __init__(self):
        self.best_scores = []
        self.score = 0
        self.highest_score = 0
        self.death_count = 0
        self.messages = ""

    def update_message(self):
        self.messages = f"Your score: {self.score}  Highest score: {self.highest_score}  Total deaths: {self.death_count}"
        return self.messages

    def update(self):
        self.best_scores.append(self.score) 
        self.highest_score = max(self.best_scores)
from dataclasses import dataclass
import pygame


@dataclass
class Settings:
    menu_width: int = 1024
    menu_height: int = 768
    width_game: int = 1920
    height_game: int = 1080
    text_size: int = 20
    text_style: str = 'Georgia'
    FPS: int = 60
    WIDTH: int = 600
    HEIGHT: int = 600
    WHITE: int = (255, 255, 255)
    BLACK: int = (0, 0, 0)
    RED: int = (255, 0, 0)
    GREEN: int = (0, 255, 0)
    BLUE: int = (0, 0, 255)
    YELLOW: int = (255, 255, 0)


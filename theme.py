from pathlib import Path

from manim import *

ROOT = Path(__file__).resolve().parent
RES = ROOT / "resources"

INK = "#222222"
MUTED = "#707579"
ACCENT = "#3390ec"
ACCENT_DEEP = "#2b5278"
RAIL = "#f4f4f5"
LINE = "#e6e8eb"
WASH = "#d7e4ee"
WHITE = "#ffffff"
GREEN = "#3d9a4a"
STOP = "#e53935"


class DemoScene(Scene):
    def setup(self):
        self.camera.background_color = WHITE


def words(text, size=28, color=INK):
    return Text(text, font_size=size, color=color, font="Helvetica")


def fit(text, size, max_width, color=INK):
    mob = words(text, size, color)
    if mob.width > max_width:
        mob.scale_to_fit_width(max_width)
    return mob


def caption(text):
    line = fit(text, 30, 12.4)
    line.to_edge(DOWN, buff=0.38)
    return line


def bubble(text, width=2.5, height=0.68):
    body = RoundedRectangle(
        corner_radius=0.14,
        width=width,
        height=height,
        fill_color=WASH,
        fill_opacity=1,
        stroke_color=LINE,
        stroke_width=2,
    )
    label = fit(text, 22, width - 0.28)
    label.move_to(body)
    return VGroup(body, label)


def agent_icon(mark, radius=0.42):
    dot = Circle(
        radius=radius,
        color=ACCENT,
        fill_color=ACCENT,
        fill_opacity=1,
        stroke_width=0,
    )
    tag = words(mark, 26, WHITE)
    tag.move_to(dot)
    return VGroup(dot, tag)


def termite(name, height=1.05, fill="#161616", stroke=None):
    sprite = ImageMobject(str(RES / f"{name}.bmp"))
    sprite.height = height
    card = RoundedRectangle(
        corner_radius=0.12,
        width=sprite.width + 0.28,
        height=sprite.height + 0.28,
        fill_color=fill,
        fill_opacity=1,
        stroke_color=stroke if stroke is not None else fill,
        stroke_width=1.5 if stroke is not None else 0,
    )
    sprite.move_to(card)
    return Group(card, sprite)


def role_token(sprite_name, title, height=1.0):
    icon = termite(sprite_name, height)
    name = fit(title, 20, 2.15)
    name.next_to(icon, DOWN, buff=0.12)
    return Group(icon, name)

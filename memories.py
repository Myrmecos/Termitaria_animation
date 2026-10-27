from theme import *


AGENTS = ["PI", "Collector", "Ideator", "Designer", "Reviewer"]
SPOTS = [
    LEFT * 4.35 + UP * 1.35,
    LEFT * 2.45 + UP * 1.15,
    LEFT * 4.75 + UP * 0.2,
    LEFT * 3.25 + UP * 0.1,
    LEFT * 1.85 + UP * 0.0,
    LEFT * 3.9 + DOWN * 1.0,
    LEFT * 2.25 + DOWN * 1.1,
]
LINKS = [
    (0, 1),
    (0, 2),
    (0, 3),
    (1, 4),
    (2, 3),
    (2, 5),
    (3, 4),
    (3, 5),
    (4, 6),
    (5, 6),
]


def spoken(lines):
    text = VGroup(*[words(line, 24) for line in lines]).arrange(DOWN, buff=0.08)
    text.to_edge(DOWN, buff=0.28)
    return text


def memory_row(names):
    icons = VGroup(*[database() for _ in names]).arrange(RIGHT, buff=1.15)
    row = VGroup()
    for icon, name in zip(icons, names):
        label = words(name, 16)
        label.next_to(icon, DOWN, buff=0.12)
        row.add(VGroup(icon, label))
    return row


def database():
    width = 0.58
    rim = 0.15
    step = 0.24
    layers = 3
    top = step * (layers - 1) / 2
    ellipses = []
    for index in range(layers):
        ell = Ellipse(
            width=width,
            height=rim,
            stroke_color=ACCENT_DEEP,
            stroke_width=2,
            fill_color=WHITE if index == 0 else WASH,
            fill_opacity=1,
        )
        ell.move_to(UP * (top - index * step))
        ellipses.append(ell)
    body = Rectangle(
        width=width,
        height=step * (layers - 1),
        fill_color=WASH,
        fill_opacity=1,
        stroke_width=0,
    )
    body.move_to((ellipses[0].get_center() + ellipses[-1].get_center()) / 2)
    left = Line(
        ellipses[0].get_center() + LEFT * width / 2,
        ellipses[-1].get_center() + LEFT * width / 2,
        color=ACCENT_DEEP,
        stroke_width=2,
    )
    right = Line(
        ellipses[0].get_center() + RIGHT * width / 2,
        ellipses[-1].get_center() + RIGHT * width / 2,
        color=ACCENT_DEEP,
        stroke_width=2,
    )
    icon = VGroup(body, left, right, *reversed(ellipses))
    icon.move_to(ORIGIN)
    return icon


class Memories(DemoScene):
    def construct(self):
        dots = VGroup(*[Dot(spot, radius=0.09, color=ACCENT) for spot in SPOTS])
        edges = VGroup(*[
            Line(dots[a].get_center(), dots[b].get_center(), color=ACCENT, stroke_width=2.5)
            for a, b in LINKS
        ])
        graph_name = words("Knowledge graph", 24, ACCENT_DEEP)
        graph_name.next_to(dots, UP, buff=0.28)
        title = caption("Projects also evolve over time.")
        self.play(FadeIn(title), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(dot, scale=0.4) for dot in dots], lag_ratio=0.15), run_time=1.2)
        self.play(LaggedStart(*[Create(edge) for edge in edges], lag_ratio=0.08), run_time=1.3)
        self.play(FadeIn(graph_name), run_time=0.35)
        self.wait(0.35)

        detail = spoken([
            "To keep track of previous information, Termitaria uses",
            "a shared knowledge graph to preserve project-level evidence and relationships,",
            "and agent-specific memory for each agent.",
        ])
        self.play(FadeOut(title), run_time=0.3)
        self.play(FadeIn(detail), run_time=0.3)

        row_one = memory_row(AGENTS[:3])
        row_two = memory_row(AGENTS[3:])
        row_two.move_to(row_one.get_center() + DOWN * 1.5)
        stores = VGroup(row_one, row_two)
        stores.move_to(RIGHT * 3.35 + UP * 0.15)
        memory_name = words("Agent memory", 24, ACCENT_DEEP)
        memory_name.next_to(stores, UP, buff=0.22)
        self.play(
            FadeIn(memory_name),
            LaggedStart(*[FadeIn(store, shift=LEFT * 0.15) for store in stores], lag_ratio=0.12),
            run_time=1.6,
        )
        self.wait(6.2)

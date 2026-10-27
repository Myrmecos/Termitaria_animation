from theme import *


FACTS = [
    "What is insulin?",
    "It lowers blood sugar",
    "A medical paper",
]
LINKS = ["answered by", "drawn from"]
NOTES = ["PI", "Collector", "Ideator", "Designer", "Reviewer"]
CHAIN_X = -3.55
CHAIN_Y = [1.55, 0.35, -0.85]


def fact_box(text):
    label = words(text, 18)
    body = RoundedRectangle(
        corner_radius=0.14,
        width=3.2,
        height=0.62,
        fill_color=WASH,
        fill_opacity=1,
        stroke_color=LINE,
        stroke_width=2,
    )
    label.move_to(body)
    return VGroup(body, label)


def notebook(title):
    cover = RoundedRectangle(
        corner_radius=0.08,
        width=1.55,
        height=0.95,
        fill_color=WHITE,
        fill_opacity=1,
        stroke_color=LINE,
        stroke_width=2,
    )
    spine = Rectangle(
        width=0.1,
        height=0.95,
        fill_color=ACCENT_DEEP,
        fill_opacity=1,
        stroke_width=0,
    )
    spine.align_to(cover, LEFT)
    spine.align_to(cover, UP)
    name = words(title, 16)
    name.move_to(cover.get_center() + RIGHT * 0.06)
    return VGroup(cover, spine, name)


class Memories(DemoScene):
    def construct(self):
        boxes = VGroup(*[fact_box(text) for text in FACTS]).arrange(DOWN, buff=0.28)
        boxes.move_to(UP * 0.35)
        title = caption("A project changes when new evidence shows up.")
        self.play(FadeIn(title), FadeIn(boxes[0]), run_time=0.8)
        self.wait(0.3)
        self.play(FadeIn(boxes[1]), run_time=0.4)
        self.wait(0.3)
        self.play(FadeIn(boxes[2]), run_time=0.4)
        self.wait(1.2)

        apart = caption("Termitaria keeps two memories apart.")
        self.play(FadeOut(title), run_time=0.3)
        self.play(FadeIn(apart), run_time=0.3)
        self.wait(2.0)

        graph_title = caption(
            "The knowledge graph holds the project's evidence and the links between facts."
        )
        self.play(FadeOut(apart), run_time=0.3)
        self.play(
            FadeIn(graph_title),
            *[boxes[i].animate.move_to(RIGHT * CHAIN_X + UP * CHAIN_Y[i]) for i in range(3)],
            run_time=1.6,
        )
        edges = VGroup()
        link_labels = VGroup()
        for i, name in enumerate(LINKS):
            edge = Line(
                boxes[i].get_bottom(),
                boxes[i + 1].get_top(),
                color=ACCENT,
                stroke_width=3,
            )
            label = words(name, 15, MUTED)
            label.next_to(edge, RIGHT, buff=0.14)
            edges.add(edge)
            link_labels.add(label)
        graph_name = words("Knowledge graph", 24, ACCENT_DEEP)
        graph_name.next_to(boxes, UP, buff=0.28)
        self.play(
            *[Create(edge) for edge in edges],
            FadeIn(link_labels),
            FadeIn(graph_name),
            run_time=1.2,
        )
        self.wait(2.2)

        books = VGroup(*[notebook(name) for name in NOTES]).arrange(DOWN, buff=0.14)
        books.move_to(RIGHT * 3.5 + UP * 0.15)
        books_title = caption(
            "Each agent keeps its own notebook: its role, its rules, and what it did last time."
        )
        self.play(FadeOut(graph_title), run_time=0.3)
        self.play(
            FadeIn(books_title),
            LaggedStart(*[FadeIn(book, shift=LEFT * 0.2) for book in books], lag_ratio=0.12),
            run_time=2.6,
        )
        self.wait(2.0)

        start = books[1].get_left() + LEFT * 0.7
        stop = books[4].get_left() + LEFT * 0.7
        arrow = Arrow(
            start,
            stop,
            color=MUTED,
            stroke_width=3,
            buff=0.0,
            max_tip_length_to_length_ratio=0.12,
        )
        bar = Line(UP * 0.28, DOWN * 0.28, color=STOP, stroke_width=6)
        bar.move_to(stop)
        private = words("private", 20, STOP)
        private.next_to(bar, LEFT, buff=0.12)
        private_title = caption("One agent cannot read another's notes.")
        self.play(FadeOut(books_title), run_time=0.3)
        self.play(
            FadeIn(private_title),
            GrowArrow(arrow),
            FadeIn(bar),
            FadeIn(private),
            run_time=1.6,
        )
        self.wait(3.9)

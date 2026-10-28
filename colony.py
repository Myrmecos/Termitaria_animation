from theme import *


ROLES = [
    ("reproductive", "Principal\nInvestigator"),
    ("worker", "Literature\nCollector"),
    ("worker", "Idea\nGenerator"),
    ("worker", "Experiment\nDesigner"),
    ("soldier", "Skeptical\nReviewer"),
]

STEPS = [
    "literature\ngap scan",
    "hypothesis",
    "experiment\ndesign",
    "method\nreview",
]

SPLIT = ["Gap scan", "Hypothesis", "Experiment", "Review"]


def user_box():
    body = RoundedRectangle(
        corner_radius=0.16,
        width=1.55,
        height=0.64,
        fill_color=ACCENT,
        fill_opacity=1,
        stroke_width=0,
    )
    label = words("User", 24, WHITE)
    label.move_to(body)
    return VGroup(body, label)


def task_chip(text):
    label = words(text, 15)
    body = RoundedRectangle(
        corner_radius=0.12,
        width=1.24,
        height=0.46,
        fill_color=WASH,
        fill_opacity=1,
        stroke_color=LINE,
        stroke_width=2,
    )
    label.move_to(body)
    return VGroup(body, label)


class Colony(DemoScene):
    def construct(self):
        surface = Line(LEFT * 5.8, RIGHT * 5.8, color=LINE, stroke_width=3)
        surface.move_to(UP * 2.35)
        user = user_box()
        user.next_to(surface, UP, buff=0.22)
        title = caption("Termitaria gives a complex project a team.")
        self.play(Create(surface), FadeIn(user), FadeIn(title), run_time=1.6)
        self.wait(1.2)

        tokens = Group()
        for sprite_name, title_text in ROLES:
            icon = termite(sprite_name, height=0.82, fill=WHITE, stroke=LINE)
            label = words(title_text, 16)
            label.next_to(icon, DOWN, buff=0.08)
            tokens.add(Group(icon, label))
        tokens.arrange(RIGHT, buff=0.28)
        tokens.next_to(surface, DOWN, buff=0.78)
        surface_title = caption("A user sets the direction from the surface.")
        self.play(FadeOut(title), run_time=0.3)
        self.play(FadeIn(surface_title), run_time=0.3)
        self.wait(2.4)
        team_title = caption("Beneath it, specialized agents carry out distinct responsibilities.")
        self.play(FadeOut(surface_title), run_time=0.3)
        self.play(
            FadeIn(team_title),
            LaggedStart(*[FadeIn(token, shift=UP * 0.25) for token in tokens], lag_ratio=0.16),
            run_time=4.0,
        )
        self.wait(0.35)

        task = task_chip("Research")
        task.next_to(user, DOWN, buff=0.06)
        pi_icon = tokens[0][0]
        self.play(FadeIn(task), run_time=0.25)
        self.play(task.animate.next_to(pi_icon, UP, buff=0.08), run_time=1.5)
        self.wait(0.35)

        parts = VGroup(*[task_chip(name) for name in SPLIT])
        for part in parts:
            part.move_to(task.get_center())
        self.add(parts)
        self.play(
            FadeOut(task),
            *[
                parts[i].animate.next_to(tokens[i + 1][0], UP, buff=0.08)
                for i in range(4)
            ],
            run_time=2.2,
        )
        self.wait(0.7)
        self.play(FadeOut(parts), run_time=0.4)

        dots = VGroup(*[Dot(radius=0.07, color=ACCENT) for _ in STEPS])
        dots.arrange(RIGHT, buff=2.15)
        labels = VGroup()
        for dot, name in zip(dots, STEPS):
            label = fit(name, 15, 2.05, MUTED)
            label.next_to(dot, DOWN, buff=0.1)
            labels.add(label)
        track = Line(dots[0].get_center(), dots[-1].get_center(), color=ACCENT, stroke_width=3)
        steps = VGroup(track, dots, labels)
        steps.next_to(tokens, DOWN, buff=0.28)
        plan_title = caption("Their work becomes shared project knowledge")
        self.play(FadeOut(team_title), run_time=0.35)
        self.play(
            FadeIn(plan_title),
            Create(track),
            LaggedStart(
                *[
                    AnimationGroup(FadeIn(dot, scale=0.4), FadeIn(label))
                    for dot, label in zip(dots, labels)
                ],
                lag_ratio=0.25,
            ),
            run_time=2.6,
        )
        self.replace_caption(plan_title, "rather than disappearing into one long chat.")
        self.wait(2.6)

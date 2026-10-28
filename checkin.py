from theme import *


STEPS = [
    "literature\ngap scan",
    "hypothesis",
    "experiment\ndesign",
    "method\nreview",
]
XS = [-4.9, -1.65, 1.65, 4.9]
STEP_Y = 0.55

# Later step, earlier step, label on the cut-in arrow.
CHECKS = [
    (3, 2, "Check"),
    (1, 0, "Clarify"),
    (2, 1, "Follow up"),
]


def user_box():
    body = RoundedRectangle(
        corner_radius=0.16,
        width=1.7,
        height=0.64,
        fill_color=ACCENT,
        fill_opacity=1,
        stroke_width=0,
    )
    label = words("User", 24, WHITE)
    label.move_to(body)
    return VGroup(body, label)


def note(text):
    label = words(text, 16)
    body = RoundedRectangle(
        corner_radius=0.1,
        width=1.5,
        height=0.42,
        fill_color=WASH,
        fill_opacity=1,
        stroke_color=LINE,
        stroke_width=2,
    )
    label.move_to(body)
    return VGroup(body, label)


class CheckIn(DemoScene):
    def construct(self):
        dots = VGroup(*[Dot(RIGHT * x + UP * STEP_Y, radius=0.1, color=ACCENT) for x in XS])
        labels = VGroup()
        for dot, name in zip(dots, STEPS):
            label = words(name, 16)
            label.next_to(dot, DOWN, buff=1.05)
            labels.add(label)
        forward = VGroup()
        for i in range(3):
            forward.add(
                Arrow(
                    dots[i].get_right(),
                    dots[i + 1].get_left(),
                    color=ACCENT,
                    stroke_width=3,
                    buff=0.08,
                    max_tip_length_to_length_ratio=0.08,
                )
            )
        title = caption("Complex work is rarely linear.")
        self.play(FadeIn(title), run_time=0.4)
        steps = []
        for index, (dot, label) in enumerate(zip(dots, labels)):
            anims = [FadeIn(dot), FadeIn(label)]
            if index:
                anims.append(GrowArrow(forward[index - 1]))
            steps.append(AnimationGroup(*anims))
        self.play(LaggedStart(*steps, lag_ratio=0.35), run_time=2.6)
        self.wait(1.3)

        detail = caption("Users may need to check a decision, clarify a direction,")
        self.play(FadeOut(title), run_time=0.3)
        self.play(FadeIn(detail), run_time=0.3)

        user = user_box()
        user.move_to(UP * 2.4)
        self.play(FadeIn(user), run_time=0.45)
        self.wait(0.25)

        for later, earlier, name in CHECKS:
            start = user.get_bottom()
            if later == 1:
                start = user.get_corner(DL) + RIGHT * 0.15
            elif later == 3:
                start = user.get_corner(DR) + LEFT * 0.15
            cut = Arrow(
                start,
                dots[later].get_top(),
                color=ACCENT_DEEP,
                stroke_width=3,
                buff=0.06,
                max_tip_length_to_length_ratio=0.06,
            )
            chip = note(name)
            chip.move_to(cut.point_from_proportion(0.42))
            back = CurvedArrow(
                dots[later].get_bottom() + DOWN * 0.06,
                dots[earlier].get_bottom() + DOWN * 0.06,
                angle=-1.8,
                color=ACCENT_DEEP,
                stroke_width=3,
            )
            self.play(GrowArrow(cut), FadeIn(chip), run_time=0.7)
            self.play(Create(back), run_time=0.7)
            self.wait(0.25)

        detail = self.replace_caption(detail, "or ask a specialist a follow-up question")
        self.wait(2.2)
        detail = self.replace_caption(detail, "without derailing the entire project.")
        self.wait(4.15)

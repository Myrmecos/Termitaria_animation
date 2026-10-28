from theme import *


JOBS = [
    "answer questions",
    "analyze problems",
    "propose a plan",
    "draft a report",
]

ANGLES = [-0.08, -0.03, 0.04, 0.09]
LABEL_SIZE = 22
BOX_WIDTH = 2.75
BOX_GAP = 0.32
ROW_Y = 2.15


def job_bubble(text):
    label = words(text, LABEL_SIZE)
    body = RoundedRectangle(
        corner_radius=0.14,
        width=BOX_WIDTH,
        height=0.7,
        fill_color=WASH,
        fill_opacity=1,
        stroke_color=LINE,
        stroke_width=2,
    )
    label.move_to(body)
    return VGroup(body, label)


def agent_sprite(name, height=1.35):
    icon = ImageMobject(str(RES / f"{name}.bmp"))
    icon.height = height
    return icon


def row_slot(count, index):
    step = BOX_WIDTH + BOX_GAP
    span = count * BOX_WIDTH + (count - 1) * BOX_GAP
    x = -span / 2 + BOX_WIDTH / 2 + index * step
    return RIGHT * x + UP * ROW_Y


class Problem(DemoScene):
    def construct(self):
        one = agent_sprite("agent0", height=1.55)
        one.move_to(UP * 0.05)
        title = caption("One agent can answer questions, analyze information,")
        self.play(FadeIn(one), FadeIn(title), run_time=0.9)
        self.wait(0.25)

        chips = VGroup(*[job_bubble(job) for job in JOBS])
        for index, chip in enumerate(chips):
            count = index + 1
            chip.move_to(row_slot(count, index))
            if index == 2:
                self.play(FadeOut(title), run_time=0.3)
                title = caption("propose a plan, or draft a report.")
                self.play(FadeIn(title), run_time=0.3)
            if index:
                self.play(
                    *[
                        chips[earlier].animate.move_to(row_slot(count, earlier))
                        for earlier in range(index)
                    ],
                    run_time=0.3,
                )
                self.play(FadeIn(chip), run_time=0.35)
                self.wait(0.4)
            else:
                self.play(FadeIn(chip), run_time=0.4)
                self.wait(0.45)

        many = caption("But complex projects require many of these jobs at once.")
        self.play(FadeOut(title), run_time=0.25)
        self.play(FadeIn(many), run_time=0.25)
        self.wait(0.7)

        pile = [
            one.get_center() + UP * 0.78 + LEFT * 0.15,
            one.get_center() + UP * 0.42 + RIGHT * 0.7,
            one.get_center() + DOWN * 0.4 + RIGHT * 0.85,
            one.get_center() + DOWN * 0.82 + LEFT * 0.1,
        ]
        self.play(
            *[chips[i].animate.move_to(pile[i]).rotate(ANGLES[i]) for i in range(4)],
            run_time=1.5,
        )
        self.wait(0.45)

        row_title = caption("Asking one agent to do everything in a single conversation")
        self.play(FadeOut(many), run_time=0.25)
        icons = Group(*[agent_sprite(f"agent{i}") for i in range(1, 5)])
        icons.arrange(RIGHT, buff=1.55)
        icons.move_to(DOWN * 1.05)
        self.play(
            FadeOut(one),
            FadeIn(row_title),
            FadeIn(icons),
            *[
                chips[i].animate.move_to(icons[i].get_center() + UP * 1.25).rotate(-ANGLES[i])
                for i in range(4)
            ],
            run_time=2.2,
        )
        row_title = self.replace_caption(
            row_title,
            "makes the work harder to steer, inspect, verify, and build upon.",
        )
        self.wait(4.05)

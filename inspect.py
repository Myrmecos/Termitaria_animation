from theme import *


ROLES = [
    ("reproductive", "Principal Investigator"),
    ("worker", "Literature Collector"),
    ("worker", "Idea Generator"),
    ("worker", "Experiment Designer"),
    ("soldier", "Skeptical Reviewer"),
]
AGENT_LINE = "The design is ready for review."
USER_LINE = "Does the method cite the source?"


def avatar(name):
    icon = ImageMobject(str(RES / f"{name}.bmp"))
    icon.height = 0.48
    return icon


def message(text, fill, color):
    label = words(text, 16, color)
    body = RoundedRectangle(
        corner_radius=0.12,
        width=label.width + 0.5,
        height=0.56,
        fill_color=fill,
        fill_opacity=1,
        stroke_width=0,
    )
    label.move_to(body)
    return VGroup(body, label)


def spoken(top, bottom):
    lines = VGroup(words(top, 26), words(bottom, 26)).arrange(DOWN, buff=0.08)
    lines.to_edge(DOWN, buff=0.28)
    return lines


def pointer():
    mark = Triangle(color=INK, fill_color=INK, fill_opacity=1, stroke_width=0)
    mark.scale(0.11)
    mark.rotate(PI / 2)
    return mark


class Inspect(DemoScene):
    def construct(self):
        panel = RoundedRectangle(
            corner_radius=0.16,
            width=12.6,
            height=5.35,
            fill_color=WHITE,
            fill_opacity=1,
            stroke_color=LINE,
            stroke_width=2,
        )
        panel.move_to(UP * 0.22)
        divider = Line(
            panel.get_left() + RIGHT * 4.55 + UP * 2.5,
            panel.get_left() + RIGHT * 4.55 + DOWN * 2.5,
            color=LINE,
            stroke_width=2,
        )
        heading = words("Chats", 22)
        heading.move_to(panel.get_corner(UL) + RIGHT * 1.15 + DOWN * 0.42)

        rows = Group()
        row_centers = []
        top = heading.get_bottom()[1] - 0.48
        for index, (sprite_name, title) in enumerate(ROLES):
            center = RIGHT * (panel.get_left()[0] + 2.35) + UP * (top - index * 0.82)
            row_centers.append(center)
            icon = avatar(sprite_name)
            icon.move_to(center + LEFT * 1.45)
            label = words(title, 16)
            label.next_to(icon, RIGHT, buff=0.16)
            rows.add(Group(icon, label))

        highlight = RoundedRectangle(
            corner_radius=0.1,
            width=4.15,
            height=0.7,
            fill_color=WASH,
            fill_opacity=0,
            stroke_width=0,
        )
        highlight.move_to(row_centers[4])

        prompt = words("Select a chat", 20, MUTED)
        prompt.move_to(panel.get_center() + RIGHT * 2.15)

        title = spoken(
            "In Termitaria, users can inspect the team's work",
            "and speak directly with individual agents.",
        )
        panel.set_z_index(0)
        highlight.set_z_index(1)
        for item in (divider, heading, prompt, title):
            item.set_z_index(2)
        for row in rows:
            row.set_z_index(2)
            for part in row:
                part.set_z_index(2)
        self.play(
            FadeIn(panel),
            FadeIn(divider),
            FadeIn(heading),
            LaggedStart(*[FadeIn(row) for row in rows], lag_ratio=0.12),
            FadeIn(prompt),
            FadeIn(title),
            run_time=1.4,
        )
        self.wait(0.25)

        cursor = pointer()
        cursor.set_z_index(3)
        cursor.move_to(row_centers[0] + RIGHT * 1.7)
        self.play(FadeIn(cursor), run_time=0.25)
        self.play(cursor.animate.move_to(row_centers[4] + RIGHT * 1.7), run_time=0.9)
        self.add(highlight)
        self.play(highlight.animate.set_fill(WASH, opacity=1), run_time=0.3)
        self.wait(0.15)

        header_icon = avatar("soldier")
        header_icon.move_to(divider.get_center() + RIGHT * 0.7 + UP * 2.05)
        header_name = words("Skeptical Reviewer", 20)
        header_name.next_to(header_icon, RIGHT, buff=0.16)
        header_state = words("online", 15, MUTED)
        header_state.next_to(header_name, DOWN, buff=0.04, aligned_edge=LEFT)
        rule = Line(
            divider.get_center() + RIGHT * 0.25 + UP * 1.55,
            panel.get_right() + LEFT * 0.3 + UP * 1.55,
            color=LINE,
            stroke_width=2,
        )
        agent = message(AGENT_LINE, WASH, INK)
        agent.next_to(rule, DOWN, buff=0.35)
        agent.align_to(rule, LEFT)
        composer = RoundedRectangle(
            corner_radius=0.12,
            width=7.2,
            height=0.58,
            fill_color=RAIL,
            fill_opacity=1,
            stroke_width=0,
        )
        composer.move_to(panel.get_corner(DR) + LEFT * 3.85 + UP * 0.55)
        hint = words("Message", 16, MUTED)
        hint.move_to(composer.get_center())

        self.play(
            FadeOut(prompt),
            FadeIn(header_icon),
            FadeIn(header_name),
            FadeIn(header_state),
            Create(rule),
            FadeIn(agent),
            FadeIn(composer),
            FadeIn(hint),
            run_time=0.9,
        )
        self.wait(0.3)

        typed = words(USER_LINE, 16, INK)
        typed.move_to(composer.get_center())
        self.play(FadeOut(hint), FadeIn(typed), run_time=0.5)
        self.wait(0.2)
        user = message(USER_LINE, ACCENT, WHITE)
        user.next_to(agent, DOWN, buff=0.28)
        user.align_to(composer, RIGHT)
        self.play(FadeOut(typed), FadeIn(user), run_time=0.55)
        self.wait(1.0)

        compare = spoken(
            "That is more like checking in with a specific teammate",
            "than interrupting a single all-purpose assistant.",
        )
        self.play(FadeOut(title), run_time=0.3)
        self.play(FadeIn(compare), run_time=0.3)
        self.wait(4.7)

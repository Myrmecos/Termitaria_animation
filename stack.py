from theme import *


LAYERS = [
    ("Client", "Next.js"),
    ("Control plane", "Go  ·  NATS JetStream"),
    ("Workers", "Python"),
    ("Inference", "Nebius Token Factory"),
]


def band(title, detail):
    box = RoundedRectangle(
        corner_radius=0.12,
        width=8.6,
        height=0.92,
        fill_color=RAIL,
        fill_opacity=1,
        stroke_color=LINE,
        stroke_width=2,
    )
    name = words(title, 26)
    sub = words(detail, 20, MUTED)
    text = VGroup(name, sub).arrange(RIGHT, buff=0.35)
    if text.width > 7.8:
        text.scale_to_fit_width(7.8)
    text.move_to(box)
    return VGroup(box, text)


def chip(title, model_id, tint):
    box = RoundedRectangle(
        corner_radius=0.1,
        width=4.3,
        height=1.05,
        fill_color=WHITE,
        fill_opacity=1,
        stroke_color=tint,
        stroke_width=3,
    )
    name = words(title, 22, tint)
    ident = fit(model_id, 15, 3.9, MUTED)
    text = VGroup(name, ident).arrange(DOWN, buff=0.08)
    text.move_to(box)
    return VGroup(box, text)


class Stack(DemoScene):
    def construct(self):
        title = caption("The app is the surface. Workers call the model.")
        layers = VGroup(*[band(name, detail) for name, detail in LAYERS])
        layers.arrange(DOWN, buff=0.14)
        layers.move_to(UP * 1.15)
        self.play(FadeIn(title), run_time=0.8)
        self.play(
            LaggedStart(*[FadeIn(layer, shift=UP * 0.15) for layer in layers], lag_ratio=0.25),
            run_time=7.4,
        )
        self.wait(0.4)

        super_chip = chip("Nemotron 3 Super", "nvidia/nemotron-3-super-120b-a12b", ACCENT)
        ultra_chip = chip("Nemotron 3 Ultra", "nvidia/Nemotron-3-Ultra-550b-a55b", ACCENT_DEEP)
        chips = VGroup(super_chip, ultra_chip).arrange(RIGHT, buff=0.4)
        chips.next_to(layers, DOWN, buff=0.35)
        model_title = caption("Everyday turns use Super. The review uses Ultra.")
        self.play(ReplacementTransform(title, model_title), FadeIn(chips), run_time=3.6)
        self.wait(0.4)

        worker = termite("worker", height=0.62)
        reviewer = termite("soldier", height=0.72)
        worker.next_to(super_chip, LEFT, buff=0.28)
        reviewer.next_to(ultra_chip, RIGHT, buff=0.28)
        to_super = Arrow(
            worker.get_right(),
            super_chip.get_left(),
            color=ACCENT,
            stroke_width=3,
            buff=0.08,
            max_tip_length_to_length_ratio=0.2,
        )
        to_ultra = Arrow(
            reviewer.get_left(),
            ultra_chip.get_right(),
            color=ACCENT_DEEP,
            stroke_width=3,
            buff=0.08,
            max_tip_length_to_length_ratio=0.2,
        )
        worker_name = words("other roles", 16, MUTED)
        worker_name.next_to(worker, DOWN, buff=0.08)
        reviewer_name = words("reviewer", 16, MUTED)
        reviewer_name.next_to(reviewer, DOWN, buff=0.08)
        self.play(
            FadeIn(worker),
            FadeIn(reviewer),
            GrowArrow(to_super),
            GrowArrow(to_ultra),
            FadeIn(worker_name),
            FadeIn(reviewer_name),
            run_time=3.8,
        )
        self.wait(5.6)

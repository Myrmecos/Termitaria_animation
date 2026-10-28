from theme import *


class Close(DemoScene):
    def construct(self):
        row_y = UP * 0.4
        worker = termite("worker", height=1.25, fill=WHITE, stroke=LINE)
        worker.move_to(row_y)
        reproductive = termite("reproductive", height=1.25, fill=WHITE, stroke=LINE)
        reproductive.move_to(LEFT * 2.45 + row_y)
        soldier = termite("soldier", height=1.25, fill=WHITE, stroke=LINE)
        soldier.move_to(RIGHT * 2.45 + row_y)

        line = caption("Like a termite colony, no single member holds the whole plan.")
        self.play(FadeIn(worker), FadeIn(line), run_time=0.7)
        self.wait(2.8)

        detail = caption("Specialized members contribute their own work,")
        self.play(FadeOut(line), run_time=0.3)
        self.play(FadeIn(detail), run_time=0.3)
        self.play(
            LaggedStart(
                FadeIn(reproductive, target_position=worker),
                FadeIn(soldier, target_position=worker),
                lag_ratio=0.35,
            ),
            run_time=1.5,
        )
        detail = self.replace_caption(detail, "preserve what they learn,")
        self.wait(0.8)
        detail = self.replace_caption(detail, "and coordinate to build something larger.")
        self.wait(1.2)

        ending = caption("That is why we call it Termitaria.")
        self.play(FadeOut(detail), run_time=0.3)
        self.play(FadeIn(ending), run_time=0.3)
        self.play(FadeOut(reproductive), FadeOut(worker), FadeOut(soldier), run_time=0.45)
        hero = termite("soldier", height=1.85, fill=WHITE, stroke=LINE)
        hero.move_to(UP * 0.85)
        name = words("Termitaria", 52)
        name.next_to(hero, DOWN, buff=0.32)
        self.play(FadeIn(hero), run_time=0.55)
        self.play(FadeIn(name), run_time=0.45)
        self.wait(2.15)

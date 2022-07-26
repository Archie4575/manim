from manim import *
from random import randint
from manim.utils.rate_functions import ease_in_expo
from math import floor

class DiceRollBarGraph(Scene):
    cache = { str(i): 0 for i in range(1,7) }
    trials = 0
    def tally(self, n: int):
        while n > self.trials:
            self.cache[str(randint(1,6))] += 1
            self.trials += 1
        return self.cache

    def construct(self):
        n = ValueTracker(1)
        s = ValueTracker(1)
        graph = always_redraw(
                lambda: BarChart(list(self.tally(n.get_value()).values()), 
                    max_value=(floor(int(s.get_value())/5))+5,
                    bar_names=list(self.cache.keys()),
                    label_y_axis=False
                    )
                )

        label = always_redraw(lambda: Tex(f"n={int(n.get_value())}"))
        label.add_updater(lambda m: m.next_to(graph, UP))

        self.add(graph)
        self.play(Write(label))
        self.wait()
        for i in range(6):
            self.play(n.animate().set_value(n.get_value()*10), s.animate.set_value(s.get_value()*10), run_time=2)
        self.wait()

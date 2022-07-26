from manim import *
from math import sqrt

class QuadraticGraph3D(ThreeDScene):
    def func(self, x, y):
        return [x, y, (x**2 - y**2 + 2)]

    def construct(self):
        ylen = ValueTracker(0.01)
        yrange = ValueTracker(0)

        ax = always_redraw(
            lambda: ThreeDAxes(
                x_range = (-5,5),
                x_length = 8,
                z_range = (-5,5),
                y_length = ylen.get_value(),
                tips = True,
            )
        )
        ax.y_axis.add_labels({-yrange.get_value(): Tex("Im(x)")})
        ax.z_axis.add_labels({5 : Tex("Re(y)")})
        ax.x_axis.add_labels({3 : Tex("Re(x)")})

        surface = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(*self.func(u, v)),
                u_range=[-2.5, 2.5],
                v_range=[-yrange.get_value(), yrange.get_value()],
                color=
            )
        )
    
        print(ax.__dict__)
        self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES)
        self.add(ax, surface)
        self.wait()
        self.move_camera(phi = 80 * DEGREES, theta = -60 * DEGREES)
        self.wait()
        self.play(ylen.animate().set_value(10.5))
        self.wait()
        self.play(yrange.animate().set_value(sqrt(2)))
        self.wait()

from manim import *
import logging


class BinaryBox(VGroup):
    def __init__(self):
        VGroup.__init__(self)
        self.box = Square()
        self.value = 1
        self.text = Integer(self.value)
        self.text.font_size = 200
        self.add(self.box)
        self.add(self.text)

    def change_state(self, value=None):
        if not value:
            self.value = 1 - self.value
        else:
            self.value = value
        nt = Integer(self.value)
        nt.font_size = self.text.font_size
        nt.move_to(self.box)
        rt = ReplacementTransform(self.text, nt,)
        self.text = nt
        return rt


class BinaryBoxes(VGroup):
    def __init__(self, nbits):
        VGroup.__init__(self)
        self.nbits = nbits
        self.build_boxes()

    def build_boxes(self):
        self.bb = BinaryBox()
        self.boxes = [self.bb]
        self.add(self.bb)
        for i in range(self.nbits-1):
            self._add_box()
        self.move_to(self.bb)

    def _add_box(self):
        bbx = BinaryBox().match_dim_size(self.bb, 0).next_to(
            self.boxes[-1], LEFT, buff=0)
        self.boxes.append(bbx)
        self.add(bbx)
        return bbx

    def add_box(self):
        self.nbits += 1
        return FadeIn(self._add_box(), lag_ratio=0.1)


class SquareToCircle(Scene):
    def construct(self):

        bb = BinaryBoxes(6)  # create a square
        self.play(FadeIn(bb, lag_ratio=0.1))  # fade out animation
        self.play(bb.animate.scale(0.3))
        rt = bb.boxes[0].change_state()
        self.play(rt)
        self.play(bb.animate.scale(2))
        self.play(bb.add_box())
        rt = bb.boxes[0].change_state()
        self.play(rt)
        self.play(FadeOut(bb))  # fade out animation

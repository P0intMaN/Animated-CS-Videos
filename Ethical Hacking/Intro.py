from manimlib.imports import *
import random


class Intro(Scene):
    def construct(self):
        title = TextMobject("Hacker's Methodology").scale(2.5).move_to(ORIGIN).set_color(DARK_BLUE)
        self.play(DrawBorderThenFill(title))
        self.wait(2)

        self.play(title.scale,0.5)
        self.wait()

        encrpt = VGroup(*[Dot() for i in range(36)]).arrange_in_grid(6,6,buff=SMALL_BUFF)
        encrpt.move_to(2*UP)
        encrpt.set_color(RED)
        self.play(ShowCreation(encrpt))
        for i in range(5):
            t1 =  random.randint(0,35)
            t2 =  random.randint(0,35)
            t3 =  random.randint(0,35)
            self.play(encrpt[t1].set_color,YELLOW,encrpt[t2].set_color,YELLOW,encrpt[t3].set_color,YELLOW,run_time=0.1)
            self.play(encrpt[t1].set_color,RED,encrpt[t2].set_color,RED,encrpt[t3].set_color,RED,run_time=0.1)
        s = TextMobject("success!").next_to(encrpt,RIGHT,buff=MED_LARGE_BUFF).set_color(GREEN).scale(0.8)
        self.play(encrpt[14].set_color,GREEN,encrpt[15].set_color,GREEN,encrpt[16].set_color,GREEN,FadeInFrom(s,2*LEFT),run_time=0.1)
        self.wait()
        
        lap = SpeechBubble(direction=RIGHT)
        self.play(ShowCreation(lap))
        self.wait()

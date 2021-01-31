from numpy.core.numeric import indices
from manimlib.imports import *

class Introduction(Scene):
    def construct(self):
        width = (475 / 1280) * FRAME_WIDTH
        height = width * (323 / 575)
        video_rect = Rectangle(
            width=width,
            height=height,
            fill_color=BLACK,
            fill_opacity=1,
        )
        video_rect.shift(0.8*UP)
        title = TextMobject("Previously...").next_to(video_rect,DOWN,buff=MED_LARGE_BUFF)
        t = AnimatedBoundary(video_rect)
        self.add(t)
        self.wait(2)
        self.play(FadeIn(title))
        self.wait(5)

        self.play(FadeOut(t))
        printtex = TexMobject("print()").scale(1.5).move_to(ORIGIN).set_color(ORANGE)
        self.play(ReplacementTransform(title,printtex))
        self.wait(2)

        self.play(ApplyMethod(printtex.to_edge,UP))
        titleun = Underline(printtex,buff=0.2)
        self.play(Write(titleun))

        title = VGroup(titleun,printtex)
        printpara = Text("used to display the output to the screen or terminal.")
        printpara.next_to(titleun,2.5*DOWN).scale(0.7).set_color(YELLOW)
        self.play(Write(printpara),rate_fun=rush_into)
        self.wait()

        pr = TexMobject("\\texttt{print}","\\texttt{(}","\\texttt{)}").set_color_by_tex("print",DARK_BLUE)
        self.play(Write(pr),run_time=2)
        self.wait()
        anything = TexMobject("\\texttt{`hello, world' }").scale(0.7).set_color(GOLD)
        anything.next_to(pr[1],RIGHT)
        self.play(Indicate(pr[1],color=RED),Indicate(pr[2],color=RED))
        self.play(pr[2].next_to,anything,RIGHT,FadeIn(anything))
        self.wait(2)
        self.play(FadeOut(anything),FadeOutAndShift(pr,2*RIGHT),FadeOutAndShift(title,2*LEFT),FadeOutAndShift(printpara,2*UP))
        self.wait()







        

        

        

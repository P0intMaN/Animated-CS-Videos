from os import write
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
        
        soceng1 = VGroup(
            TextMobject("Hello Sir,"),
            TextMobject("I am from the Security Department"),
            TextMobject("I would like to know your account and pswd"),
            TextMobject("for verification purposes."),
        ).arrange(DOWN,buff=0.2).set_color(ORANGE)

        soceng2 = VGroup(
            TextMobject("Sure..."),
            TextMobject("Username is AlphaRomeo"),
            TextMobject("Pswd is Awlled123")
        ).arrange(DOWN,buff=0.2).set_color(YELLOW)

        soceng1.move_to(1.5*LEFT+1.5*DOWN).scale(0.5)
        self.play(FadeInFrom(soceng1,3*DOWN),WiggleOutThenIn(soceng1,run_time=2))
        
        soceng2.move_to(3*RIGHT+1.5*DOWN).scale(0.5)
        self.play(FadeInFrom(soceng2,3*RIGHT))
        self.wait(4)

        self.play(FadeOutAndShift(soceng1,2*DOWN),FadeOutAndShift(soceng2,2*DOWN),FadeOutAndShift(title,3*RIGHT),FadeOutAndShift(s,2*UP),FadeOutAndShift(encrpt,2*UP))
        self.wait()

class Steps(Scene):
    def construct(self):
        rec  = TextMobject("Reconnaisance").scale(1)
        scan = TextMobject("Scanning").scale(1.3).set_color(YELLOW)
        exp  = TextMobject("Exploitation").scale(2).set_color(RED)
        pers = TextMobject("Persistance").scale(1.3).set_color(BLUE)
        cov  = TextMobject("Covering your tracks").scale(1).set_color(GREEN)

        rrec  = rec.to_corner(UL)
        eexp  = exp.move_to(3*UP+1.5*RIGHT)
        sscan = scan.move_to(3.5*LEFT)
        ppers = pers.move_to(0.5*UP+4*RIGHT)
        ccov  = cov.move_to(2*DOWN)

        a1 = arrow1  = Arrow(rec.get_bottom(),scan.get_corner(UL),max_tip_length_to_length_ratio=0,max_stroke_width_to_length_ratio=3.8).set_color_by_gradient(PURPLE,BLUE)
        a2 = arrow2  = Arrow(scan.get_right(),exp.get_corner(DL),max_tip_length_to_length_ratio=0,max_stroke_width_to_length_ratio=3.8).set_color_by_gradient(PURPLE,BLUE)
        a3 = arrow3  = Arrow(exp.get_corner(DR),pers.get_top(),max_tip_length_to_length_ratio=0,max_stroke_width_to_length_ratio=3.8).set_color_by_gradient(PURPLE,BLUE)
        a4 = arrow4  = Arrow(pers.get_corner(DL),cov.get_top(),max_tip_length_to_length_ratio=0,max_stroke_width_to_length_ratio=3.8).set_color_by_gradient(PURPLE,BLUE)

        
        self.play(Write(rec))
        self.play(ShowCreation(arrow1),run_time=0.5)
        self.play(Write(scan))
        self.play(ShowCreation(arrow2),run_time=0.5)
        self.play(Write(exp))
        self.play(ShowCreation(arrow3),run_time=0.5)
        self.play(Write(pers))
        self.play(ShowCreation(arrow4),run_time=0.5)
        self.play(Write(cov),run_time=0.9)
        self.wait()
        
        mindtree = VGroup(rrec,sscan,ppers,eexp,ccov,a1,a2,a3,a4)
        reco = mindtree[0].copy()

        self.play(mindtree.set_opacity,0.1,reco.set_opacity,1,reco.move_to,ORIGIN,reco.scale,1.5)
        self.wait()
        self.play(reco.to_edge,UP)
        for i in range(0,9):
            self.play(FadeOut(mindtree[i]),run_time=0.01)
        self.wait()

        box = VGroup(
            Line(ORIGIN,3*RIGHT,color =DARK_BLUE),
            Line(3*RIGHT,3*UR,color   =DARK_BLUE),
            Line(3*UR,3*UP,color      =DARK_BLUE),
            Line(3*UP,ORIGIN,color    =DARK_BLUE)
        )

        bar = Line(ORIGIN,2.5*LEFT,color = BLACK)
        bar.move_to(2*LEFT,0.25*UP)

        options = VGroup(*[Dot() for i in range(3)]).arrange(RIGHT,buff=0.1)
        options[0].set_color(GREEN)
        options[1].set_color(YELLOW)
        options[2].set_color(RED)
        options.next_to(bar,0.2*UP).shift(1*RIGHT+0.13*UP)

        box.move_to(2*LEFT).shift(DOWN)

        lines = VGroup(*[Line(ORIGIN,2*LEFT,color= GREEN) for i in range(5)]).arrange(DOWN,aligned_edge = LEFT,buff=0.35)
        lines.move_to(2*LEFT+1*DOWN)

        toolbox = VGroup(options,box,lines)
        toolbox.shift(1*UP)

        self.play(ShowCreation(toolbox))
        self.wait()

        ellipse=Ellipse(width=5, height=2.5, color=DARK_BLUE).scale(1.2)
        eyeball = Annulus(inner_radius=0.6, outer_radius=1, color=BLUE).scale(1.2)
        eyem = Annulus(inner_radius=0.2, outer_radius=1, color=BLUE).scale(1.2)

        self.play(toolbox.set_opacity,0.1,reco.set_opacity,0.1,ShowCreation(ellipse),ShowCreation(eyem))
        self.play(eyeball.move_to,ORIGIN,ReplacementTransform(eyem,eyeball))
        self.play(eyeball.move_to,RIGHT,run_time=0.5)
        self.play(eyeball.move_to,ORIGIN,run_time=0.5)
        self.play(eyeball.move_to,LEFT,run_time=0.5)
        self.play(eyeball.move_to,ORIGIN,run_time=0.5)
        
        self.play(FadeOut(eyeball),FadeOut(ellipse),reco.set_opacity,1,toolbox.set_opacity,1)


        rect = Rectangle(height=1)
        rect.surround(lines[0])
        self.play(FadeIn(rect))
        self.wait()
        
        infos = VGroup(TextMobject("Registered Users"),TextMobject("Emails"),TextMobject("Contacts"),TextMobject("Domain Names"), TextMobject("...")).arrange(DOWN,aligned_edge = LEFT,buff=0.35).set_color_by_gradient(RED, YELLOW)
        infos.next_to(toolbox,6*RIGHT).scale(0.7)

        

        j=0
        for i in range(1,5):
            self.play(rect.surround,lines[i],run_time=0.5)
            if i%2!=0:
                self.play(TransformFromCopy(lines[i],infos[j]),run_time=0.5)
                j+=1
            
        for i in range(4,-1,-1):
            self.play(rect.surround,lines[i],run_time=0.5)
            if i%2==0:
                self.play(TransformFromCopy(lines[i],infos[j]),run_time=0.5)
                j+=1
        self.wait()

        self.play(toolbox.set_opacity,0.05,infos.set_opacity,0.05,rect.set_opacity,0.05)

        info = TextMobject("Generally, these are Publically Available Information").set_color_by_gradient(BLUE,YELLOW).scale(1.2)
        self.play(Write(info,run_time=0.5))
        self.wait()
        self.play(FadeOut(info),FadeOut(toolbox),FadeOut(infos),FadeOut(rect),FadeIn(mindtree),mindtree.set_opacity,1,ReplacementTransform(reco,mindtree[0]),rect.set_opacity,1)
        self.wait()

        


        

        






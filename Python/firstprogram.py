from os import write
from xml.dom import DomstringSizeErr
from numpy.core.fromnumeric import _transpose_dispatcher
from manimlib.imports import *

class Introduction(Scene):
    def construct(self):
        self.wait()
        title = TextMobject("First Program").scale(2)
        self.play(Write(title))
        self.wait(5)
        self.play(FadeOutAndShift(title,2*RIGHT))
        contents = VGroup(
            TexMobject("\emph IDLE"),
            TextMobject("Any Code Editor (recommended)")
        ).arrange(DOWN,buff=1.5)
        contents[0].set_color(YELLOW)
        contents[1].set_color(TEAL)
        self.play(FadeInFrom(contents[0],UP))
        self.wait(2)
        self.play(FadeInFrom(contents[1],UP))
        self.wait(2)

        idle = contents[0].copy()

        self.play(ApplyMethod(idle.move_to,ORIGIN),FadeOut(contents),ApplyMethod(idle.scale,2))
        self.wait(2)

        idlefull = TextMobject('Integrated ','Development ','and ','Learning ','Environment').next_to(idle,DOWN,buff=0.5)
        self.play(FadeIn(idlefull))
        self.wait()
        self.play(idlefull.move_to,2*UP)
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
        self.play(ReplacementTransform(idle,box),run_time=2)
        lines = VGroup(*[Line(ORIGIN,2*LEFT,color= GREEN) for i in range(5)]).arrange(DOWN,aligned_edge = LEFT,buff=0.35)
        lines.move_to(2*LEFT+1*DOWN)
        self.play(ShowCreation(options),Transform(idlefull,lines))
        toolbox = VGroup(options,idlefull,box)
        self.play(toolbox.shift,1*UP)
        #toolbox = 
        # for x,y in zip(idlefull,lines):
        #     self.play(Transform(x,y),run_time=0.25)
        self.wait()

        code = VGroup(
            TextMobject(">>> ","2+2"),
            TextMobject(">>> ","4"),
            TextMobject(">>> ","'apple' ","+"," 'banana'"),
            TextMobject(">>> ","'applebanana'")
        ).arrange(DOWN,buff=0.5,aligned_edge=LEFT)

        code[0][0].set_color(GOLD)
        code[0][1].set_color(PURPLE) 
        code[1][0].set_color(GOLD) 
        code[1][1].set_color(TEAL) 
        code[2][0].set_color(GOLD) 
        code[2][1].set_color(GREEN) 
        code[2][2].set_color(PURPLE) 
        code[2][3].set_color(GREEN) 
        code[3][0].set_color(GOLD) 
        code[3][1].set_color(MAROON) 

        code.next_to(box,2*RIGHT).scale(0.8)
        self.play(Write(code),rate_func=rush_into)
 
        statement = TextMobject("statements").to_edge(UR,buff=0.5)
        output = TextMobject("outputs").next_to(statement,DOWN,buff=0.8)
 
        arrow1 = Arrow(code[0][1].get_right(),statement.get_corner(DL),max_tip_length_to_length_ratio=0,max_stroke_width_to_length_ratio=1)
        arrow2 = Arrow(code[2][3].get_corner(UR),statement.get_corner(DL),max_tip_length_to_length_ratio=0,max_stroke_width_to_length_ratio=1)

        self.play(ShowCreation(arrow1),ShowCreation(arrow2))
        self.wait(0.1)
        self.play(DrawBorderThenFill(statement))
        st = VGroup(arrow1,arrow2,statement)
        arrow3 = Arrow(code[1][1].get_right(),output.get_corner(DL),max_tip_length_to_length_ratio=0,max_stroke_width_to_length_ratio=1)
        arrow4 = Arrow(code[3][1].get_corner(UR),output.get_corner(DL),max_tip_length_to_length_ratio=0,max_stroke_width_to_length_ratio=1)
        
        self.play(ShowCreation(arrow3),ShowCreation(arrow4),st.set_opacity,0.2)
        self.wait(0.1)
        self.play(Write(output))
        
        fullstot = VGroup(arrow3,arrow4,output,st)
        self.wait(6)
        self.play(FadeOutAndShift(fullstot,3*DL),FadeOutAndShift(toolbox,3*UR),FadeOutAndShiftDown(code))
        self.wait()


class CodeEditors(Scene):
    def construct(self):
        contents = VGroup(
            TexMobject("\emph IDLE"),
            TextMobject("Any", " Code Editor", " (recommended)")
        ).arrange(DOWN,buff=1.5)
        contents[0].set_color(YELLOW)
        contents[1].set_color(TEAL)
        self.wait(8)
        self.play(FadeIn(contents))
        self.play(contents[1].scale,1.5,contents[1].move_to,ORIGIN,FadeOut(contents[0]))
        self.wait(3)
        
        self.play(FadeOut(contents[1][0]),FadeOut(contents[1][2]))
        self.play(contents[1][1].shift,2*LEFT)
        
        ide = VGroup(
            TextMobject(" /"),
            TextMobject(" IDE"),
            TextMobject(" Integrated Development Environment")
        ).arrange(RIGHT,buff=0.2)

        ide.scale(1.5)
        ide.next_to(contents[1][1],RIGHT,buff=0.2)
        ide[2].shift(0.5*UP+3*LEFT)
        ide[2].scale(0.5)
        ide[0].set_color(YELLOW)
        ide[1].set_color(ORANGE)
        ide[2].set_color(WHITE)
        self.play(ShowCreation(ide[0]),ShowCreation(ide[1]))
        self.play(Write(ide[2]))
        self.wait(2)

        newtopic = VGroup(ide[0],ide[1],contents[1][1])

        self.play(FadeOut(ide[2]),ApplyMethod(newtopic.to_edge,UP))
        self.wait()

        ides = VGroup(
            TextMobject("Pycharm"),
            TextMobject("Anaconda"),
            TextMobject("VS Code"),
            TextMobject("Google Colab")
        )

        vscode = SVGMobject("zbunker/resources/vs-code.svg")
        vscode.scale(1.5).move_to(0*RIGHT+0.8*DOWN)
        colors = it.cycle(["#0b75bb","#248ccc","#1474b4","#3c9cd4","#1880c1"])
        for i in range(len(vscode)):
            color = next(colors)
            vscode[i].set_color(color)
            vscode[i].set_stroke(color,0)


        ides[0].next_to(vscode,vscode.get_corner(UR),buff=0.2)
        ides[1].next_to(vscode,vscode.get_corner(DR),buff=0.2)
        ides[2].next_to(vscode,vscode.get_corner(DL),buff=0.2)
        ides[3].next_to(vscode,vscode.get_corner(UL),buff=0.2)

        for i in ides:
            self.play(Write(i))

        for i in range(3):
            self.play(CyclicReplace(*ides),run_time=3)

        highlight = BackgroundRectangle(ides[2],color= YELLOW, fill_opacity = 0.4,buff=0.125 )
        self.play(ShowCreationThenFadeOut(highlight))
        self.play(TransformFromCopy(ides[2],vscode))
        self.wait(8)

        self.play(Flash(ides[0]),Flash(ides[1]),Flash(ides[3]),flash_radius = 0.5)
        self.wait(8)

        self.play(FadeOutAndShift(ides,2*DR),FadeOutAndShift(ide[1],2*UL),FadeOutAndShift(contents[1][1],2*UL),FadeOutAndShift(ide[0],2*UL))
        self.wait(5)
        self.play(vscode.shift,2.5*LEFT+0.8*UP)
        RN = VGroup(
            TextMobject("Video link in"),
            TextMobject("the description"),
            TextMobject("Rishabh Narayan")
        ).arrange(DOWN,buff=0.5)

        RN.next_to(vscode,RIGHT,buff=1)

        self.play(Write(RN[0]),Write(RN[1]))
        self.wait(5)
        RN[2].shift(1.5*UP).scale(1.2).set_color(RED)
        self.play(ReplacementTransform(RN[1],RN[2]),FadeOut(RN[0]))
        self.wait(12)

        self.play(FadeOut(vscode),FadeOut(RN[2]))
        self.wait()







    



        
        

        

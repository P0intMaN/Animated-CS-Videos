#from numpy.lib.type_check import imag
from os import write
from re import L
from numpy.core.einsumfunc import _greedy_path
from manimlib.imports import *

class PythonIntro(Scene):
    def construct(self):
        image = SVGMobject("zbunker/resources/python.svg")
        image.scale(3)
        colors = it.cycle(["#fccc3b","#fcd546","#377dae","#346b94","#fcdd54"])
        for i in range(len(image)):
            color = next(colors)
            image[i].set_color(color)
            image[i].set_stroke(color,0)
        self.play(DrawBorderThenFill(image),run_time=3)
        pytext = TextMobject("PYTHON").scale(1.5)
        self.play(image.move_to,(4*LEFT),image.scale,0.5,Write(pytext))
        self.wait(6)
        
        
        # interpreted,  highlevel, general purpose
        points = BulletedList("Interpreted", "High level","General Purpose")
        points.next_to(image,buff=MED_LARGE_BUFF)
        self.play(ReplacementTransform(pytext,points))
        #self.play(Write(points),run_time=2)
        self.wait()
        self.play(points[1].set_opacity,0.2,points[2].set_opacity,0.2)
        self.wait()
        #arrow = Arrow(points[0].get_right(),3*UP+3*RIGHT,max_tip_length_to_length_ratio=0,max_stroke_width_to_length_ratio=1)
        #self.play(ShowCreation(arrow))#self.play(Write(arrow)) 
        ip = TextMobject("Uses an Interpreter not Compiler.").set_color(YELLOW).to_edge(UP)
        ip2 = TextMobject("Reads the line of code one by one and executes.").set_color(BLUE).move_to(2*DOWN)
        self.play(Write(ip))
        self.wait(2)
        self.play(Write(ip2),rate_func=rush_into)
        self.wait()
        self.play(FadeOut(ip),FadeOut(ip2))
        self.wait()
        self.play(points[0].set_opacity,0.2,points[2].set_opacity,0.2,points[1].set_opacity,1)
        self.wait()
        Hl = TextMobject("The syntaxes are similar to English.").set_color(BLUE).move_to(2*UP)
        self.play(Write(Hl))
        self.wait(7) 
        self.play(FadeOut(Hl))
        self.wait()
        self.play(points[0].set_opacity,0.2,points[1].set_opacity,0.2,points[2].set_opacity,1)
        gp = TextMobject("Build Anything :)").set_color(YELLOW).to_edge(2*RIGHT)
        self.play(Write(gp))
        self.wait(3)
        self.play(FadeOut(gp))
        self.play(FadeOut(points),FadeOut(image))
        

class OpenSource(Scene):
    def construct(self):
        opentxt = TextMobject("OPEN"," SOURCE")
        opentxt.set_color_by_gradient(PURPLE,BLUE)
        opentxt.scale(3)
        self.play(DrawBorderThenFill(opentxt),run_time=3)
        self.wait(8)
        self.play(ApplyWave(opentxt))
        self.play(opentxt.to_edge,UP,opentxt.scale,0.5)
        self.wait(2)
        opens = TextMobject("open-source (computing) ").set_color(YELLOW)
        opens.move_to(4*LEFT+1.8*UP)
        adj = TexMobject("\emph adjective: ").set_color(ORANGE)
        open1 = Text(" used to describe software for which")
        open1.move_to(1.8*UP+3.8*RIGHT).scale(0.7)
        open2 = Text(" the original source code is made available to anyone")
        open2.move_to(1*UP+2.7*LEFT).scale(0.7)
        adj.next_to(opens,RIGHT)
        allop = VGroup(opens,adj,open1,open2)
        self.play(Write(allop),rate_func=rush_into)
        self.wait(5)
        osi = SVGMobject("zbunker/resources/osi.svg")
        osi.move_to(1.7*DOWN).scale(2)
        colors = it.cycle(["#1c541c","#3ca43c","#246423","#2d7b2a","#349032"])
        for i in range(len(osi)):
            color = next(colors)
            osi[i].set_color(color)
            osi[i].set_stroke(color,0)
        self.play(ShowCreation(osi))
        self.wait(5)
        self.play(FadeOut(osi),FadeOut(allop),FadeOutAndShift(opentxt,RIGHT))
        self.wait()


class XPlatform(GraphScene):
    def construct(self):
        title = TextMobject("CROSS PLATFORM").scale(2.5)
        title.set_color_by_gradient(RED,YELLOW)
        self.play(Write(title))
        self.wait()
        dot = Dot(radius = 0.15, color = YELLOW)
        dot.move_to(2*UP)
        dots = TexMobject("\emph code").scale(1.8).move_to(2*UP+4*LEFT)
        self.play(ReplacementTransform(title,dots))
        self.wait()
        linux = TextMobject("linux OS").move_to(4*RIGHT)
        wind = TextMobject("windows").move_to(4*LEFT)
        windrect = Square(color = BLUE).surround(wind)
        linuxrect = Square(color = RED).surround(linux)
        windwos = VGroup(wind,windrect)
        lin = VGroup(linux,linuxrect)
        #self.play(ShowCreation(windrect),ShowCreation(linuxrect),Write(wind),Write(linux))
        self.play(TransformFromCopy(dots,windwos))
        self.play(dots.move_to,4*RIGHT+2*UP)
        self.play(TransformFromCopy(dots,lin))
        self.play(dots.move_to,2*UP+0*RIGHT)
        self.wait()
        runs1 = TextMobject("runs perfect!").set_color(GREEN)
        runs2 = runs1.copy()
        runs1.next_to(windwos,DOWN,buff=1)
        runs2.next_to(lin,DOWN,buff=1)
        self.play(FadeInFrom(runs1,UP),FadeInFrom(runs2,UP))
        self.wait()
        self.play(FadeOutAndShift(windwos,LEFT),FadeOutAndShift(lin,RIGHT),FadeOutAndShiftDown(runs1),FadeOutAndShiftDown(runs2),FadeOutAndShift(dots,UP))
        

class Libraries(Scene):
    def construct(self):
        l = TextMobject("L")
        i = TextMobject("I")
        b = TextMobject("B")
        r1= TextMobject("R")
        a = TextMobject("A")
        r2= TextMobject("R")
        y = TextMobject("Y")

        library = VGroup(l,i,b,r1,a,r2,y).set_color(TEAL).arrange_submobjects(RIGHT).scale(2)
        self.play(FadeInFrom(library,LEFT))
        self.wait(21)
        self.play(library.arrange_submobjects,DOWN,library.move_to,3.2*LEFT)
        storetext = TexMobject("\emph store").scale(2)
        store = VGroup(
            Line(ORIGIN,3*RIGHT,color = RED),#L
            Line(3*RIGHT,3*UR,color = BLUE),#I
            Line(3*UR,3*UP,color = MAROON),#B
            Line(3*UP,ORIGIN,color = PURPLE),#R
            
        )
        storetext.next_to(store,DOWN)
        #self.play(ReplacementTransform(l,store[0]),ReplacementTransform(i,store[1]),ReplacementTransform(b,store[2]),ReplacementTransform(r1,store[3]),ReplacementTransform(r2,storetext),ReplacementTransform(a,storetext),ReplacementTransform(y,storetext))

        for i in range(0,4):
            self.play(ReplacementTransform(library[i],store[i]),run_time=0.5)

        self.play(ReplacementTransform(r2,storetext),ReplacementTransform(a,storetext),ReplacementTransform(y,storetext),run_time=0.5)
        stores = VGroup(store,storetext)
        self.play(stores.shift,5*LEFT+DOWN)
        x = 10
        y = 10
        dots = VGroup(*[Dot() for i in range(x*y)])
        dots.arrange_in_grid(x,y,buff= SMALL_BUFF)
        colors = [RED,GREEN,ORANGE,TEAL,WHITE]
        for i in range(0,x*y):
            dots[i].set_color(colors[i%5])
        
        dots.shift(RIGHT+0.5*UP)
        self.play(ApplyWave(stores),FadeInFrom(dots,2*LEFT))
        brace = Brace(dots,DOWN,buff=SMALL_BUFF)
        li = TextMobject("library").set_color_by_gradient(BLUE,YELLOW)
        li.next_to(brace,DOWN)
        self.play(Write(brace),FadeInFrom(li,DOWN))
        self.play(FocusOn(dots[0]),stores.set_opacity,0.2,dots.set_opacity,0.2,dots[0].set_opacity,1,li.set_opacity,0.2,brace.set_opacity,0.2)
        arrow = Arrow(dots[0].get_top(),3*UP+2*RIGHT,max_tip_length_to_length_ratio=0,max_stroke_width_to_length_ratio=1)
        self.play(ShowCreation(arrow))
        m = TextMobject("a module")
        m.next_to(arrow).shift(0.8*UP).set_color(GOLD)
        self.play(Write(m))
        
        self.play(FadeOutAndShiftDown(dots),FadeOutAndShiftDown(stores),FadeOutAndShiftDown(arrow),m.scale,3,m.move_to,0*RIGHT+0*DOWN,FadeOutAndShiftDown(li),FadeOutAndShiftDown(brace))
        self.modules(m)
        self.examples()

    def modules(self,m):
        frstloc = TextMobject("key = [NULL,2]")
        scndloc = TextMobject("x: ArrayLike,")
        thrdloc = TextMobject("def autonum() -> None")
        frthloc = TextMobject("int(np.nextafter(x, np.inf)*dpi) % n = 0")
        f = TextMobject("...")
        s = TextMobject("...")
        codes = VGroup(frstloc,scndloc,thrdloc,frthloc,f,s).arrange(DOWN,center=False,aligned_edge=LEFT).set_color(TEAL_E)
        codes.move_to(3*LEFT+UP).scale(0.8)
        self.play(ReplacementTransform(m,codes[0]))
        self.play(FadeInFrom(codes[1],UP))
        self.play(FadeInFrom(codes[2],UP))
        self.play(FadeInFrom(codes[3],UP),FadeInFrom(codes[4],UP),FadeInFrom(codes[5],UP))
        arrow = Arrow(codes.get_right(),1.5*RIGHT+1*UP,buff=SMALL_BUFF)
        self.play(Write(arrow),run_time=0.5)
        sp = VGroup(
            TextMobject("Advanced Computation"),
            TextMobject("Graphing"),
            TextMobject("Requests"),
        ).arrange(DOWN)
        sp.next_to(arrow,RIGHT).set_color(RED)
        self.play(ShowCreation(sp))
        self.wait(7)
        self.play(FadeOut(sp),FadeOut(codes),FadeOut(arrow))
        self.wait()

    def examples(self):
        xmp = TextMobject("Some Famous Libraries").scale(1.5)
        line = Line(xmp.get_left(),xmp.get_right())
        line.next_to(xmp, DOWN)
        self.play(Write(xmp),run_time=2)
        self.play(Write(line))
        introl = VGroup(xmp, line)
        self.play(introl.to_edge,UP, introl.set_color,YELLOW)
        self.wait()        

        dots = VGroup(*[Dot() for i in range(3)]).arrange(RIGHT)         
        for dot in dots:
            self.play(FadeIn(dot),run_time=0.5)
        ml = TextMobject("Machine Learning").move_to(UP+4*LEFT).set_color_by_gradient(PURPLE,GREEN)
        ml_line = Line(ml.get_left(),ml.get_right()).next_to(ml,DOWN)
        #dots.next_to(ml,RIGHT)        
        self.play(ReplacementTransform(dots,ml),ShowCreation(ml_line)) 
        self.wait()
        mp = BulletedList("TensorFlow","Pytorch", "SciKit Learn","Keras",color=BLUE)
        mp.next_to(ml_line,DOWN)
        self.play(Write(mp))
        Ml = VGroup(ml,ml_line,mp)
        self.wait()
        tri = Polygon(np.array([0,0,0]),np.array([1,1,0]),np.array([1,-1,0]))
        self.play(ShowCreation(tri))
        ds = TextMobject("Data Science").move_to(4*RIGHT+UP).set_color_by_gradient(BLUE,YELLOW)
        ds_line = Line(ds.get_left(),ds.get_right()).next_to(ds,DOWN)
        self.play(ReplacementTransform(tri,ds),ShowCreation(ds_line))
        dp = BulletedList("NumPy","Pandas", "Matplotlib",color=RED)
        dp.next_to(ds_line,DOWN)
        self.play(Write(dp))
        Ds = VGroup(ds,ds_line,dp)

        ring=Annulus(inner_radius=.2, outer_radius=1, color=BLUE)
        ring2 = Annulus(inner_radius=0.6, outer_radius=1, color=BLUE)
        self.play(Transform(ring,ring2))
        self.play(Transform(ring2, ring),run_time=0.5)
        rings = VGroup(ring,ring2)
        cv = TextMobject("Computer Vision").move_to(UP+0.25*RIGHT).set_color_by_gradient(RED,WHITE)
        cv_line = Line(cv.get_left(),cv.get_right()).next_to(cv,DOWN)
        self.play(ReplacementTransform(rings,cv),ShowCreation(cv_line),Ds.set_opacity,0.2,Ml.set_opacity,0.2)
        cp = BulletedList("OpenCV","PyTesseract",color = GOLD)
        cp.next_to(cv_line,DOWN)
        self.play(Write(cp))        
        Cv = VGroup(cv,cv_line,cp)

        self.wait(18)
        self.play(FadeOutAndShift(Ml,2*DL),FadeOutAndShift(Ds,2*DL),FadeOutAndShift(Cv,2*DL),FadeOut(introl))


class Speed(Scene):
    def construct(self):
        dis = TextMobject("Disadvantage").scale(2).set_color(BLUE)
        speed = TexMobject("\emph speed").scale(2).set_color(RED)
        self.play(Write(dis))
        self.wait(2)
        self.play(Transform(dis,speed))
        self.play(ShowPassingFlashAround(dis))
        self.wait()
        self.play(dis.move_to,3*LEFT+UP,dis.scale,0.5)
        speed_test = TextMobject("Speed Comparison").scale(2).to_edge(UP).set_color(DARK_BLUE)
        self.play(TransformFromCopy(dis,speed_test))
        
        desc = TextMobject("Speed tests carried out: ").move_to(3*LEFT+UP)
        Li = BulletedList("K-mer Test","BLAST Test","FASTA Test","...","...")
        sq = Rectangle(height = 5,width = 5.5,color=RED).move_to(3*LEFT+1*DOWN)
        Li[0].set_color(MAROON)
        Li[1].set_color(ORANGE)
        Li[2].set_color(YELLOW)
        Li.next_to(dis,DOWN,buff=0.5)
        self.play(ReplacementTransform(dis,sq),FadeIn(desc))
        self.play(FadeInFrom(Li[0],UP))
        self.play(FadeInFrom(Li[1],UP))
        self.play(FadeInFrom(Li[2],UP),FadeInFrom(Li[3],UP),FadeInFrom(Li[4],UP))
        speedt = VGroup(desc,Li,sq) 
        trend = VGroup(
            TextMobject("C/C++"),
            TextMobject("JAVA"),
            TextMobject("Go"),
            TextMobject("JavaScript"),
            TextMobject("Python"),
        ).arrange(DOWN)
        arrow = Arrow(speedt.get_right(),2*RIGHT+0.5*DOWN,buff=SMALL_BUFF)
        self.play(ShowCreationThenDestruction(arrow))
        trend[0].set_color(GREEN)
        trend[1].set_color(TEAL)
        trend[2].set_color(YELLOW)
        trend[3].set_color(ORANGE)
        trend[4].set_color(RED)

        trend.move_to(2*RIGHT+0.5*DOWN)
        self.play(DrawBorderThenFill(trend[0]))
        self.play(Write(trend[1]))
        self.play(FadeIn(trend[2]))
        self.play(FadeInFromLarge(trend[3]),FadeInFromDown(trend[4]))
        self.wait(3)
        self.play(trend.set_opacity,0.2,speedt.set_opacity,0.2,trend[4].set_opacity,1,ShowCreationThenFadeAround(trend[4]))
        self.wait(3)
        self.play(FadeOutAndShift(trend[0],2*UP),FadeOutAndShift(trend[1],2*UP),FadeOutAndShift(trend[2],2*UP),FadeOutAndShift(trend[3],2*UP),FadeOutAndShift(speedt,2*DOWN),trend[4].move_to,0*RIGHT+0*DOWN,trend[4].scale,2,FadeOut(speed_test))
        self.wait(10)        

        image = SVGMobject("zbunker/resources/python.svg")
        image.scale(3)
        colors = it.cycle(["#fccc3b","#fcd546","#377dae","#346b94","#fcdd54"])
        for i in range(len(image)):
            color = next(colors)
            image[i].set_color(color)
            image[i].set_stroke(color,0)
        self.play(Transform(trend[4],image),run_time=3)
        self.wait(10)
        



         






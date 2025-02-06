from manim import *

class ComboSolve(Scene):
    def construct(self):
        '''
        square1 = Square(color=BLUE)
        circle = Circle(fill_opacity=0.5, color=PINK)
        square2 = square1.copy().set_color(color=RED).move_to(RIGHT *5)
        group = Group(square1, square2)
        self.play(FadeIn(group))
        self.play(Transform(square1, circle))
        self.play(Rotate(square2, PI * 20))
        self.wait(2)
        '''

        equation1 = MathTex("1+22+333+4444+55555+666666+7777777+88888888+999999999")
        equation2 = MathTex("9+98+987+9876+98765+987654+9876543+98765432+987654321")
        equation1.shift(UP)
        equation2.shift(DOWN)
        eq_group = VGroup(equation1, equation2)
        eq_group.scale(0.8)
        self.play(Write(eq_group))
        task = Text("Какое из этих выражений больше (или они равны)?", font="Noto Sans")
        '''
        first_word = Text("Какие возникают первые мысли?", font="Noto Sans")
        second_word = Text("В первом выражении складываются числа, размер которых такой же, как и цифра, из которой они состоят", font="Noto Sans")
        third_word = Text("Во втором - числа, состоящие из цифр, стоящих в обратном порядке", font="Noto Sans")
        second_word.shift(UP)
        third_word.shift(DOWN)
        '''
        task.scale(0.7)
        '''
        first_word.scale(0.7)
        second_word.scale(0.4)
        third_word.scale(0.4)
        word3_group = VGroup(first_word, second_word, third_word)
        '''
        self.play(Write(task))
        self.wait(10)
        animations = [
            FadeOut(task, scale=0.5),
            FadeOut(eq_group, shift=DOWN),
            #FadeIn(word3_group[0]),
            #FadeIn(word3_group[1], shift=2*DOWN),
            #FadeIn(word3_group[2],shift=2*UP),
        ]
        self.play(AnimationGroup(*animations, lag_ratio=1))
        #self.wait(10)
        
        #self.play(FadeOut(word3_group, shift=DOWN))
        
        n1 = MathTex("1")
        n2 = MathTex("2", "2")
        n3 = MathTex("3", "3", "3")
        n4 = MathTex("4", "4", "4", "4")
        n5 = MathTex("5", "5", "5", "5", "5")
        n6 = MathTex("6", "6", "6", "6", "6", "6")
        n7 = MathTex("7", "7", "7", "7", "7", "7", "7")
        n8 = MathTex("8", "8", "8", "8", "8", "8", "8", "8")
        n9 = MathTex("9", "9", "9", "9", "9", "9", "9", "9", "9")
        n1.shift(UP*3.2)
        n2.shift(UP*2.4)
        n3.shift(UP*1.6)
        n4.shift(UP*0.8)
        n6.shift(DOWN*0.8)
        n7.shift(DOWN*1.6)
        n8.shift(DOWN*2.4)
        n9.shift(DOWN*3.2)
        n2.align_to(n1, RIGHT)
        n3.align_to(n1, RIGHT)
        n4.align_to(n1, RIGHT)
        n5.align_to(n1, RIGHT)
        n6.align_to(n1, RIGHT)
        n7.align_to(n1, RIGHT)
        n8.align_to(n1, RIGHT)
        n9.align_to(n1, RIGHT)
        num1_group = VGroup(n1, n2, n3, n4, n5, n6, n7, n8, n9)
        num1_group.shift(UP + LEFT*0.8)
        num1_group.scale(0.8)
        for i in range(9):
            for j in range(i+1):
                num1_group[i][i-j].shift(LEFT*(0.4*j))
        n11 = MathTex("9")
        n22 = MathTex("9", "8")
        n33 = MathTex("9", "8", "7")
        n44 = MathTex("9", "8", "7", "6")
        n55 = MathTex("9", "8", "7", "6", "5")
        n66 = MathTex("9", "8", "7", "6", "5", "4")
        n77 = MathTex("9", "8", "7", "6", "5", "4", "3")
        n88 = MathTex("9", "8", "7", "6", "5", "4", "3", "2")
        n99 = MathTex("9", "8", "7", "6", "5", "4", "3", "2", "1")
        n11.shift(UP*3.2)
        n22.shift(UP*2.4)
        n33.shift(UP*1.6)
        n44.shift(UP*0.8)
        n66.shift(DOWN*0.8)
        n77.shift(DOWN*1.6)
        n88.shift(DOWN*2.4)
        n99.shift(DOWN*3.2)
        n22.align_to(n11, RIGHT)
        n33.align_to(n11, RIGHT)
        n44.align_to(n11, RIGHT)
        n55.align_to(n11, RIGHT)
        n66.align_to(n11, RIGHT)
        n77.align_to(n11, RIGHT)
        n88.align_to(n11, RIGHT)
        n99.align_to(n11, RIGHT)
        num2_group = VGroup(n11, n22, n33, n44, n55, n66, n77, n88, n99)
        num2_group.shift(UP + RIGHT*6)
        num2_group.scale(0.8)
        for i in range(9):
            for j in range(i+1):
                num2_group[i][i-j].shift(LEFT*(0.4*j))
        animations2 = [
            FadeIn(num1_group[0], shift=DOWN*0.8),
            FadeIn(num2_group[0], shift=DOWN*0.8),
            FadeIn(num1_group[1], shift=DOWN*1.6),
            FadeIn(num2_group[1], shift=DOWN*1.6),
            FadeIn(num1_group[2], shift=DOWN*2.4),
            FadeIn(num2_group[2], shift=DOWN*2.4),
            FadeIn(num1_group[3], shift=DOWN*3.2),
            FadeIn(num2_group[3], shift=DOWN*3.2),
            FadeIn(num1_group[4], shift=DOWN*4),
            FadeIn(num2_group[4], shift=DOWN*4),
            FadeIn(num1_group[5], shift=DOWN*4.8),
            FadeIn(num2_group[5], shift=DOWN*4.8),
            FadeIn(num1_group[6], shift=DOWN*5.6),
            FadeIn(num2_group[6], shift=DOWN*5.6),
            FadeIn(num1_group[7], shift=DOWN*6.4),
            FadeIn(num2_group[7], shift=DOWN*6.4),
            FadeIn(num1_group[8], shift=DOWN*7.2),
            FadeIn(num2_group[8], shift=DOWN*7.2),
        ]
        self.play(AnimationGroup(*animations2, lag_ratio=0.2))
        self.wait(1)
        for i in range(4):
            #0.64, т.к. 0.8(DOWN) * 0.8(scale)
            self.play(num2_group[i].animate.shift(DOWN*((8-i*2)*0.64)),
                      num2_group[8-i].animate.shift(UP*((8-i*2)*0.64)))
        final = []
        for i in range(1, 9):
            for j in range(1, i+1):
                animation = num2_group[i][i-j].animate.shift(DOWN*j*0.64)
                final.append(animation)
        self.play(AnimationGroup(*final, lag_ratio=0.1))
        self.wait(3)

        frame = Rectangle(
            width = 5.2,
            height = 6,
            color = YELLOW,
        )
        frame.move_to(n99[4])
        self.play(Create(frame))
        self.wait(0.5)
        self.play(frame.animate.move_to(n5[0]))
        self.play(FadeOut(frame))
        end1 = Text("Они одинаковые", font="Noto Sans")
        end2 = Text("Ответ: два этих выражения равны", font="Noto Sans")
        end1.shift(DOWN*3)
        end2.shift(DOWN*3)
        end2.set_color_by_gradient(RED, YELLOW, GREEN, BLUE)
        self.play(FadeIn(end1))
        self.play(FadeOut(end1))
        self.play(FadeIn(end2))
        self.wait(7)
                
        
        
        
        
        

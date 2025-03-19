from manim import *        

class ConvolutionalLayerProcess(Scene):
    def construct(self):
        title = Text("Convolutional Layer Process", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        
        image = ImageMobject("input.png").scale(2).to_edge(LEFT).shift(DOWN*1)
        img_txt = Text("28 x 28 x 1 Image", font_size=24).move_to(image, UP).shift(UP *0.76)
        
        self.add(image)
        self.play(Write(img_txt))
        self.wait(0.5)
        
        grid_size = 28
        cell_size = image.width /grid_size
        
        grid = NumberPlane(
            x_range=[-image.width / 2, image.width / 2, cell_size],
            y_range=[-image.height / 2, image.height / 2, cell_size],
            stroke_color=WHITE,
            stroke_opacity=0.4,
            stroke_width=1
        ).to_edge(LEFT).shift(DOWN*1)


        self.play(Create(grid))
        self.wait(1)
        
        kernel_size = 3
        kernel = Square(side_length=cell_size * kernel_size, color=YELLOW)
        kernel_txt = Text("Kernel 3x3", font_size=24).move_to(kernel, UP).shift(UP)
        self.play(Create(kernel), Write(kernel_txt))
        self.wait(0.5)
        self.play(FadeOut(kernel_txt))
        
        
        self.play(kernel.animate.move_to(image.get_center() + LEFT * (image.width / 2 - cell_size * 1.5) + UP * (image.height / 2 - cell_size * 1.5)), run_time= 1.5)
        
        for i in range(grid_size - kernel_size + 1):
            for j in range(grid_size - kernel_size + 1):
                new_position = image.get_center() + LEFT * (image.width / 2 - cell_size * (1.5 + j)) + UP * (image.height / 2 - cell_size * (1.5 + i))
                self.play(kernel.animate.move_to(new_position), run_time=0.1)
        
        result_img = ImageMobject('after_one_conv.png').scale(0.65).to_edge(RIGHT).shift(DOWN)
        result_img_txt = Text("26 x 26 x 32 OutputMap", font_size=24).move_to(result_img, UP).shift(UP*0.76)
        
        self.add(result_img)
        self.play(Write(result_img_txt))
        self.wait(1)
        self.play(FadeOut(kernel, grid))
        
        images_group = Group(result_img, result_img_txt, image, img_txt).scale(0.6)

        self.play(images_group.animate.shift(LEFT*3))

        conv1_and_max_pool = ImageMobject('maxPooling.png').scale(0.65).to_edge(RIGHT).shift(DOWN).scale(0.6)
        max_pool_txt = Text("After Max Pooling\n  14 x 14 x 32", font_size=24).scale(0.6).move_to(conv1_and_max_pool, UP).shift(UP*0.76)
        
        
        self.add(conv1_and_max_pool)
        self.play(Write(max_pool_txt))
        self.wait(1)
        
        self.play(FadeOut(images_group, conv1_and_max_pool, max_pool_txt))
        
        max_pooling_img = ImageMobject('maxPooling.png').scale(0.65).to_edge(LEFT).shift(DOWN*1)
        max_pool_txt = Text("After Max Pooling\n  14 x 14 x 32", font_size=24).move_to(max_pooling_img, UP).shift(UP*0.76)
    
        self.add(max_pooling_img)
        self.play(Write(max_pool_txt))
        
        grid_size = 14
        cell_size = max_pooling_img.width /grid_size
        
        grid = NumberPlane(
            x_range=[-max_pooling_img.width / 2, max_pooling_img.width / 2, cell_size],
            y_range=[-max_pooling_img.height / 2, max_pooling_img.height / 2, cell_size],
            stroke_color=WHITE,
            stroke_opacity=0.4,
            stroke_width=1
        ).to_edge(LEFT).shift(DOWN*1)


        self.play(Create(grid))
        self.wait(1)
        
        kernel_size = 3
        kernel = Square(side_length=cell_size * kernel_size, color=ORANGE)
        kernel_txt = Text("Kernel 3x3", font_size=24).move_to(kernel, UP).shift(UP)
        self.play(Create(kernel), Write(kernel_txt))
        self.wait(0.5)
        self.play(FadeOut(kernel_txt))
        self.play(kernel.animate.move_to(max_pooling_img.get_center() + LEFT * (max_pooling_img.width / 2 - cell_size * 1.5) + UP * (max_pooling_img.height / 2 - cell_size * 1.5)), run_time= 1.5)
        
        
        for i in range(grid_size - kernel_size + 1):
            for j in range(grid_size - kernel_size + 1):
                new_position = max_pooling_img.get_center() + LEFT * (max_pooling_img.width / 2 - cell_size * (1.5 + j)) + UP * (max_pooling_img.height / 2 - cell_size * (1.5 + i))
                self.play(kernel.animate.move_to(new_position), run_time=0.1)
        

        sec_conv = ImageMobject("after_sec_conv.png").scale(0.65).to_edge(RIGHT).shift(DOWN)
        sec_txt = Text("14 x 14 x 64 Output Map", font_size=24).move_to(sec_conv, UP).shift(UP*0.76)
        
        self.add(sec_conv)
        self.play(Write(sec_txt))
        self.wait(1)
        
        self.play(FadeOut(grid, kernel))
        
        images_group = Group(sec_conv, sec_txt, max_pool_txt, max_pooling_img).scale(0.6)
        
        self.play(images_group.animate.shift(LEFT*3))
        
        conv2_and_max_pool = ImageMobject('maxpool_2.png').scale(0.65).to_edge(RIGHT).shift(DOWN).scale(0.6)
        max_pool_txt = Text("After Max Pooling\n  14 x 14 x 64", font_size=24).scale(0.6).move_to(conv1_and_max_pool, UP).shift(UP*0.76)
        
        
        self.add(conv2_and_max_pool)
        self.play(Write(max_pool_txt))
        self.wait(1)
        
        self.play(FadeOut(title,conv2_and_max_pool, max_pool_txt, images_group))
        self.wait(0.5)
        title = Text("Fully Connected Layers with Flattening and Softmax Output", font_size=36).to_edge(UP)
        
        self.play(Write(title))
        
        conv2_and_max_pool = ImageMobject('maxpool_2.png').scale(0.75).to_edge(LEFT).shift(DOWN).scale(0.6).shift(LEFT*0.5)
        max_pool_txt = Text("After Max Pooling\n  14 x 14 x 64", font_size=24).scale(0.6).move_to(conv2_and_max_pool, UP).shift(UP*0.76)
        
        self.add(conv2_and_max_pool)
        self.play(Write(max_pool_txt))
        
        
        grid_size = 14
        cell_size = conv2_and_max_pool.width /grid_size
        
        grid = NumberPlane(
            x_range=[-conv2_and_max_pool.width / 2, conv2_and_max_pool.width / 2, cell_size],
            y_range=[-conv2_and_max_pool.height / 2, conv2_and_max_pool.height / 2, cell_size],
            stroke_color=WHITE,
            stroke_opacity=0.4,
            stroke_width=1
        ).to_edge(LEFT).shift(DOWN*1, LEFT *(-0.68))
    
        self.play(Create(grid))
        self.wait(0.5)
        
        squares = VGroup(*[Square(side_length=0.5) for _ in range(7)])
        dots = VGroup(*[Dot(radius=0.1)for _ in range(3)] )
        rest_square = VGroup(*[Square(side_length=0.5) for _ in range(7)])
        
        squares.arrange(DOWN, buff=0.5)
        dots.arrange(DOWN, buff= 0.5)
        rest_square.arrange(DOWN, buff=0.5)
        
        label = VGroup(*[MathTex(fr"X_{i}", color=BLUE) for i in range(1,7)]).scale(0.35)
        label.arrange(DOWN, buff=0.2).next_to(squares, LEFT).shift(LEFT).shift(UP*0.6)
        
        label_1 = VGroup(*[MathTex(fr"X_{{{i}}}", color=BLUE) for i in range(12537, 12544)]).scale(0.35)

        label_1.arrange(DOWN, buff=0.2).next_to(rest_square, LEFT).shift(LEFT).shift(DOWN*2.6)
        
        combination = VGroup(squares, dots, rest_square).arrange(DOWN, buff=0.5).move_to(ORIGIN).scale(0.35).shift(DOWN, LEFT)
        
        txt = Text("Flattend Layer\n  1D Vector", font_size=24).move_to(combination, UP).shift(UP*0.75)
        
        self.play(Create(combination))
        self.play(Write(txt))
        self.play(Write(label))
        self.play(Write(label_1))
        self.wait(0.5)
        
        dense = VGroup(*[Circle(radius=0.2, color=BLUE) for _ in range(6)])
        dots_1 = VGroup(*[Dot(radius=0.1)for _ in range(3)] )
        dense_1 = VGroup(*[Circle(radius=0.2, color=BLUE) for _ in range(6)])
        
        dense.arrange(DOWN, buff=0.5)
        dots_1.arrange(DOWN, buff=0.5)
        dense_1.arrange(DOWN, buff=0.5)
        
        combo = VGroup(dense, dots, dense_1 ).arrange(DOWN, buff=0.5).scale(0.35).move_to(ORIGIN).shift(RIGHT, DOWN)
        
        dense_txt = Text(" Dense Layer\n  64 Neurons", font_size=24).move_to(combo, UP).shift(UP*0.75)
        self.play(Create(combo))
        self.play(Write(dense_txt))
        self.wait(0.5)
        
        
        dense_2 = VGroup(*[Circle(radius=0.2, color=RED) for _ in range(3)])
        dots_2 = VGroup(*[Dot(radius=0.1)for _ in range(3)] )
        dense_3 =  VGroup(*[Circle(radius=0.2, color=RED) for _ in range(3)])
        
        dense_2.arrange(DOWN, buff=0.5)
        dots_2.arrange(DOWN, buff=0.5)
        dense_3.arrange(DOWN, buff=0.5)
        
        combo_1 = VGroup(dense_2, dots_2, dense_3 ).arrange(DOWN, buff=0.5).scale(0.35).move_to(ORIGIN).shift(RIGHT*4, DOWN)
        
        dense_txt_1 = Text("    Output\n 10 Neurons", font_size=24).move_to(combo_1, UP).shift(UP*0.75)
        self.play(Create(combo_1))
        self.play(Write(dense_txt_1))
        self.wait(0.5)
        
        label_2 = VGroup(*[Text(f"{i}", color= RED) for i in range(3)]).scale(0.35)
        label_2.arrange(DOWN, buff=0.2).next_to(dense_2, RIGHT)
        
        label_3 = VGroup(*[Text(f"{i}", color= RED) for i in range(7,10)]).scale(0.35)
        
        label_3.arrange(DOWN, buff=0.2).next_to(dense_3, RIGHT)
        
        self.play(Write(label_2), Write(label_3))
        
        self.wait(0.5)
        
        lines = VGroup()
        
        for source_group, target_group in [(dense, dense_2), (dense_1, dense_3)]:
            for source in source_group:
                for target in target_group:
                    line = Line(source.get_center(), target.get_center(), color=WHITE, stroke_width=1)
                    lines.add(line)

        self.play(Create(lines))
        self.wait(0.5)
        
        self.play(*[line.animate.set_color(BLUE) for line in lines], run_time = 2)
        self.wait(0.5)
        
        dense_3[-1].set_fill(color=RED, opacity = 1)
        self.wait(1)
        
        arrow = Arrow(start = dense_3[-1].get_center() + RIGHT*3, end =dense_3[-1].get_center()+RIGHT*1, color = RED )
        self.play(Create(arrow))
        
        self.wait(0.5)
        
        self.play(FadeOut(combo, combo_1, arrow, title,
                          grid,conv2_and_max_pool,combination,label,
                          label_1, label_2, label_3 , max_pool_txt,txt,dense_txt, dense_txt_1, lines  ))
        
        self.wait(0.5)
        
        title = Text("Thanks for watching.").to_edge(ORIGIN)
        self.play(Write(title))
        self.wait(2)
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
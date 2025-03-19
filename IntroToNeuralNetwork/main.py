from manim import *
class MLPAnimation(Scene):
    
    def construct(self):
       
        input_layer = VGroup(*[Circle(radius=0.2, color=BLUE) for _ in range(10)]).arrange(DOWN, buff=0.3).shift(LEFT * 4)
        hidden_layer1 = VGroup(*[Circle(radius=0.2, color=GREEN) for _ in range(8)]).arrange(DOWN, buff=0.4).shift(LEFT * 2)
        hidden_layer2 = VGroup(*[Circle(radius=0.2, color=YELLOW) for _ in range(7)]).arrange(DOWN, buff=0.5).shift(RIGHT * 1.5)
        output_layer = VGroup(*[Circle(radius=0.2, color=RED) for _ in range(3)]).arrange(DOWN, buff=0.7).shift(RIGHT * 3.5)

       
        dots_before = VGroup(*[Dot(radius=0.04) for _ in range(3)]).arrange(DOWN, buff=0.1).next_to(output_layer[0], DOWN *0.5)
        dots_after = VGroup(*[Dot(radius=0.04) for _ in range(3)]).arrange(DOWN, buff=0.1).next_to(output_layer[1], DOWN * 0.5)

        input_values = VGroup(
            Text("X₁").scale(0.6).next_to(input_layer[0], LEFT, buff=0.2),
            Text("X₂").scale(0.6).next_to(input_layer[1], LEFT, buff=0.2),
            Text("X₃").scale(0.6).next_to(input_layer[2], LEFT, buff=0.2),
            Text("X₄").scale(0.6).next_to(input_layer[3], LEFT, buff=0.2),
            Text("X₅").scale(0.6).next_to(input_layer[4], LEFT, buff=0.2),
            Text("X₆").scale(0.6).next_to(input_layer[5], LEFT, buff=0.2),
            Text("(...)").scale(0.6).next_to(input_layer[6], LEFT, buff=0.2),
            Text("X_{D-2}").scale(0.6).next_to(input_layer[7], LEFT, buff=0.2),
            Text("X_{D-1}").scale(0.6).next_to(input_layer[8], LEFT, buff=0.2),
            Text("X_D").scale(0.6).next_to(input_layer[9], LEFT, buff=0.2),
        )
        
       
        output_labels = VGroup(
            Text("0").scale(0.6).next_to(output_layer[0], RIGHT, buff=0.2),
            Text("5").scale(0.6).next_to(output_layer[1], RIGHT, buff=0.2),
            Text("9").scale(0.6).next_to(output_layer[2], RIGHT, buff=0.2),
        )

        
        input_label = Text("Input Layer (784)").scale(0.5).next_to(input_layer, LEFT).shift(LEFT *0.5)
        hidden_label1 = Text("Hidden Layer (128)").scale(0.5).next_to(hidden_layer1, UP)
        hidden_label2 = Text("Hidden Layer (64)").scale(0.5).next_to(hidden_layer2, UP)
        output_label = Text("Output Layer (10)").scale(0.5).next_to(output_layer, RIGHT).shift(RIGHT *0.25)

        
        connections = VGroup()
        for l1, l2 in [(input_layer, hidden_layer1), (hidden_layer1, hidden_layer2), (hidden_layer2, output_layer)]:
            for neuron1 in l1:
                for neuron2 in l2:
                    connections.add(Line(neuron1.get_right(), neuron2.get_left(), stroke_width=1.2, color=WHITE))

        title = Text("Multi Layer Perceptron").scale(0.8).to_edge(UP)
        self.play(Write(title))
        
        network_group = VGroup(input_layer, hidden_layer1, hidden_layer2, output_layer, 
                       input_label, hidden_label1, hidden_label2, output_label, 
                       dots_before, dots_after, output_labels, connections, input_values)
        
        network_group.shift(DOWN* 0.65, RIGHT*0.25)
        
        self.play(FadeIn(input_layer, hidden_layer1, hidden_layer2, output_layer, 
                         input_label, hidden_label1, hidden_label2, output_label, dots_before, dots_after, output_labels, input_values))
        self.play(Create(connections), run_time=1)
        
        self.play(*[neuron.animate.set_fill(ORANGE) for neuron in input_layer], run_time=1)
        self.play(*[neuron.animate.set_fill(YELLOW) for neuron in hidden_layer1], run_time=1)
        self.play(*[neuron.animate.set_fill(GREEN) for neuron in hidden_layer2], run_time=1)
        self.play(*[neuron.animate.set_fill(RED) for neuron in output_layer], run_time=1)

        self.play(FadeOut(network_group))
        self.next_animation()
        

    def next_animation(self):
        input_layer = VGroup(*[Circle(radius=0.2, color=BLUE) for _ in range(10)]).arrange(DOWN, buff=0.3).shift(LEFT * 4)
        input_values = VGroup(
            Text("X₁").scale(0.6).next_to(input_layer[0], LEFT, buff=0.2),
            Text("X₂").scale(0.6).next_to(input_layer[1], LEFT, buff=0.2),
            Text("X₃").scale(0.6).next_to(input_layer[2], LEFT, buff=0.2),
            Text("X₄").scale(0.6).next_to(input_layer[3], LEFT, buff=0.2),
            Text("X₅").scale(0.6).next_to(input_layer[4], LEFT, buff=0.2),
            Text("X₆").scale(0.6).next_to(input_layer[5], LEFT, buff=0.2),
            Text("(...)").scale(0.6).next_to(input_layer[6], LEFT, buff=0.2),
            Text("X_{D-2}").scale(0.6).next_to(input_layer[7], LEFT, buff=0.2),
            Text("X_{D-1}").scale(0.6).next_to(input_layer[8], LEFT, buff=0.2),
            Text("X_D").scale(0.6).next_to(input_layer[9], LEFT, buff=0.2),
        )
        input_label = Text("Input Layer (784)").scale(0.5).next_to(input_layer, LEFT).shift(LEFT *0.5)
        
        input_value = ImageMobject("input_value.png")
        input_value.scale(0.5)
        input_value.to_edge(LEFT)
        
        image_text = Text("28 x 28 Image\nTransformed\nto 784 Pixels").scale(0.5).next_to(input_value, UP).shift(RIGHT *0.25)
        
        neural_layer = VGroup(input_layer, input_values, input_label)
        neural_layer.shift(DOWN* 0.65, RIGHT*0.25)
        
        self.play(FadeIn(neural_layer))
        self.play(FadeIn(input_value))
        self.play(FadeIn(image_text))
        
        for neuron in input_layer:
            self.play(neuron.animate.set_color(ORANGE), run_time=0.3)

        for _ in range(2):
            self.play(*[neuron.animate.set_color(YELLOW) for neuron in input_layer], run_time=0.3)
            self.play(*[neuron.animate.set_color(ORANGE) for neuron in input_layer], run_time=0.3)
            
            
        hidden_layer1 = VGroup(*[Circle(radius=0.2, color=GREEN) for _ in range(8)]).arrange(DOWN, buff=0.4).shift(LEFT * 2)
        hidden_label1 = Text("Hidden Layer (128)").scale(0.5).next_to(hidden_layer1, UP)
        
        self.play(FadeIn(VGroup(hidden_layer1, hidden_label1).shift(DOWN *0.65)))
        
        connections = VGroup()
        for l1, l2 in [(input_layer, hidden_layer1)]:
            for neuron1 in l1:
                for neuron2 in l2:
                    connections.add(Line(neuron1.get_right(), neuron2.get_left(), stroke_width=1.2, color=WHITE))
        
        self.play(FadeIn(connections))
        
        for connection in connections:
            self.play(
                connection.animate.set_stroke(width=6, color=YELLOW),  
                run_time=0.2
            )
            self.play(
                connection.animate.set_stroke(width=1.2, color=WHITE), 
                run_time=0.2
            )
            
        hidden_layer2 = VGroup(*[Circle(radius=0.2, color=YELLOW) for _ in range(7)]).arrange(DOWN, buff=0.5).shift(RIGHT * 1.5)
        hidden_label2 = Text("Hidden Layer (64)").scale(0.5).next_to(hidden_layer2, UP)
        
        self.play(FadeIn(VGroup(hidden_layer2, hidden_label2).shift(DOWN *0.65)))
        
        connections1 = VGroup()
        for l1, l2 in [(hidden_layer1, hidden_layer2)]:
            for neuron1 in l1:
                for neuron2 in l2:
                    connections1.add(Line(neuron1.get_right(), neuron2.get_left(), stroke_width=1.2, color=WHITE))
        
        self.play(FadeIn(connections1))
        
        for connection in connections1:
            self.play(
                connection.animate.set_stroke(width=6, color=BLUE),  
                run_time=0.2
            )
            self.play(
                connection.animate.set_stroke(width=1.2, color=WHITE), 
                run_time=0.2
            )
            
        output_layer = VGroup(*[Circle(radius=0.2, color=RED) for _ in range(3)]).arrange(DOWN, buff=0.7).shift(RIGHT * 3.5)
        dots_before = VGroup(*[Dot(radius=0.04) for _ in range(3)]).arrange(DOWN, buff=0.1).next_to(output_layer[0], DOWN *0.5)
        dots_after = VGroup(*[Dot(radius=0.04) for _ in range(3)]).arrange(DOWN, buff=0.1).next_to(output_layer[1], DOWN * 0.5)
        
        output_labels = VGroup(
            Text("0").scale(0.6).next_to(output_layer[0], RIGHT, buff=0.2),
            Text("5").scale(0.6).next_to(output_layer[1], RIGHT, buff=0.2),
            Text("9").scale(0.6).next_to(output_layer[2], RIGHT, buff=0.2),
        )
        output_label = Text("Output Layer (10)").scale(0.5).next_to(output_layer, RIGHT).shift(RIGHT *0.25)
        
        self.play(FadeIn(VGroup(output_layer, dots_before, dots_after, output_labels, output_label).shift(DOWN* 0.65, RIGHT*0.25)))

        connections2 = VGroup()
        for l1, l2 in [(hidden_layer2, output_layer)]:
            for neuron1 in l1:
                for neuron2 in l2:
                    connections2.add(Line(neuron1.get_right(), neuron2.get_left(), stroke_width=1.2, color=WHITE))
        
        
        self.play(FadeIn(connections2))
        
        for connection in connections2:
            self.play(
                connection.animate.set_stroke(width=6, color=RED),  
                run_time=0.2
            )
            self.play(
                connection.animate.set_stroke(width=1.2, color=WHITE), 
                run_time=0.2
            )
            
        output_values = [0.05, 0.83, 0.05]
        
        output_texts = VGroup(*[
            Text(str(value)).scale(0.2).move_to(neuron)
            for neuron, value in zip(output_layer, output_values)
        ])
        self.play(FadeIn(output_texts))
        
        self.play(FadeOut(neural_layer, input_value, image_text, hidden_layer1, hidden_label1, connections,connections1, connections2, hidden_layer2, hidden_label2, output_layer, dots_before, dots_after, output_labels, output_label, output_texts))

        self.last_animation()
    
    def last_animation(self,):
        output_layer = VGroup(*[Circle(radius=0.3, color=RED) for _ in range(10)]).arrange(RIGHT, buff=0.7)
        
        txt_header = Text(
            "The values in the neurons are probabilities, where if you sum them all up,\n"
            "you obtain the value 1. Each neuron indicates a class, and in this case,\n"
            "the numbers range from 0 to 9."
        ).scale(0.5).move_to(ORIGIN).next_to(output_layer, UP * 4)
        
        output_values = [0.05, 0.05, 0.05, 0.05, 0.83, 0.05, 0.05, 0.05, 0.05, 0.05]
        
        labels = list(range(0, 10))
        
        output_label = Text("Output Layer (10)").scale(0.5).next_to(output_layer, DOWN)
        
        output_texts = VGroup(*[
            Text(str(value)).scale(0.3).move_to(neuron)
            for neuron, value in zip(output_layer, output_values)
        ])
        
        output_labels = VGroup(*[
            Text(str(value)).scale(0.3).move_to(neuron).shift(UP)
            for neuron, value in zip(output_layer, labels)
        ])
        
        self.play(FadeIn(txt_header,output_label,output_layer,output_texts, output_labels))
        
        txt = Text(
            "In a Neural network for multi-classification, the Softmax function is applied to the logits to convert\n"
            "them into probability. Then the Argmax function selects the index with the highest probability,\n"
            "determining the predicted class."
        ).scale(0.5).move_to(ORIGIN).next_to(output_label, DOWN) 
        self.play(FadeIn(txt))       
        
        predicted_output = VGroup(Circle(radius=0.5, color=RED)).next_to(txt, DOWN * 0.25)

        
        predicted_value = Text("0.83").scale(0.5).move_to(predicted_output)

        
        predicted_label = Text("Class: 5").scale(0.4).next_to(predicted_output, DOWN * 0.3)

        input_value = ImageMobject("input_value.png")
        input_value.scale(0.8)
        input_value.next_to(predicted_output, RIGHT * 0.2)

        self.play(FadeIn(predicted_output, predicted_value, predicted_label, input_value))
        self.wait(2)  
        self.play(FadeOut(
        txt_header, output_label, output_layer, output_texts, output_labels, 
        txt, predicted_output, predicted_value, predicted_label, input_value
        ))
        
        good_bye = Text("Thank you for watching.").scale(0.7).move_to(ORIGIN)
        self.play(FadeIn(good_bye))

        


        
        
        
        
        
        
        
        
        
        
        
        
        
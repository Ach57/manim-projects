from manim import *


class BackPropagation(Scene):
    def construct(self):
        self.add_sound("Data_Storm_trimmed.mp3")
        
        title = Text("How is a MLP actually trained?").scale(0.8).to_edge(UP)
        self.play(Write(title))
        
        description = Text(
            "To train a Multi-Layer Perceptron (MLP):\n"
            "   1. Prepare training & testing datasets\n"
            "   2. Define neural network architecture\n"
            "   3. Choose an objective (loss) function\n"
            "   4. Select an optimization algorithm\n"
            "   5. Train using forward & backpropagation\n"
            "   6. Evaluate performance on test data",
            font_size=24
        ).to_edge(LEFT).shift(UP *1.2)
        
        self.play(Write(description))
        
        
        text_above_code = Text("Loading training and testing data...", font_size=24).shift(DOWN*0.5, LEFT*2.55)
        self.play(Write(text_above_code))
        

        df_prep_code = '''import pandas as pd
import numpy as np
import torch

training_df = pd.read_csv("training_minst.csv")
testing_df = pd.read_csv("testing_minst.csv")

X_train = training_df.iloc[:, 1:].values
y_train = training_df.iloc[:, 0].values

X_train = torch.tensor(X_train, dtype=torch.float32) / 255.0
y_train = torch.tensor(y_train, dtype=torch.long)'''
                
        df_prep = Code(
            code_string = df_prep_code,
            language="Python",
            background="window",
            background_config={"stroke_color": "maroon"},
        ).shift(DOWN*2.2, LEFT*2.25).scale(0.5)
        
        self.play(Write(df_prep))
        
        
        model_struct_code = '''model = torch.nn.Sequential(
            torch.nn.Linear(784, 128),
            torch.nn.ReLU(),
            torch.nn.Linear(128,64),
            torch.nn.ReLU(),
            torch.nn.Linear(64,10)
        )
        '''
        
        text_above_model = Text("Model Structure...", font_size=24).shift(UP*2.45, RIGHT*2.35)
        self.play(Write(text_above_model))
        
        model_code = Code(
            code_string= model_struct_code,
            language="Python",
            background="window",
            background_config={"stroke_color": "maroon"}
        ).shift(UP*1.25, RIGHT *2.75).scale(0.5)
            
        self.play(Write(model_code))
        
        
        text_above_loss_optim = Text("Loss and Optimizer", font_size=24).shift(DOWN*1.3, RIGHT*3.1)
        self.play(Write(text_above_loss_optim))
        
        
        
        text_loss_optim = '''loss = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(
    model.parameters(),
    lr = 0.01)'''

        loss_optim_code = Code(
            code_string= text_loss_optim,
            language="Python",
            background="window",
            background_config={"stroke_color": "maroon"},
        ).shift(DOWN*2.2, RIGHT*3.3).scale(0.5)
        
        self.play(Write(loss_optim_code))
        
        self.wait(2)
        
        self.play(FadeOut(VGroup(title,description,text_above_code, df_prep, text_above_model,model_code,text_above_loss_optim, loss_optim_code )))
        
        self.next_animation()
    
    def next_animation(self):
        input_layer  = VGroup(*[Circle(radius=0.2, color = BLUE ) for _ in range(10)]).arrange(DOWN, buff=0.3).shift(LEFT *3.5)
        hidden_layer1 = VGroup(*[Circle(radius= 0.2, color = GREEN) for _ in range( 8)]).arrange(DOWN, buff = 0.4).shift(LEFT*1.5 )
        hidden_layer2 = VGroup(*[Circle(radius=0.2, color=YELLOW) for _ in range(7)]).arrange(DOWN, buff=0.5).shift(RIGHT *1.5)
        output_layer = VGroup(*[Circle(radius=0.2, color=RED) for _ in range(3)]).arrange(DOWN, buff=0.7).shift(RIGHT *3.5)

        
        input_label = Text("Input Layer (784)").scale(0.5).next_to(input_layer, LEFT).shift(LEFT *0.5)
        hidden_label1 = Text("Hidden Layer (128)").scale(0.5).next_to(hidden_layer1, UP). shift(DOWN *0.2)
        hidden_label2 = Text("Hidden Layer (64)").scale(0.5).next_to(hidden_layer2, UP).shift(DOWN *0.2)
        output_label = Text("Output Layer (10)").scale(0.5).next_to(output_layer, RIGHT).shift(RIGHT *0.25)
        
        dots_before = VGroup(*[Dot(radius=0.04) for _ in range(3)]).arrange(DOWN, buff=0.1).next_to(output_layer[0], DOWN *0.5)
        dots_after = VGroup(*[Dot(radius=0.04) for _ in range(3)]).arrange(DOWN, buff=0.1).next_to(output_layer[1], DOWN * 0.5)

        
        output_labels = VGroup(
            Text("0").scale(0.6).next_to(output_layer[0], RIGHT, buff=0.2),
            Text("5").scale(0.6).next_to(output_layer[1], RIGHT, buff=0.2),
            Text("9").scale(0.6).next_to(output_layer[2], RIGHT, buff=0.2),
        )
        
        connections = VGroup()
        for l1, l2 in [(input_layer, hidden_layer1), (hidden_layer1, hidden_layer2), (hidden_layer2, output_layer)]:
            for neuron1 in l1:
                for neuron2 in l2:
                    connections.add(Line(neuron1.get_right(), neuron2.get_left(), stroke_width=1.2, color=WHITE))


        title = Text("Multi Layer Perceptron").scale(0.8).to_edge(UP)
        self.play(Write(title))
        
        input_value = ImageMobject("input_label.png")
        input_value.scale(0.5)
        input_value.to_edge(LEFT).shift(UP *0.5, RIGHT *0.2)
        
        image_text = Text("28 x 28 Image\nTransformed\nto 784 Pixels").scale(0.5).next_to(input_value, UP).shift(RIGHT *0.25)
        
        self.play(FadeIn(VGroup(input_layer, hidden_layer1, hidden_layer2, output_layer, connections, 
                                input_label, hidden_label1, hidden_label2, output_label, output_labels,dots_before, dots_after, ).shift( DOWN *0.5)))
        
        self.play(FadeIn(input_value))
        self.play(FadeIn(image_text))
        
        self.play(FadeOut(title))
        
        title = Text("Forward Propagation (Forward Pass)").scale(0.8).to_edge(UP)
        self.play(Write(title))
        
        
        num_repeats = 3  
        #Forward Propagation
        for _ in range(num_repeats):
            signals = VGroup()
            
            for l1, l2 in [(input_layer, hidden_layer1), (hidden_layer1, hidden_layer2), (hidden_layer2, output_layer)]:
                for neuron1 in l1:
                    for neuron2 in l2:
                        signal = Dot(radius=0.05, color=WHITE).move_to(neuron1.get_right())
                        signals.add(signal)

            
            self.play(
                *[signal.animate.move_to(connections[i].get_end()) for i, signal in enumerate(signals)],
                run_time=1 
            )

            self.play(
                *[neuron.animate.set_color(WHITE) for neuron in hidden_layer1],
                *[neuron.animate.set_color(WHITE) for neuron in hidden_layer2],
                *[neuron.animate.set_color(YELLOW) for neuron in output_layer]
            )

            
            self.play(FadeOut(signals))
            
            
        info_txt = Text("Forward propagation\n is first performed\nthen we measure the loss", font_size=24).shift(RIGHT*4.1, DOWN*3)
        
        self.play(Write(info_txt))
        self.wait(1)
        self.play(FadeOut(info_txt))
        
        self.play(FadeOut(title))
        
        title = Text("Back Propagation ").scale(0.8).to_edge(UP)
        self.play(Write(title))
        
        
        num_repeats = 3 
        #BackWard Propagation
        for _ in range(num_repeats):
            signals = VGroup()
            
            for l1, l2 in [(output_layer, hidden_layer2), (hidden_layer2, hidden_layer1), (hidden_layer1, input_layer)]:
                for neuron1 in l1:
                    for neuron2 in l2:
                        signal = Dot(radius=0.05, color=RED).move_to(neuron1.get_left())
                        signals.add(signal)

            self.play(
                *[signal.animate.move_to(connections[i].get_start()) for i, signal in enumerate(signals)],
                run_time=1  
            )

            self.play(
                *[connection.animate.set_color(BLUE) for connection in connections],
                run_time=0.5
            )

            self.play(
                *[connection.animate.set_color(WHITE) for connection in connections],
                run_time=0.5
            )

            self.play(FadeOut(signals))
            

        
        info_txt = Text("Backpropagation helps optimize\n the parameters to find the best fit.", font_size=24).shift(RIGHT*4.4, DOWN*3)
        self.play(Write(info_txt))
        
        self.wait(1)
        self.play(FadeOut(input_value))
        self.play(FadeOut(VGroup(
            input_layer, hidden_layer1, hidden_layer2, output_layer, connections, 
            input_label, hidden_label1, hidden_label2, output_label, output_labels, 
            dots_before, dots_after, image_text, title, info_txt
        )))
        
        good_bye = Text("Thank you for watching.").scale(0.7).move_to(ORIGIN)
        self.play(FadeIn(good_bye))
        
        

        
        
    

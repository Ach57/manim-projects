from manim import *

class GraphSearch(MovingCameraScene):
    def construct(self):
        self.add_sound("output.mp3")
        title = Text("Informed & Uninformed Search").to_edge(UP)
        self.play(FadeIn(title))
    
        nodes = {
            "S": [0, 4, 0], "A": [-2, 2, 0], "B": [2, 2, 0],
            "C": [-4, 2, 0], "D": [-2, 0, 0], "E": [2, 0, 0],
            "G1": [-4, 0, 0], "G2": [4, 2, 0]
        }
        
        edges = [
            ("S","A", 3), ("S","B", 7), ("A", "C", 1),
            ("C", "S", 2), ("A", "D", 6), ("C","D", 4),
            ("D", "G1", 6),("G1", "C", 2), ("D", "B", 3),
            ("B", "G2", 9), ("B", "E", 4),("E", "G2", 5),
        ]
        
        heuristic_values = {
            "S": 10, "A": 5, "B": 8, "C": 3, "D": 2, "E": 2, "G1": 0, "G2": 0
        }
        
        
        graph = DiGraph(
            list(nodes.keys()),
            [(start, end) for start, end, _ in edges],
            layout = nodes,
            edge_config={
                "stroke_width": 1.5,
                "tip_length": 0.1
            },
            vertex_config= {"radius": 0.3, "fill_color":RED}
        ).move_to(DOWN*0.25).scale(0.8)
        
        node_labels = VGroup(
            *[Text(name, font_size=22).move_to(graph[name].get_center()) for name in nodes]
        )
        
        heuristic_labels = VGroup(
                *[
                    Text(str(heuristic_values[node]), font_size=20, color=YELLOW)
                    .move_to(
                        graph[node].get_center() + UP * 0.5 if node in ['S','A', 'C', 'B', 'G2', ] else
                        graph[node].get_center() + LEFT *0.5  if node in ['G1', 'E'] else
                        graph[node].get_center() + RIGHT *0.5 
                        )
                    for node in nodes
                ]
            )
        
        edge_labels = VGroup()
        
        
        for start, end, weight in edges:
            mid_point = (graph[start].get_center() + graph[end].get_center()) / 2
            edge_labels.add(Text(str(weight), font_size=20, color=BLUE)
                            .move_to(mid_point, DOWN*2.8 if not( (start, end) in [('B','E'),('A','D'),('G1','C')] ) else
                                     RIGHT*2.7)
            )
        
        self.play(Create(graph))
        self.play(FadeIn(node_labels))
        self.play(FadeIn(heuristic_labels))
        self.play(FadeIn(edge_labels))
        
        self.wait(1)
        
        self.play(
            Create(graph.shift(LEFT*3 + UP*0.85)),  
            FadeIn(node_labels.shift(LEFT*3 + UP*0.85)),
            FadeIn(heuristic_labels.shift(LEFT*3 + UP*0.85)),
            FadeIn(edge_labels.shift(LEFT*3 + UP*0.85))
        )
        
        self.wait(1)
        
        uninformed_txt = Text(
            "Uninformed Search (Blind Search)\n"
            "1. Breadth-First Search (BFS)\n"
            "2. Depth-First Search (DFS)\n"
            "3. Uniform Cost Search (UCS)",
            font_size=24
        ).to_edge(RIGHT).shift(UP * 1) 
        self.play(FadeIn(uninformed_txt))
        
        informed_txt = Text(
            "Informed Search (Heuristic Search)\n"
            "1. Vanilla Hill Climbing\n"
            "2. Greedy-Best first search\n"
            "3. Algorithm A",
            font_size=24
        ).to_edge(RIGHT).shift(DOWN ) 
        self.play(FadeIn(informed_txt))
        
        
        clarification_txt = Text(
            "Yellow values indicate Heuristic value of each node => h(S) = 10\n"
            "Blue values indicate the path value => g(A) = 5 (S->A)", font_size=24
        ).to_edge(DOWN)
        self.play(FadeIn(clarification_txt))
        self.wait(1)
        self.play(FadeOut(clarification_txt, informed_txt, uninformed_txt, graph, node_labels, heuristic_labels,edge_labels, title))
        self.next_animation()
        
        
    def next_animation(self):
        title = Text("Breadth-First Search").to_edge(UP)
        self.play(FadeIn(title))
        
        nodes = {
            "S": [0, 4, 0], "A": [-2, 2, 0], "B": [2, 2, 0],
            "C": [-4, 2, 0], "D": [-2, 0, 0], "E": [2, 0, 0],
            "G1": [-4, 0, 0], "G2": [4, 2, 0]
        }
        edges = [
            ("S","A", 3), ("S","B", 7), ("A", "C", 1),
            ("C", "S", 2), ("A", "D", 6), ("C","D", 4),
            ("D", "G1", 6),("G1", "C", 2), ("D", "B", 3),
            ("B", "G2", 9), ("B", "E", 4),("E", "G2", 5),
        ]
        
        graph = DiGraph(
            list(nodes.keys()),
            [(start, end) for start, end, _ in edges],
            layout = nodes,
            edge_config={
                "stroke_width": 1.5,
                "tip_length": 0.1
            },
            vertex_config= {"radius": 0.3, "fill_color":RED}
        ).move_to(DOWN*0.25,).scale(0.8)
        
        node_labels = VGroup(
            *[Text(name, font_size=22).move_to(graph[name].get_center()) for name in nodes]
        )
        self.play(Create(graph.shift(LEFT*3 + UP*0.85)),
                  FadeIn(node_labels.shift(LEFT*3 + UP*0.85)))
        
        
        uninformed_txt = Text(
            "In BFS, the path cost and heuristic value don't matter\n"
            "Goal Nodes are G1 or G2",
            font_size=24
        ).to_edge(RIGHT).shift(UP * 1.4) 
        self.play(FadeIn(uninformed_txt))
        
        highlighted_edges = VGroup()
        txt = Text("Queue = [ (S) ]", font_size=24).shift(DOWN*1, RIGHT)
        self.play(FadeIn(txt))
        
        highlighted_edges.add(Line(graph['S'], graph['A'], color = ORANGE, ).add_tip(tip_length=0.1, tip_width=0.1))
        self.play(highlighted_edges[0].animate.set_color(ORANGE)) 
        
        highlighted_edges.add(Line(graph['S'], graph['B'], color = ORANGE, ).add_tip(tip_length=0.1, tip_width=0.1))
        self.play(highlighted_edges[1].animate.set_color(ORANGE)) 
        
        self.play(FadeOut(txt))
        txt = Text("Queue = [ (S) (A) (B) ]", font_size=24).shift(DOWN*1, RIGHT*1.2)
        self.play(FadeIn(txt))
        
        highlighted_edges.add(Line(graph['A'], graph['C'], color = ORANGE, ).add_tip(tip_length=0.1, tip_width=0.1))
        self.play(highlighted_edges[2].animate.set_color(ORANGE)) 
        
        highlighted_edges.add(Line(graph['A'], graph['D'], color = ORANGE, ).add_tip(tip_length=0.1, tip_width=0.1))
        self.play(highlighted_edges[3].animate.set_color(ORANGE)) 
        
        self.play(FadeOut(txt))
        txt = Text("Queue = [ (S) (A) (B) (C) (D) ]", font_size=24).shift(DOWN*1, RIGHT*1.7)
        self.play(FadeIn(txt))
        
        highlighted_edges.add(Line(graph['B'], graph['E'], color = ORANGE, ).add_tip(tip_length=0.1, tip_width=0.1))
        self.play(highlighted_edges[4].animate.set_color(ORANGE)) 
        
        highlighted_edges.add(Line(graph['B'], graph['G2'], color = ORANGE, ).add_tip(tip_length=0.1, tip_width=0.1))
        self.play(highlighted_edges[5].animate.set_color(ORANGE)) 
        
        self.play(FadeOut(txt))
        txt = Text("Queue = [ (S) (A) (B) (C) (D) (E) (G2) ]\n"
                   "Goal Found at G2", font_size=24).shift(DOWN*1, RIGHT*2)
        self.play(FadeIn(txt))
                
        self.wait(1)
        
        self.play(FadeOut(txt, title,graph, highlighted_edges, node_labels, uninformed_txt ))
        self.dfs_animation()
    
    def dfs_animation(self):
        title = Text("Depth-First Search").to_edge(UP)
        self.play(FadeIn(title))
        
        nodes = {
            "S": [0, 4, 0], "A": [-2, 2, 0], "B": [2, 2, 0],
            "C": [-4, 2, 0], "D": [-2, 0, 0], "E": [2, 0, 0],
            "G1": [-4, 0, 0], "G2": [4, 2, 0]
        }
        edges = [
            ("S","A", 3), ("S","B", 7), ("A", "C", 1),
            ("C", "S", 2), ("A", "D", 6), ("C","D", 4),
            ("D", "G1", 6),("G1", "C", 2), ("D", "B", 3),
            ("B", "G2", 9), ("B", "E", 4),("E", "G2", 5),
        ]
        
        graph = DiGraph(
            list(nodes.keys()),
            [(start, end) for start, end, _ in edges],
            layout = nodes,
            edge_config={
                "stroke_width": 1.5,
                "tip_length": 0.1
            },
            vertex_config= {"radius": 0.3, "fill_color":RED}
        ).move_to(DOWN*0.25,).scale(0.8)
        
        node_labels = VGroup(
            *[Text(name, font_size=22).move_to(graph[name].get_center()) for name in nodes]
        )
        self.play(Create(graph.shift(LEFT*3 + UP*0.85)),
                  FadeIn(node_labels.shift(LEFT*3 + UP*0.85)))
        
        
        uninformed_txt = Text(
            "In DFS, the path cost and heuristic value don't matter\n"
            "Goal Nodes are G1 or G2",
            font_size=24
        ).to_edge(RIGHT).shift(UP * 1.4) 
        self.play(FadeIn(uninformed_txt))
        
        
        highlighted_edges = VGroup()
        
        highlighted_edges.add(Line(graph['S'], graph['A'], color = ORANGE, ).add_tip(tip_length=0.1, tip_width=0.1))
        self.play(highlighted_edges[0].animate.set_color(ORANGE)) 
        
        highlighted_edges.add(Line(graph['A'], graph['C'], color = ORANGE, ).add_tip(tip_length=0.1, tip_width=0.1))
        self.play(highlighted_edges[1].animate.set_color(ORANGE)) 
        
        highlighted_edges.add(Line(graph['C'], graph['D'], color = ORANGE, ).add_tip(tip_length=0.1, tip_width=0.1))
        self.play(highlighted_edges[2].animate.set_color(ORANGE)) 
        
        highlighted_edges.add(Line(graph['D'], graph['G1'], color = ORANGE, ).add_tip(tip_length=0.1, tip_width=0.1))
        self.play(highlighted_edges[3].animate.set_color(ORANGE)) 
        
    
        txt = Text("Search Path: S A C D G1\n"
                   "Goal found at Node G1", font_size=24).shift(DOWN*1, RIGHT*1.7)
        self.play(FadeIn(txt))
        self.wait(0.5)
        
        self.play(FadeOut(txt, graph, node_labels, title, highlighted_edges, uninformed_txt))
        self.ucs_animation()
        
    def ucs_animation(self):
        
        title = Text("Uniform-Cost Search").to_edge(UP)
        self.play(FadeIn(title))
        
        nodes = {
            "S": [0, 4, 0], "A": [-2, 2, 0], "B": [2, 2, 0],
            "C": [-4, 2, 0], "D": [-2, 0, 0], "E": [2, 0, 0],
            "G1": [-4, 0, 0], "G2": [4, 2, 0]
        }
        edges = [
            ("S","A", 3), ("S","B", 7), ("A", "C", 1),
            ("C", "S", 2), ("A", "D", 6), ("C","D", 4),
            ("D", "G1", 6),("G1", "C", 2), ("D", "B", 3),
            ("B", "G2", 9), ("B", "E", 4),("E", "G2", 5),
        ]
        
        graph = DiGraph(
            list(nodes.keys()),
            [(start, end) for start, end, _ in edges],
            layout = nodes,
            edge_config={
                "stroke_width": 1.5,
                "tip_length": 0.1
            },
            vertex_config= {"radius": 0.3, "fill_color":RED}
        ).move_to(DOWN*0.25,).scale(0.8)
        
        node_labels = VGroup(
            *[Text(name, font_size=22).move_to(graph[name].get_center()) for name in nodes]
        )
        
        edge_labels = VGroup()
        
        
        for start, end, weight in edges:
            mid_point = (graph[start].get_center() + graph[end].get_center()) / 2
            edge_labels.add(Text(str(weight), font_size=20, color=BLUE)
                            .move_to(mid_point, DOWN*2.8 if not( (start, end) in [('B','E'),('A','D'),('G1','C')] ) else
                                     RIGHT*2.7)
            )
            
        self.play(Create(graph.shift(LEFT*3 + UP*0.85)),
                  FadeIn(node_labels.shift(LEFT*3 + UP*0.85)),
                  FadeIn(edge_labels.shift(LEFT*3 + UP*0.85))
        )
        
        uninformed_txt = Text(
            "In UCS, the path cost matters but heuristic value don't matter\n"
            "Goal Nodes are G1 or G2",
            font_size=24
        ).to_edge(RIGHT).shift(UP * 1.4) 
        self.play(FadeIn(uninformed_txt))
        
        self.play(FadeOut(uninformed_txt))
        
        table = Table(
            [["Node", "Cost from Start", "Parent Node"],
             ["S", "0", "-"],
             ["A", "∞", "-"],
             ["B", "∞", "-"],
             ["C", "∞", "-"],
             ["D", "∞", "-"],
             ["E", "∞", "-"],
             ["G1", "∞", "-"],
             ["G2", "∞", "-"]]
        ).shift(UP, RIGHT*3).scale(0.25)

        
        self.play(Create(table))

        
        highlighted_edges = VGroup()
        highlighted_edges.add(Line(graph['S'], graph['A'], color = ORANGE, ).add_tip(tip_length=0.1, tip_width=0.1))
        self.play(highlighted_edges[0].animate.set_color(ORANGE)) 
        
        highlighted_edges.add(Line(graph['S'], graph['B'], color = ORANGE, ).add_tip(tip_length=0.1, tip_width=0.1))
        self.play(highlighted_edges[1].animate.set_color(ORANGE)) 
        
        self.play(FadeOut(table))
        
        table = Table(
            [["Node", "Cost from Start", "Parent Node"],
             ["S", "0", "-"],
             ["A", "3", "S"],
             ["B", "7", "S"],
             ["C", "∞", "-"],
             ["D", "∞", "-"],
             ["E", "∞", "-"],
             ["G1", "∞", "-"],
             ["G2", "∞", "-"]]
        ).shift(UP, RIGHT*3).scale(0.25)
        self.play(Create(table))
        table.add_highlighted_cell((3,2), color=BLUE)
        table.add_highlighted_cell((3,3), color=BLUE)
        table.add_highlighted_cell((4,2), color=BLUE)
        table.add_highlighted_cell((4,3), color=BLUE)
        
        self.wait(1)
        self.play(FadeOut(table))
        
        table = Table(
            [["Node", "Cost from Start", "Parent Node"],
             ["S", "0", "-"],
             ["A", "3", "S"],
             ["B", "7", "S"],
             ["C", "4", "A"],
             ["D", "9", "A"],
             ["E", "∞", "-"],
             ["G1", "∞", "-"],
             ["G2", "∞", "-"]]
        ).shift(UP, RIGHT*3).scale(0.25)
        
        self.play(Create(table))
        
        table.add_highlighted_cell((5,2), color=ORANGE)
        table.add_highlighted_cell((5,3), color=ORANGE)
        table.add_highlighted_cell((6,2), color=ORANGE)
        table.add_highlighted_cell((6,3), color=ORANGE)
        
        self.wait(0.25)
        
        highlighted_edges.add(Line(graph['A'], graph['C'], color = ORANGE, ).add_tip(tip_length=0.1, tip_width=0.1))
        self.play(highlighted_edges[2].animate.set_color(ORANGE)) 
        
        
        self.wait(0.25)
        self.play(FadeOut(table))
        
        table = Table(
            [["Node", "Cost from Start", "Parent Node"],
             ["S", "0", "-"],
             ["A", "3", "S"],
             ["B", "7", "S"],
             ["C", "4", "A"],
             ["D", "8", "C"],
             ["E", "11", "B"],
             ["G1", "∞", "-"],
             ["G2", "15", "B"]]
        ).shift(UP, RIGHT*3).scale(0.25)
        
        self.play(Create(table))
        
        highlighted_edges.add(Line(graph['C'], graph['D'], color = ORANGE, ).add_tip(tip_length=0.1, tip_width=0.1))
        self.play(highlighted_edges[3].animate.set_color(ORANGE)) 
        
        table.add_highlighted_cell((6,2), color=RED)
        table.add_highlighted_cell((6,3), color=RED)
        table.add_highlighted_cell((7,2), color=RED)
        table.add_highlighted_cell((7,3), color=RED)
        table.add_highlighted_cell((9,2), color=RED)
        table.add_highlighted_cell((9,3), color=RED)
        
        highlighted_edges.add(Line(graph['B'], graph['E'], color = ORANGE, ).add_tip(tip_length=0.1, tip_width=0.1))
        self.play(highlighted_edges[4].animate.set_color(ORANGE)) 
        
        self.wait(0.25)
        self.play(FadeOut(table))
        
        
        table = Table(
            [["Node", "Cost from Start", "Parent Node"],
             ["S", "0", "-"],
             ["A", "3", "S"],
             ["B", "7", "S"],
             ["C", "4", "A"],
             ["D", "8", "C"],
             ["E", "11", "B"],
             ["G1", "14", "D"],
             ["G2", "15", "B"]]
        ).shift(UP, RIGHT*3).scale(0.25)
        self.play(FadeIn(table))
        highlighted_edges.add(Line(graph['D'], graph['G1'], color = ORANGE, ).add_tip(tip_length=0.1, tip_width=0.1))
        self.play(highlighted_edges[5].animate.set_color(ORANGE)) 
        
        table.add_highlighted_cell((8,3), color=GREEN)
        table.add_highlighted_cell((8,2), color=GREEN)
        
        txt = Text("Search Path: S A C B D E G2\n"
                   "Goal found at Node G2", font_size=24).shift(DOWN*1, RIGHT)
        self.play(FadeIn(txt))
        self.wait(0.75)
        
        self.play(FadeOut(table, txt, graph, node_labels, edge_labels, highlighted_edges, title))
        self.vanilla_hc_animation()
        
        
    def vanilla_hc_animation(self,):
        title = Text("Vanilla Hill Climbing").to_edge(UP)
        self.play(FadeIn(title))
        
        
        nodes = {
            "S": [0, 4, 0], "A": [-2, 2, 0], "B": [2, 2, 0],
            "C": [-4, 2, 0], "D": [-2, 0, 0], "E": [2, 0, 0],
            "G1": [-4, 0, 0], "G2": [4, 2, 0]
        }
        edges = [
            ("S","A", 3), ("S","B", 7), ("A", "C", 1),
            ("C", "S", 2), ("A", "D", 6), ("C","D", 4),
            ("D", "G1", 6),("G1", "C", 2), ("D", "B", 3),
            ("B", "G2", 9), ("B", "E", 4),("E", "G2", 5),
        ]
        
        graph = DiGraph(
            list(nodes.keys()),
            [(start, end) for start, end, _ in edges],
            layout = nodes,
            edge_config={
                "stroke_width": 1.5,
                "tip_length": 0.1
            },
            vertex_config= {"radius": 0.3, "fill_color":RED}
        ).move_to(DOWN*0.25,).scale(0.8)
        
        node_labels = VGroup(
            *[Text(name, font_size=22).move_to(graph[name].get_center()) for name in nodes]
        )
        
        heuristic_values = {
            "S": 10, "A": 5, "B": 8, "C": 3, "D": 2, "E": 2, "G1": 0, "G2": 0
        }
        heuristic_labels = VGroup(
                *[
                    Text(str(heuristic_values[node]), font_size=20, color=YELLOW)
                    .move_to(
                        graph[node].get_center() + UP * 0.5 if node in ['S','A', 'C', 'B', 'G2', ] else
                        graph[node].get_center() + LEFT *0.5  if node in ['G1', 'E'] else
                        graph[node].get_center() + RIGHT *0.5 
                        )
                    for node in nodes
                ]
            )
        
        
        self.play(Create(graph.shift(LEFT*3 + UP*0.85)),
                  FadeIn(node_labels.shift(LEFT*3 + UP*0.85)),
                  FadeIn(heuristic_labels.shift(LEFT*3 + UP*0.85))
        )
        
        
        uninformed_txt = Text(
            "In HC, only the heuristic value matters\n"
            "Goal Nodes are G1 or G2",
            font_size=24
        ).to_edge(RIGHT).shift(UP * 1.4) 
        self.play(FadeIn(uninformed_txt))
        self.wait(0.25)
        self.play(FadeOut(uninformed_txt))
        
        uninformed_txt = Text(
            "With hill climbing,\n"
            "we start with the initial node S.\n"
            "h(S) = 10, and we start by selecting\n the first lowest heuristic neighbor",
            font_size=24
        ).to_edge(RIGHT* 2).shift(UP * 1.4)
                
        self.play(FadeIn(uninformed_txt))
        
        highlighted_edges = VGroup()
        self.wait(0.25)
        highlighted_edges.add(Line(graph['S'], graph['A'], color = ORANGE, ).add_tip(tip_length=0.1, tip_width=0.1))
        self.play(highlighted_edges[0].animate.set_color(ORANGE)) 
        
        highlighted_edges.add(Line(graph['A'], graph['D'], color = ORANGE, ).add_tip(tip_length=0.1, tip_width=0.1))
        self.play(highlighted_edges[1].animate.set_color(ORANGE)) 
        
        highlighted_edges.add(Line(graph['D'], graph['G1'], color = ORANGE, ).add_tip(tip_length=0.1, tip_width=0.1))
        self.play(highlighted_edges[2].animate.set_color(ORANGE)) 
        
        self.play(FadeOut(uninformed_txt))
        
        
        uninformed_txt = Text(
            "Search Path: S A C D G1\n"
            "Goal node G1 found",
            font_size=24
        ).shift(UP * 1.4, RIGHT*2.3)
                
        self.play(FadeIn(uninformed_txt))
        
        self.wait(0.25)
        self.play(FadeOut(uninformed_txt, graph, heuristic_labels, node_labels, highlighted_edges, title))
        
        self.greedy_best_animation()
        
    def greedy_best_animation(self):
        title = Text("Greedy-Best First Search").to_edge(UP)
        self.play(FadeIn(title))
        
        nodes = {
            "S": [0, 4, 0], "A": [-2, 2, 0], "B": [2, 2, 0],
            "C": [-4, 2, 0], "D": [-2, 0, 0], "E": [2, 0, 0],
            "G1": [-4, 0, 0], "G2": [4, 2, 0]
        }
        edges = [
            ("S","A", 3), ("S","B", 7), ("A", "C", 1),
            ("C", "S", 2), ("A", "D", 6), ("C","D", 4),
            ("D", "G1", 6),("G1", "C", 2), ("D", "B", 3),
            ("B", "G2", 9), ("B", "E", 4),("E", "G2", 5),
        ]
        
        graph = DiGraph(
            list(nodes.keys()),
            [(start, end) for start, end, _ in edges],
            layout = nodes,
            edge_config={
                "stroke_width": 1.5,
                "tip_length": 0.1
            },
            vertex_config= {"radius": 0.3, "fill_color":RED}
        ).move_to(DOWN*0.25,).scale(0.8)
        
        node_labels = VGroup(
            *[Text(name, font_size=22).move_to(graph[name].get_center()) for name in nodes]
        )
        
        heuristic_values = {
            "S": 10, "A": 5, "B": 8, "C": 3, "D": 2, "E": 2, "G1": 0, "G2": 0
        }
        heuristic_labels = VGroup(
                *[
                    Text(str(heuristic_values[node]), font_size=20, color=YELLOW)
                    .move_to(
                        graph[node].get_center() + UP * 0.5 if node in ['S','A', 'C', 'B', 'G2', ] else
                        graph[node].get_center() + LEFT *0.5  if node in ['G1', 'E'] else
                        graph[node].get_center() + RIGHT *0.5 
                        )
                    for node in nodes
                ]
            )
        
        
        self.play(Create(graph.shift(LEFT*3 + UP*0.85)),
                  FadeIn(node_labels.shift(LEFT*3 + UP*0.85)),
                  FadeIn(heuristic_labels.shift(LEFT*3 + UP*0.85))
        )
        
        uninformed_txt = Text(
            "In GBS, only the heuristic value matters\n"
            "Goal Nodes are G1 or G2",
            font_size=24
        ).to_edge(RIGHT).shift(UP * 1.4) 
        self.play(FadeIn(uninformed_txt))
        self.wait(0.25)
        self.play(FadeOut(uninformed_txt))
        
        uninformed_txt = Text(
            "With Greedy Best First Search,\n"
            "We use an Open & Closed list.\n"
            "We pick the best-looking option h(n)",
            font_size=24
        ).to_edge(RIGHT* 2).shift(UP * 1.4)
                
        self.play(FadeIn(uninformed_txt))
        
        self.wait(0.25)
        self.play(FadeOut(uninformed_txt))
        
        table = Table(
            [["Open", "Closed", "Heuristic value"],
             ["S", "    ", "10"],
             ]
        ).shift(UP, RIGHT*3).scale(0.25)
        
        self.play(Create(table))
        
        self.wait(0.25)
        
        self.play(FadeOut(table))
        table = Table(
            [["Open", "Closed", "Heuristic value"],
             ["S", "    ", "10"],
             ["A", "S", "5"],
             ]
        ).shift(UP, RIGHT*3).scale(0.25)
        self.play(Create(table))
        
        table.add_highlighted_cell((3,1), color=RED)
        table.add_highlighted_cell((3,2), color=RED)
        table.add_highlighted_cell((3,3), color=RED)
        
        
        highlighted_edges = VGroup()
        self.wait(0.25)
        highlighted_edges.add(Line(graph['S'], graph['A'], color = ORANGE, ).add_tip(tip_length=0.1, tip_width=0.1))
        self.play(highlighted_edges[0].animate.set_color(ORANGE)) 
        
        
        self.play(FadeOut(table))
        
        
        table = Table(
            [["Open", "Closed", "Heuristic value"],
             ["S", "    ", "10"],
             ["A, B", "S", "5, 8"],
             ['D, C, B', "S, A", "2, 3, 5"]
             ]
        ).shift(UP, RIGHT*3).scale(0.25)
        self.play(Create(table))
        
        table.add_highlighted_cell((4,1), color=RED)
        table.add_highlighted_cell((4,2), color=RED)
        table.add_highlighted_cell((4,3), color=RED)
        self.wait(0.25)
        highlighted_edges.add(Line(graph['A'], graph['D'], color = ORANGE, ).add_tip(tip_length=0.1, tip_width=0.1))
        self.play(highlighted_edges[1].animate.set_color(ORANGE)) 
        
        self.wait(0.25)
        
        self.play(FadeOut(table))
        
        
        table = Table(
            [["Open", "Closed", "Heuristic value"],
             ["S", "    ", "10"],
             ["A, B", "S", "5, 8"],
             ['D, C, B', "S, A", "2, 3, 5"],
             ['G1, C, B', "S, A, D", "0, 3, 5"]
             ]
        ).shift(UP, RIGHT*3).scale(0.25)
        self.play(Create(table))
        
        table.add_highlighted_cell((5,1), color=RED)
        table.add_highlighted_cell((5,2), color=RED)
        table.add_highlighted_cell((5,3), color=RED)
        self.wait(0.25)
        
        highlighted_edges.add(Line(graph['D'], graph['G1'], color = ORANGE, ).add_tip(tip_length=0.1, tip_width=0.1))
        self.play(highlighted_edges[2].animate.set_color(ORANGE)) 
        
        self.play(FadeOut(table))
        self.wait(0.25)
        
        table = Table(
            [["Open", "Closed", "Heuristic value"],
             ["S", "    ", "10"],
             ["A, B", "S", "5, 8"],
             ['D, C, B', "S, A", "2, 3, 5"],
             ['G1, C, B', "S, A, D", "0, 3, 5"],
             ['C, B', "S, A, D, G1", "3, 5"]
             ]
        ).shift(UP, RIGHT*3).scale(0.25)
        self.play(Create(table))
        
        table.add_highlighted_cell((6,2), color=GREEN)
        self.wait(0.25)
        
        self.play(FadeOut(title, graph, heuristic_labels, table, highlighted_edges, node_labels))
        self.algorithm_a_animation()
        
    def algorithm_a_animation(self):
        
        title = Text("A Algorithm Search").to_edge(UP)
        self.play(FadeIn(title))
        
        nodes = {
            "S": [0, 4, 0], "A": [-2, 2, 0], "B": [2, 2, 0],
            "C": [-4, 2, 0], "D": [-2, 0, 0], "E": [2, 0, 0],
            "G1": [-4, 0, 0], "G2": [4, 2, 0]
        }
        
        edges = [
            ("S","A", 3), ("S","B", 7), ("A", "C", 1),
            ("C", "S", 2), ("A", "D", 6), ("C","D", 4),
            ("D", "G1", 6),("G1", "C", 2), ("D", "B", 3),
            ("B", "G2", 9), ("B", "E", 4),("E", "G2", 5),
        ]
        
        heuristic_values = {
            "S": 10, "A": 5, "B": 8, "C": 3, "D": 2, "E": 2, "G1": 0, "G2": 0
        }
        
        
        graph = DiGraph(
            list(nodes.keys()),
            [(start, end) for start, end, _ in edges],
            layout = nodes,
            edge_config={
                "stroke_width": 1.5,
                "tip_length": 0.1
            },
            vertex_config= {"radius": 0.3, "fill_color":RED}
        ).move_to(DOWN*0.25).scale(0.8)
        
        node_labels = VGroup(
            *[Text(name, font_size=22).move_to(graph[name].get_center()) for name in nodes]
        )
        
        heuristic_labels = VGroup(
                *[
                    Text(str(heuristic_values[node]), font_size=20, color=YELLOW)
                    .move_to(
                        graph[node].get_center() + UP * 0.5 if node in ['S','A', 'C', 'B', 'G2', ] else
                        graph[node].get_center() + LEFT *0.5  if node in ['G1', 'E'] else
                        graph[node].get_center() + RIGHT *0.5 
                        )
                    for node in nodes
                ]
            )
        
        edge_labels = VGroup()
        
        
        for start, end, weight in edges:
            mid_point = (graph[start].get_center() + graph[end].get_center()) / 2
            edge_labels.add(Text(str(weight), font_size=20, color=BLUE)
                            .move_to(mid_point, DOWN*2.8 if not( (start, end) in [('B','E'),('A','D'),('G1','C')] ) else
                                     RIGHT*2.7)
            )
        
        self.play(
            Create(graph.shift(LEFT*3 + UP*0.85)),  
            FadeIn(node_labels.shift(LEFT*3 + UP*0.85)),
            FadeIn(heuristic_labels.shift(LEFT*3 + UP*0.85)),
            FadeIn(edge_labels.shift(LEFT*3 + UP*0.85))
        )
        
        
        uninformed_txt = Text(
            "With Algorithm A, we use f(n),\n"
            "f(n) = h(n) + g(n)\n",
            font_size=24
        ).to_edge(RIGHT).shift(UP * 1.4)
        
        self.play(FadeIn(uninformed_txt))

        self.wait(0.25)    
        
        self.play(FadeOut(uninformed_txt))
        
        table = Table(
            [["Open", "Closed", "f(n) = g(n)+h(n)"],
             ["S", "    ", "0+10"],
             ]
        ).shift(UP, RIGHT*3).scale(0.25)
        self.play(Create(table))
        
        self.wait(0.25)
        self.play(FadeOut(table))
        
        table = Table(
            [["Open", "Closed", "f(n) = g(n)+h(n)"],
             ["S", "    ", "0+10"],
             ["A, B", "S", "8, 15"],
             ]
        ).shift(UP, RIGHT*3).scale(0.25)
        self.play(Create(table))
        table.add_highlighted_cell((3,1), color=RED)
        table.add_highlighted_cell((3,2), color=RED)
        table.add_highlighted_cell((3,3), color=RED)
        self.wait(0.25)
        
        highlighted_edges = VGroup()
        highlighted_edges.add(Line(graph['S'], graph['A'], color = ORANGE, ).add_tip(tip_length=0.1, tip_width=0.1))
        self.play(highlighted_edges[0].animate.set_color(ORANGE)) 
        
        self.play(FadeOut(table))
        self.wait(0.25)
        
        table = Table(
            [["Open", "Closed", "f(n) = g(n)+h(n)"],
             ["S", "    ", "0+10"],
             ["A, B", "S", "8, 15"],
             ['C, D, B', "S, A", "7, 11, 15"],
             ]
        ).shift(UP, RIGHT*3).scale(0.25)
        self.play(Create(table))
        table.add_highlighted_cell((4,1), color=RED)
        table.add_highlighted_cell((4,2), color=RED)
        table.add_highlighted_cell((4,3), color=RED)
        self.wait(0.25)
        
        highlighted_edges.add(Line(graph['A'], graph['C'], color = ORANGE, ).add_tip(tip_length=0.1, tip_width=0.1))
        self.play(highlighted_edges[1].animate.set_color(ORANGE)) 
        
        self.play(FadeOut(table))
        
        self.wait(0.25)
        
        table = Table(
            [["Open", "Closed", "f(n) = g(n)+h(n)"],
             ["S", "    ", "0+10"],
             ["A, B", "S", "8, 15"],
             ['C, D, B', "S, A", "7, 11, 15"],
             ['D, B', "S, A, C", "10, 15"],
             ]
        ).shift(UP, RIGHT*3).scale(0.25)
        self.play(Create(table))
        table.add_highlighted_cell((5,1), color=RED)
        table.add_highlighted_cell((5,2), color=RED)
        table.add_highlighted_cell((5,3), color=RED)
        self.wait(0.25)
        
        highlighted_edges.add(Line(graph['C'], graph['D'], color = ORANGE, ).add_tip(tip_length=0.1, tip_width=0.1))
        self.play(highlighted_edges[2].animate.set_color(ORANGE)) 
        
        self.play(FadeOut(table))
        
        self.wait(0.25)
        
        table = Table(
            [["Open", "Closed", "f(n) = g(n)+h(n)"],
             ["S", "    ", "0+10"],
             ["A, B", "S", "8, 15"],
             ['C, D, B', "S, A", "7, 11, 15"],
             ['D, B', "S, A, C", "10, 15"],
             ['G1, B', "S, A, C, D", "14, 15"],  
             ]
        ).shift(UP, RIGHT*3).scale(0.25)
        self.play(Create(table))
        table.add_highlighted_cell((6,1), color=RED)
        table.add_highlighted_cell((6,2), color=RED)
        table.add_highlighted_cell((6,3), color=RED)
        self.wait(0.25)
        
        
        highlighted_edges.add(Line(graph['D'], graph['G1'], color = ORANGE, ).add_tip(tip_length=0.1, tip_width=0.1))
        self.play(highlighted_edges[3].animate.set_color(ORANGE)) 
        
        self.wait(0.25)
        
        self.play(FadeOut(table))
        
        table = Table(
            [["Open", "Closed", "f(n) = g(n)+h(n)"],
             ["S", "    ", "0+10"],
             ["A, B", "S", "8, 15"],
             ['C, D, B', "S, A", "7, 11, 15"],
             ['D, B', "S, A, C", "10, 15"],
             ['B', "S, A, C, D, G1", "15"],  
             ]
        ).shift(UP, RIGHT*3).scale(0.25)
        self.play(Create(table))
        table.add_highlighted_cell((6,2), color=GREEN)
        
        self.wait(0.5)
        
        self.play(FadeOut(title, graph, heuristic_labels, node_labels, edge_labels, highlighted_edges, table))
        
        good_bye = Text("Thank you for watching.", font_size=24)    
        
        self.play(FadeIn(good_bye))
        self.wait(0.25)
        
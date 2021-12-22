import random as r 
from plotly.graph_objs._bar import Bar 
from plotly.graph_objs._layout import Layout 
from plotly import offline 

class Die:

    def __init__(self, sides=6):
        self.sides = sides 

    def roll(self):
        return r.randint(1, self.sides)

die = Die()

results = [die.roll() for _ in range(10_000)]
freqs = [results.count(i) for i in range(1, die.sides + 1)] 


xs = list(range(1, die.sides + 1))
data = [Bar(x=xs, y=freqs)]
x_axis_config = {'title': "Result"}
y_axis_config = {'title': "Frequency"}
my_layout = Layout(title="Results of rolling a D6 10,000 times", xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename="d6.html")
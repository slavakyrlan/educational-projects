colors = ['red', 'green', 'blue', 'yellow']
for i, color in enumerate(colors):
    print(i, '-->', color)

names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']
for name, color in zip(names, colors):
    print(name, '-->', color)
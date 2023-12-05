import matplotlib.pyplot as plot

def generate_bar_chart(labels, values):

    fig, ax = plot.subplots()
    ax.bar(labels, values)
    plot.show()

def generate_pie_chart(labels, values):
    fig, ax = plot.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plot.show()

if __name__ == '__main__':
    labels = ['a','b','c']
    values = [10,20,30]
    #generate_bar_chart(labels, values)
    generate_pie_chart(labels,values)
    
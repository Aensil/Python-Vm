import matplotlib.pyplot as plt

def pie_chart():
    labels = ['Nice', 'to', 'Graph']
    values = [150, 40, 250]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('Img.png')
    plt.close()
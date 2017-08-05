import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

mock = {
    'country': "Италия",
    'food': [7, 30, 100],
    'transport': [2, 11, 40],
    'entertainment': [13, 40, 154],
}

LEVELS = ['Минимум', 'В среднем', 'Максимум']
ORDER = [0, 1, 2]

food = pd.DataFrame(dict(x=mock['food'], y=LEVELS, order=ORDER)).sort_values(by="order")
transport = pd.DataFrame(dict(x=mock['transport'], y=LEVELS, order=ORDER)).sort_values(by="order")
entertainment = pd.DataFrame(dict(x=mock['entertainment'], y=LEVELS, order=ORDER)).sort_values(by="order")

def compute_percentages(data):
    averages = {
        'food': data['food'][1] / (data['transport'][1] + data['food'][1] + data['entertainment'][1]),
        'transport': data['transport'][1] / (data['transport'][1] + data['food'][1] + data['entertainment'][1]),
        'entertainment': data['entertainment'][1] / (data['transport'][1] + data['food'][1] + data['entertainment'][1]),
    }
    return averages

percentages = compute_percentages(mock)
sns.set_context(rc={'axes.facecolor':'ffffff', 'figure.facecolor':'ffffff', 'axes.grid': False, 'axes.labelcolor': 'black',
           'text.color': 'black'})
#plt.xkcd()
font = FontProperties(fname="Roboto-Regular.ttf")

figure = plt.figure(figsize=(10, 15))

with sns.color_palette("Reds", 3) as p:
    ax = plt.subplot(3, 2, 1, aspect='equal', adjustable='box-forced')
    pie_data = [percentages['food'], 1 - percentages['food']]
    plt.pie(pie_data, colors=[p[1], 'lightgray'], labels=["{:.0%}".format(pie_data[0]), ""])
    centre_circle = plt.Circle((0, 0), 0.75, color='black', fc='white', linewidth=0.5)
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax = plt.subplot(3, 2, 2)
    plt.title("Расходы на еду", fontproperties=font)
    sns.barplot(x="x", y="y", data=food)
    ax.set_xlabel('')
    ax.set_ylabel('')


with sns.color_palette("Blues", 3) as p:
    ax = plt.subplot(3, 2, 3, aspect='equal', adjustable='box-forced')
    pie_data = [percentages['transport'], 1 - percentages['transport']]
    plt.pie(pie_data, colors=[p[1], 'lightgray'], labels=["{:.0%}".format(pie_data[0]), ""])
    centre_circle = plt.Circle((0, 0), 0.75, color='black', fc='white', linewidth=0.5)
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax = plt.subplot(3, 2, 4)
    plt.title("Расходы на транспорт", fontproperties=font)
    sns.barplot(x="x", y="y", data=transport)
    ax.set_xlabel('')
    ax.set_ylabel('')


with sns.color_palette("Greens", 3) as p:
    ax = plt.subplot(3, 2, 5, aspect='equal', adjustable='box-forced')
    pie_data = percentages['entertainment'], 1 - percentages['entertainment']
    plt.pie(pie_data, colors=[p[1], 'lightgray'], labels=["{:.0%}".format(pie_data[0]), ""])
    centre_circle = plt.Circle((0, 0), 0.75 ,color='black', fc='white', linewidth=0.5)
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax = plt.subplot(3, 2, 6)
    plt.title("Расходы на развлечения", fontproperties=font)
    sns.barplot(x="x", y="y", data=entertainment)
    ax.set_xlabel('')
    ax.set_ylabel('')

sns.color_palette("Blues_d", 3)    

font.set_size(30)
figure.suptitle("Расходы в стране: {}".format("Италия"), color="black", fontproperties=font)


plt.savefig("Italy.png")

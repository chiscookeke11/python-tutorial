import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


label = ['Nigeria', 'China', 'Urugua', 'Brazil', 'Uganda']
population = [100000, 40000, 5060000, 7870000, 4546660000]



plt.bar(label, population.toLocaleString(), color='skyblue')
plt.title("Countries and their population")
plt.xlabel("Country")
plt.ylabel("Population")

plt.gca().yaxis.set_major_formatter(
    ticker.FuncFormatter(lambda x, pos: f"{int(x):,}")
)



plt.show()
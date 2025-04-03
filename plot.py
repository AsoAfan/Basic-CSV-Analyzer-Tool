import pandas as pd


def plot_graph(ax, data: pd.Series, column: str, color: str, graph_type: str):
    if graph_type == "Histogram":
        ax.hist(data, bins=20, alpha=0.7, color=color, edgecolor='black')
        ax.set_title(f"Histogram of {column}")

    elif graph_type == "Box Plot":
        ax.boxplot(data, patch_artist=True, boxprops=dict(facecolor=color))
        ax.set_title(f"Box Plot of {column}")

    elif graph_type == "Scatter Plot":
        ax.scatter(range(len(data)), data, color=color, alpha=0.6)
        ax.set_title(f"Scatter Plot of {column}")

    elif graph_type == "Line Chart":
        ax.plot(data, color=color, linewidth=2)
        ax.set_title(f"Line Chart of {column}")

    elif graph_type == "Bar Chart":
        ax.bar(range(len(data)), data, color=color)
        ax.set_title(f"Bar Chart of {column}")

    elif graph_type == "Pie Chart":
        top_10 = data.value_counts().nlargest(10)
        print(top_10[36])
        ax.pie(top_10, labels=top_10.index, colors=[color] * len(top_10), autopct="%1.1f%%")
        ax.set_title(f"Pie Chart of top 10 {column}s")

    ax.set_xlabel(column)
    ax.set_ylabel("Value")

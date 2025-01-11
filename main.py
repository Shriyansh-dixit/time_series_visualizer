# main.py
from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

if __name__ == "__main__":
    print("Generating Line Plot...")
    draw_line_plot()
    print("Line plot saved as 'line_plot.png'.")

    print("Generating Bar Plot...")
    draw_bar_plot()
    print("Bar plot saved as 'bar_plot.png'.")

    print("Generating Box Plot...")
    draw_box_plot()
    print("Box plot saved as 'box_plot.png'.")

    print("All plots generated and saved successfully.")

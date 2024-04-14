import numpy as np
import matplotlib.pyplot as plt

def load_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        version = filename.replace(".m", "").replace("output_", "") 
        data = []
        for line in lines:
            if '[' in line or ']' in line or 'version' in line:
                continue
            values = line.strip().split()
            data.append([int(values[0]), float(values[1]), float(values[2])])
        return version, np.array(data)

def plot_data(data, version, ax, color):
    x = data[:,0]
    y1 = data[:,1]
    y2 = data[:,2]

    ax.errorbar(x, y1, yerr=y2, label=f'{version}', fmt='-o', color = color)  

def plot_figures(plot_name = "all"):
    fig, ax = plt.subplots(figsize = (15,9))
    colors_linspace_1 = plt.cm.Set3(np.linspace(0, 1, 3))
    colors_linspace_2 = plt.cm.tab20(np.linspace(0, 1, 7))
    colors_linspace_3 = plt.cm.Dark2(np.linspace(0, 1, 13))

    colors = np.concatenate((colors_linspace_1, colors_linspace_2, colors_linspace_3))

    if plot_name == "all" or plot_name == "simple":
        for n in range(3):
            filename = f"output_MMult{n}.m"
            version, data = load_data(filename)
            plot_data(data, version, ax, colors[n])
    
    if plot_name == "all" or plot_name == "1x4":
        for n in range(3, 10):
            filename = f"output_MMult_1x4_{n}.m"
            version, data = load_data(filename)
            plot_data(data, version, ax, colors[n])

    if plot_name == "all" or plot_name == "4x4":
        for n in range(3, 16):
            filename = f"output_MMult_4x4_{n}.m"
            version, data = load_data(filename)
            plot_data(data, version, ax, colors[n+7])

    ax.set_title('Performance Comparison')
    ax.set_xlabel('m=n=k')
    ax.set_ylabel('GFLOPS/sec.')
    ax.legend()
    ax.grid(True)

    # plt.show()
    plt.savefig(f"_{plot_name}_comparison.png")


if __name__ == "__main__":
    plot_figures()
    plot_figures("simple")
    plot_figures("1x4")
    plot_figures("4x4")
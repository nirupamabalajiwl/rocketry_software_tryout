import matplotlib.pyplot as plt
import pandas as pd

def visualize_temp (filename="data/telemetry_sample.csv"):
    df = pd.read_csv(filename)
    fig, ax1 = plt.subplots(figsize = (10,6))
    
    ax1.set_xlabel("altitude")
    ax1.set_ylabel("temperature", color="tab:red")
    ax1.plot(df["altitude"],df['temperature'], color="tab:red")
    ax1.tick_params(axis="y", labelcolor="tab:blue")
    ax1.grid(True, linestyle="--", alpha=0.7)

    
    fig.suptitle("Altitude to Temperature understanding", fontsize=14)
    fig.tight_layout()
    fig.legend(loc="upper right")
    ax1.grid(True, linestyle="--", alpha=0.7)

    plt.show()

if __name__ == "__main__":
    visualize_temp()



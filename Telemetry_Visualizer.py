import matplotlib.pyplot as plt
import pandas as pd

def visualize_telemetry(file_path="data/telemetry_sample.csv"):
    df = pd.read_csv(file_path)
    fig, ax1 = plt.subplots(figsize=(10, 6))

    ax1.set_xlabel("time (s)")
    ax1.set_ylabel("altitude", color="tab:blue")
    ax1.plot(df["time"], df["altitude"], color="tab:blue", label="Altitude (m)")
    ax1.tick_params(axis="y", labelcolor="tab:blue")

    ax2 = ax1.twinx()  
    ax2.set_ylabel("velocity / acceleration", color="tab:red")
    ax2.plot(df["time"], df["velocity"], color="tab:orange", label="velocity (m/s)")
    ax2.plot(df["time"], df["acceleration"], color="tab:red", label="acceleration (m/s²)")
    ax2.tick_params(axis="y", labelcolor="tab:red")

    
    fig.suptitle("Rocket Telemetry Data", fontsize=14)
    fig.tight_layout()
    fig.legend(loc="upper right")
    ax1.grid(True, linestyle="--", alpha=0.7)

    plt.show()

if __name__ == "__main__":
    visualize_telemetry()
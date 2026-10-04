# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "matplotlib",
# ]
# ///

import json
from pathlib import Path
import matplotlib.pyplot as plt


def process_and_plot(data_path, output_path):
    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    hourly = data["hourly"]
    times = hourly["time"]
    temperatures = hourly["temperature_2m"]
    precipitations = hourly["precipitation"]

    formatted_times = []
    filtered_temps = []
    filtered_precip = []

    for t, temp, p in zip(times, temperatures, precipitations):
        # 转换时间格式，如 "2026-09-20T00:00" -> "09-20 00:00"
        formatted_times.append(t[5:].replace("T", " "))
        filtered_temps.append(temp)
        filtered_precip.append(p)

    fig, ax1 = plt.subplots(figsize=(12, 6))

    # 1. 绘制温度曲线
    color = "tab:red"
    ax1.set_xlabel("Time (MM-DD HH:00)")
    ax1.set_ylabel("Temperature (°C)", color=color)
    ax1.plot(formatted_times, filtered_temps, color=color, linewidth=2, label="Temperature (°C)")
    ax1.tick_params(axis="y", labelcolor=color)

    # X轴刻度：10天共240小时，每24小时（1天）标注一次刻度，防止重叠
    ax1.set_xticks(range(0, len(formatted_times), 24))
    ax1.set_xticklabels(formatted_times[::24], rotation=45)

    # 2. 绘制降水量柱状图
    ax2 = ax1.twinx()
    color = "tab:blue"
    ax2.set_ylabel("Precipitation (mm)", color=color)
    ax2.bar(formatted_times, filtered_precip, color=color, alpha=0.3, label="Precipitation (mm)")
    ax2.tick_params(axis="y", labelcolor=color)

    plt.title("Shenzhen Hourly Temperature and Precipitation (2026-09-20 to 2026-09-30)")
    fig.tight_layout()

    output_dir = Path(output_path).parent
    output_dir.mkdir(exist_ok=True)
    plt.savefig(output_path, dpi=300)
    print(f"Plot saved successfully to {output_path}")


if __name__ == "__main__":
    process_and_plot("data/shenzhen_weather.json", "out/weather.png")
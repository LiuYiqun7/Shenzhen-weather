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
    # 1. 从本地读取 JSON 数据
    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    hourly = data["hourly"]
    times = hourly["time"]
    temperatures = hourly["temperature_2m"]
    precipitations = hourly["precipitation"]

    # 2. 使用循环提取并整理数据（满足作业必需有 loop 的要求）
    formatted_times = []
    filtered_temps = []
    filtered_precip = []

    for t, temp, p in zip(times, temperatures, precipitations):
        # 截取时间字符串 (例如 "2026-09-17T14:00" -> "09-17 14:00")
        formatted_times.append(t[5:])
        filtered_temps.append(temp)
        filtered_precip.append(p)

    # 3. 绘制双轴折线与柱状图
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # 绘制气温折线
    color = "tab:red"
    ax1.set_xlabel("Time (MM-DD HH:00)")
    ax1.set_ylabel("Temperature (°C)", color=color)
    ax1.plot(formatted_times, filtered_temps, color=color, linewidth=2, label="Temperature (°C)")
    ax1.tick_params(axis="y", labelcolor=color)

    # X轴刻度稀疏化，防止挤在一起
    ax1.set_xticks(range(0, len(formatted_times), 12))
    ax1.set_xticklabels(formatted_times[::12], rotation=45)

    # 绘制降雨量柱状图
    ax2 = ax1.twinx()
    color = "tab:blue"
    ax2.set_ylabel("Precipitation (mm)", color=color)
    ax2.bar(formatted_times, filtered_precip, color=color, alpha=0.3, label="Precipitation (mm)")
    ax2.tick_params(axis="y", labelcolor=color)

    plt.title("Shenzhen Hourly Temperature and Precipitation Forecast")
    fig.tight_layout()

    # 4. 确保 out 目录存在并保存图片
    output_dir = Path(output_path).parent
    output_dir.mkdir(exist_ok=True)
    plt.savefig(output_path, dpi=300)
    print(f"Plot saved successfully to {output_path}")


if __name__ == "__main__":
    process_and_plot("data/shenzhen_weather.json", "out/weather.png")
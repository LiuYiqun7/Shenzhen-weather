# /// script
# requires-python = ">=3.10"
# dependencies = ["requests"]
# ///

from pathlib import Path
import requests

# 深圳的经纬度：北纬22.5431, 东经114.0579
API_URL = "https://api.open-meteo.com/v1/forecast?latitude=22.5431&longitude=114.0579&hourly=temperature_2m,precipitation&timezone=Asia%2FShanghai"


def fetch_weather_data():
    # 确保 data 目录存在
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)

    file_path = data_dir / "shenzhen_weather.json"

    print("Fetching weather data for Shenzhen...")
    response = requests.get(API_URL)
    response.raise_for_status()

    # 将原始数据保存到 data/ 文件夹
    file_path.write_text(response.text, encoding="utf-8")
    print(f"Data saved successfully to {file_path}")


if __name__ == "__main__":
    fetch_weather_data()
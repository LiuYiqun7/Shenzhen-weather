# /// script
# requires-python = ">=3.10"
# dependencies = ["requests"]
# ///

from pathlib import Path
import requests

# 深圳经纬度：北纬22.5431, 东经114.0579
# 指定 start_date=2026-09-20 与 end_date=2026-09-30
API_URL = "https://archive-api.open-meteo.com/v1/archive?latitude=22.5431&longitude=114.0579&start_date=2026-09-20&end_date=2026-09-30&hourly=temperature_2m,precipitation&timezone=Asia%2FShanghai"


def fetch_weather_data():
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)

    file_path = data_dir / "shenzhen_weather.json"

    print("Fetching weather data for Shenzhen (2026-09-20 to 2026-09-30)...")
    response = requests.get(API_URL)
    response.raise_for_status()

    file_path.write_text(response.text, encoding="utf-8")
    print(f"Data saved successfully to {file_path}")


if __name__ == "__main__":
    fetch_weather_data()
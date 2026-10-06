import requests
import pandas as pd

latitude = 10.870051
longitude = 106.803331
start_date = "2021-01-01"
end_date = "2025-12-31"

url = "https://archive-api.open-meteo.com/v1/archive"

hourly_fields = [
    "temperature_2m",
    "relative_humidity_2m",
    "dew_point_2m",
    "apparent_temperature",
    "precipitation",
    "rain",
    "weather_code",
    "surface_pressure",
    "wind_speed_10m",
    "wind_direction_10m",
    "wind_gusts_10m",
    "cloud_cover"
]

params = {
    "latitude": latitude,
    "longitude": longitude,
    "start_date": start_date,
    "end_date": end_date,
    "hourly": ",".join(hourly_fields),
    "timezone": "auto"
}

print("Dang thu thap du lieu tu Open-Meteo...")

response = requests.get(
    url,
    params=params,
    timeout=60
)

response.raise_for_status()

data = response.json()
print("Latitude:", data.get("latitude"))
print("Longitude:", data.get("longitude"))
print("Elevation:", data.get("elevation"))
print("Timezone:", data.get("timezone"))
print("Timezone abbreviation:", data.get("timezone_abbreviation"))
print("UTC offset seconds:", data.get("utc_offset_seconds"))

if "hourly" not in data:
    print("Khong tim thay du lieu hourly.")
    print(data)
    exit()

df = pd.DataFrame(data["hourly"])

df["time"] = pd.to_datetime(df["time"])

df = df.sort_values(by="time")
df = df.reset_index(drop=True)

print("So dong:", len(df))
print("So cot:", len(df.columns))

print("Khoang thoi gian:")
print(df["time"].min(), "->", df["time"].max())

print("Cac cot:")
print(df.columns.tolist())

print("5 dong dau:")
print(df.head())

print("Gia tri thieu:")
print(df.isnull().sum())

print("Dong bi trung lap:")
print(df.duplicated().sum())

print("Thong ke mo ta:")
print(df.describe())

output_file = "uit_weather_2021_2025.csv"

df.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)

print("Da luu file:", output_file)
import polars as pl

# -------------------------
# Úloha 1 – Načtení datasetu
# -------------------------

df = pl.read_csv("physics_solar_panel_lab_dataset.csv")

print("Prvních 5 řádků:")
print(df.head())

print("\nShape datasetu:")
print(df.shape)

print("\nSchema (datové typy):")
print(df.schema)


# -------------------------
# Úloha 2 – Čištění dat
# -------------------------

df = df.with_columns([
    pl.col("voltage_v").cast(pl.Float64),
    pl.col("current_a").cast(pl.Float64),
    pl.col("power_w").cast(pl.Float64),
    pl.col("light_intensity_lux").cast(pl.Float64),
    pl.col("angle_deg").cast(pl.Float64),
])

# převod timestamp
df = df.with_columns(
    pl.col("timestamp").str.strptime(pl.Datetime, strict=False)
)

# odstranění nesmyslných hodnot
df = df.filter(
    (pl.col("voltage_v") >= 0) &
    (pl.col("current_a") >= 0) &
    (pl.col("power_w") >= 0) &
    (pl.col("angle_deg") <= 90)
)

# odstranění null hodnot
df = df.drop_nulls()

# odstranění duplicit
df = df.unique()

# sjednocení textu
df = df.with_columns([
    pl.col("weather")
    .str.strip_chars()
    .str.to_lowercase()
    .replace({"suny": "sunny"}),

    pl.col("room")
    .str.strip_chars()
    .str.to_lowercase()
])


# -------------------------
# Úloha 3 – výpočet výkonu
# -------------------------

df = df.with_columns(
    (pl.col("voltage_v") * pl.col("current_a")).alias("power_calc")
)

print("\nPorovnání výkonu:")
print(df.select(["power_w", "power_calc"]).head())


# -------------------------
# Úloha 4 – vliv úhlu
# -------------------------

angle_power = df.group_by("angle_deg").agg(
    pl.col("power_w").mean()
)

print("\nPrůměrný výkon podle úhlu:")
print(angle_power)


# -------------------------
# Úloha 5 – vliv světla
# -------------------------

corr = df.select(
    pl.corr("light_intensity_lux", "power_w")
)

print("\nKorelace lux vs výkon:")
print(corr)


# -------------------------
# Úloha 6 – porovnání prostředí
# -------------------------

env = df.group_by("weather").agg(
    pl.col("power_w").mean()
)

print("\nPrůměrný výkon podle počasí:")
print(env)


# -------------------------
# Úloha 7 – nejlepší podmínky
# -------------------------

best = df.sort("power_w", descending=True).head(5)

print("\nNejlepší podmínky:")
print(best)


# -------------------------
# Úloha 8 – anomálie
# -------------------------

anomalies = df.filter(
    pl.col("power_w") > df["power_w"].mean() + 3 * df["power_w"].std()
)

print("\nPodezřelé hodnoty:")
print(anomalies)


# -------------------------
# Úloha 9 – vlastní analýza
# -------------------------

panel_perf = df.group_by("panel_id").agg(
    pl.col("power_w").mean()
)

print("\nPrůměrný výkon panelů:")
print(panel_perf)
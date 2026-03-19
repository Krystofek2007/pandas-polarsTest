import pandas as pd

# -------------------------
# Úloha 1 – Načtení datasetu
# -------------------------

df = pd.read_csv("physics_solar_panel_lab_dataset.csv")

print("Prvních 5 řádků:")
print(df.head())

print("\nInformace o datasetu:")
print(df.info())

print("\nPočet řádků:", df.shape[0])
print("Počet sloupců:", df.shape[1])


# -------------------------
# Úloha 2 – Čištění dat
# -------------------------

# převod na čísla
numeric_cols = [
    "voltage_v",
    "current_a",
    "power_w",
    "light_intensity_lux",
    "angle_deg"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# převod timestampu
df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

# odstranění nesmyslných hodnot
df = df[df["voltage_v"] >= 0]
df = df[df["current_a"] >= 0]
df = df[df["power_w"] >= 0]
df = df[df["angle_deg"] <= 90]

# odstranění chybějících hodnot
df = df.dropna()

# odstranění duplicit
df = df.drop_duplicates()

# sjednocení textů
df["weather"] = df["weather"].str.strip().str.lower()
df["room"] = df["room"].str.strip().str.lower()

# oprava překlepů
df["weather"] = df["weather"].replace({
    "suny": "sunny"
})


# -------------------------
# Úloha 3 – Výpočet výkonu
# -------------------------

df["power_calc"] = df["voltage_v"] * df["current_a"]

print("\nPorovnání výkonu:")
print(df[["power_w", "power_calc"]].head())


# -------------------------
# Úloha 4 – Vliv úhlu
# -------------------------

angle_power = df.groupby("angle_deg")["power_w"].mean()

print("\nPrůměrný výkon podle úhlu:")
print(angle_power)


# -------------------------
# Úloha 5 – Vliv světla
# -------------------------

correlation = df["light_intensity_lux"].corr(df["power_w"])

print("\nKorelace lux vs výkon:", correlation)


# -------------------------
# Úloha 6 – Porovnání prostředí
# -------------------------

environment_power = df.groupby("weather")["power_w"].mean()

print("\nPrůměrný výkon podle počasí:")
print(environment_power)


# -------------------------
# Úloha 7 – Nejlepší podmínky
# -------------------------

best = df.loc[df["power_w"].idxmax()]

print("\nNejvyšší výkon:")
print(best)


# -------------------------
# Úloha 8 – Anomálie
# -------------------------

anomalies = df[
    (df["power_w"] > df["power_w"].mean() + 3 * df["power_w"].std())
]

print("\nPodezřelé hodnoty:")
print(anomalies)


# -------------------------
# Úloha 9 – Vlastní analýza
# -------------------------

panel_efficiency = df.groupby("panel_id")["power_w"].mean()

print("\nPrůměrný výkon panelů:")
print(panel_efficiency)
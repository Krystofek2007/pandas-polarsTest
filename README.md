Analýza výkonu solárního panelu

Obsah repozitáře
├── main.py                              # hlavní skript (pandas nebo Polars)
├── physics_solar_panel_lab_dataset.csv  # dataset
└── README.md                            # tento soubor
Postup čištění dat (Úloha 2)
Jaké chyby jsem našel?
Typ chyby	Sloupec	Počet výskytů	Řešení
Špatný datový typ	lamp_distance_cm, temperature_c, voltage_v, current_a	vícero	převod na float
Záporná vzdálenost lampy	lamp_distance_cm	2	odstranění řádku
Úhel > 90°	angle_deg	2	odstranění řádku
Záporný výkon	power_w	3	odstranění řádku
Nereálné napětí (>10 V)	voltage_v	1	odstranění řádku
Nereálná teplota (>80 °C)	temperature_c	1	odstranění řádku
Chybějící klíčové hodnoty	více sloupců	~8	odstranění řádku
Chybějící room / weather	textové sloupce	~9	doplnění „unknown"
Chybějící temperature_c	číslo	~2	doplnění mediánem
Duplicitní řádky	celý řádek	7	odstranění
Překlepy ve weather	„suny", „sunny ", „ cloudy", „indoor lamp"	vícero	nahrazení správnou hodnotou
Překlepy v room	„Roof ", „lab-1"	vícero	nahrazení správnou hodnotou
Odpovědi na fyzikální otázky
Úloha 1 – Problematické sloupce
lamp_distance_cm, temperature_c, voltage_v, current_a – načteny jako text místo čísel. timestamp jako řetězec. weather a room obsahují překlepy.

Úloha 3 – power_calc vs power_w
Hodnoty se mírně liší. Důvod: power_w byl v datasetu zaokrouhlen při záznamu a může obsahovat malé měřicí nepřesnosti. power_calc = voltage_v × current_a je přesnější výpočet ze změřených hodnot.

Úloha 4 – Vliv úhlu
Výkon roste s úhlem do přibližně 30–45°, pak klesá.
Fyzikální smysl: Výkon závisí na ploše průřezu paprsku dopadajícího na panel. Platí
P ∝ cos(θ), kde θ je úhel od kolmice. Při 0° (kolmo) dopadá nejvíce světla, ale v experimentu
mohl být 0° jinak definován (úhel od roviny), proto maximum není nutně na 0°.

Úloha 5 – Vliv intenzity světla
Korelace light_intensity_lux vs power_w je silná (r ≈ 0.7–0.9).
Závislost není čistě lineární – při vysokých hodnotách lux se panel přibližuje napěťovému maximu (Voc) a výkon přestává lineárně růst.

Úloha 6 – Porovnání prostředí
Venku (sunny) >> V laboratoři (indoor-lamp).
Slunce poskytuje ~80 000–100 000 lux, laboratorní lampy jen ~1 000–5 000 lux.
Vyšší intenzita světla = více elektronů excitovaných v PN přechodu = vyšší proud = vyšší výkon.

Úloha 7 – Nejlepší podmínky
Panel SP-101 nebo SP-102, venku (sunny), úhel ~30–45° → nejvyšší naměřený výkon.
Optimalizace: mít panel na střeše, nakloněný k optimálnímu úhlu, čistý povrch, ideálně kolem poledne.

Úloha 8 – Anomálie
Extrémní lux (~100 000+): Reálné pro přímé sluneční záření – není chyba.
Extrémní výkon: Odpovídá kombinaci high-lux + optimální úhel + venkovní podmínky – není chyba, jde o fyzikálně správné výsledky.
Úloha 9 – Vlastní analýza: Vliv teploty
Korelace teploty a výkonu je mírně záporná.
Fyzikální smysl: Křemíkové fotovoltaické články ztrácejí účinnost přibližně 0,4 % na každý stupeň Celsia nad standardní testovací teplotou (25 °C). Efekt je v datasetu maskován tím, že venkovní měření mají zároveň vyšší intenzitu světla – oba faktory se překrývají.

Použité nástroje
Python 3
pandas nebo Polars (dle verze main.py)
Dataset: physics_solar_panel_lab_dataset.csv
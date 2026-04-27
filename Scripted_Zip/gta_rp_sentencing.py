#gta_rp_sentencing.py


# GTA RP Sentencing Converter: Real ↔ GTA Days (All Reductions Listed)
# 1 real year = 1 GTA day; shows base + all cuts on real→GTA

def real_to_gta_all(years=0, months=0, days=0):
    total_real_days = years * 365 + months * 30 + days
    base_gta = total_real_days / 365.0
    
    base_real_min = base_gta * 48
    base_h = int(base_real_min // 60)
    base_m = int(base_real_min % 60)
    
    print(f"\nReal sentence: {years}y {months}m {days}d")
    print(f"Base GTA: {base_gta:.2f} days → {base_h}h {base_m}m (no reduction)")
    print("--- Reductions ---")
    
    for name, pct in [("Good behavior", 0.8), ("Trustee", 0.6), ("Parole", 0.5)]:
        gta_cut = base_gta * pct
        real_min_cut = gta_cut * 48
        h_cut = int(real_min_cut // 60)
        m_cut = int(real_min_cut % 60)
        print(f"{name} ({int((1-pct)*100)}% off): {gta_cut:.2f} GTA days → {h_cut}h {m_cut}m")
    
    if base_h < 4:
        print("\nLight—reductions turn it into a coffee run.")
    else:
        print("\nHeavy, but good time keeps it sane.")

def gta_to_real(days=0, hours=0, minutes=0):
    total_gta_min = days * 1440 + hours * 60 + minutes
    real_min = total_gta_min * (48 / 1440)  # 48 min per GTA day
    
    real_h = int(real_min // 60)
    real_m = int(real_min % 60)
    
    print(f"\nGTA time: {days}d {hours}h {minutes}m")
    print(f"→ Real served: {real_h}h {real_m}m")
    print("Straight clock—no cuts here.")

print("=== GTA RP Sentencing CONVERTER ===\n")
print("r = real→gta (with all reductions), g = gta→real, q = quit\n")

while True:
    mode = input("Mode: ").lower().strip()
    if mode == 'q':
        print("Session closed—don't get caught.")
        break
    
    try:
        if mode == 'r':
            y = int(input("Years: ") or 0)
            m = int(input("Months: ") or 0)
            d = int(input("Days: ") or 0)
            real_to_gta_all(y, m, d)
        
        elif mode == 'g':
            d = int(input("GTA days: ") or 0)
            h = int(input("GTA hours: ") or 0)
            mi = int(input("GTA minutes: ") or 0)
            gta_to_real(d, h, mi)
        
        else:
            print("Use 'r', 'g', or 'q'.")
    
    except ValueError:
        print("Numbers only—retry.")


#Tests: 1 year → 1 GTA day → 48 min real (“Quick coffee break.”).
# 6 months → 0.5 GTA days → 24 min real (“Shorter than a loading screen.”).
#Here’s a quick list of common criminal offenses, ranging from misdemeanors to serious felonies. 
#Petty Theft / ShopliftingReal sentence: 30 daysGTA: ~0.08 daysReal served: ~4 minutes“You’re out before the clerk finishes the receipt.”
#Public Intoxication / Disorderly ConductReal: 3 monthsGTA: ~0.25 daysReal served: ~12 minutes“A nap in the drunk tank—back to the bar.”
#Simple Assault (no weapon, no injury)Real: 6 monthsGTA: ~0.5 daysReal served: ~24 minutes“Punch-out? More like a timeout.”
#Vandalism / GraffitiReal: 1 yearGTA: 1 dayReal served: 48 minutes“Tag a wall, sit an hour—art school dropout.”
#Mid-Level Felonies (serious but not life-ruining)
#Grand Theft Auto (carjacking)Real: 2–3 yearsGTA: 2–3 daysReal served: 1h 36m – 2h 24m“Steal a Banshee? That’s a lunch break in Bolingbroke.”
#Armed Robbery (no shots fired)Real: 5 yearsGTA: 5 daysReal served: 4 hours“Bank job? You’re home for dinner.”
#Drug Possession (large amount)Real: 7 yearsGTA: 7 daysReal served: 5h 36m“Brick of coke? Solid day—watch the sunset from the yard.”
#Heavy Felonies (murder, rape, etc.—big IC, still playable)
#Murder / ManslaughterReal: 20 yearsGTA: 20 daysReal served: 16 hours“Body in the trunk? That’s a full shift—pack snacks.”
#First-Degree MurderReal: 25–40 yearsGTA: 25–40 daysReal served: 20–32 hours“Premeditated? You’re basically a weekend warrior now.”
#Life Sentence (no parole)Real: 50+ years (or “life”)GTA: 50+ daysReal served: 40+ hours (~2 days straight)“Life? Nah—just a long Netflix binge with bad lighting.”
#This scale keeps sentences sounding brutal in RP (“You’re doing 20 days hard time!”), but you’re never stuck longer than a movie marathon.

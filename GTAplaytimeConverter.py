# GTA RP Playtime Converter: Real → Full GTA Breakdown
# 1 real min = 30 GTA min → years/months/days/etc.

def real_to_gta_full(hours=0, minutes=0, seconds=0):
    total_real_sec = hours * 3600 + minutes * 60 + seconds
    gta_sec = total_real_sec * 30
    
    gta_years = gta_sec // (365 * 86400)
    remaining = gta_sec % (365 * 86400)
    
    gta_months = remaining // (30 * 86400)  # rough 30-day month
    remaining = remaining % (30 * 86400)
    
    gta_days = remaining // 86400
    remaining = remaining % 86400
    
    gta_hours = remaining // 3600
    remaining = remaining % 3600
    
    gta_min = remaining // 60
    gta_sec_left = remaining % 60
    
    print(f"\nReal playtime: {hours}h {minutes}m {seconds}s")
    print(f"→ GTA time passed: {gta_years} years, {gta_months} months, "
          f"{gta_days} days, {gta_hours}h {gta_min}m {gta_sec_left}s")
    
    # Satire kick
    if gta_years > 0:
        print("You've aged into a legend. Or just need a life.")
    elif gta_days > 30:
        print("Month-plus? Your character's got more stories than you do.")
    else:
        print("Short grind—barely enough for one car chase.")

print("=== GTA RP LIFETIME CONVERTER ===\n")
print("Real grind → GTA years/months/days. Because time's weird here.\n")

while True:
    try:
        print("Your real session:")
        h = int(input("Hours: ") or 0)
        m = int(input("Minutes: ") or 0)
        s = int(input("Seconds: ") or 0)
        
        real_to_gta_full(h, m, s)
        
        again = input("\nMore playtime? (y/n): ").lower()
        if again != 'y':
            print("Session over—your alt's probably in therapy.")
            break
    
    except ValueError:
        print("Just numbers—don't overthink it.")
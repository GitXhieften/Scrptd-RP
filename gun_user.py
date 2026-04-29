# firearm_use.py

def firearm_use():
    questions = [
        (   
            " What Is Your Relationship with Guns?",
            {
                'A': ("I’m a collector, always looking to expand my firearm collection and expertise in various types of guns.", ["Gun Enthusiast"], ["Public Servant", "Luxury Lifestyle", "Loose Screw", "Mastermind"]),
                'B': ("Mainly using guns to defend myself, and my personal possesions. I keep it for protection", ["Casual User"], ["Crashout", "Go-Getter", "Hustler", "Chamleon"]),
                'C': ("Guns are apart of my livihood, but it’s not really a big thing.", ["Practical User"], ["Hustler", "Public Servant", "Tycoon", "Go-Getter"]),
                'D': ("I don’t mess with guns, I’m not into that type of thing. I prefer non-violent conflict resolution.", ["Peacekeeper"], ["innocent Civ", "Luxury Lifestyle", "Public Servant"]),
            } 
        ),
        ( 
            " How comfortable are you with the idea of having a gun as part of your daily carry?",
            {
                'A': ("It’s an essential part of my lifestyle.", ["Casual User"], ["Crashout", "Loose Screw", "Mastermind", "Chameleon"]),
                'B': ("I carry for safety.", ["Practical User"], ["Public Servant", "Hustler", "Chameleon"]),
                'C': ("I’d rather keep my distance from guns.", ["Peacekeeper"], ["innocent Civ", "Luxury Lifestyle",]),
                'D': ("I don’t need a gun all the time.", ["Peacekeeper"], ["Innocent Civ", "Luxury Lifestyle", "Public Servant", "Tycoon"]),
            }
        ),
        (
            " How do you feel about seeing a firearm in someone’s possession?",
            {
                'A': ("It’s expected, I’d want one around for my own protection.", ["Gun Enthusiast"], ["Crashout", "Loose Screw", "Mastermind", "Go-Getter"]),
                'B': ("I don’t mind if it’s properly secured, but I wouldn’t feel safe if it's being brandished.", ["Practical User"], ["Public Servant", "Hustler", "Chameleon"]),
                'C': ("I get a little uncomfortable, guns are dangerous.", ["Peacekeeper"], ["Innocent Civ", "Luxury Lifestyle"]),
                'D': ("I don’t care, but I won’t touch it unless it’s necessary.", ["Casual User"], ["Chameleon","Tycoon", "Freelancer", "Mastermind"]),
            }
        ),
        (
            " What do you think about gun violence?",
            {
                'A': ("It’s a necessary evil in the streets.", ["Gun Enthusiast"], ["Crashout", "Freelancer", "Loose Screw,"]),
                'B': ("I’d rather avoid the violence.", ["Peacekeeper"], ["Public Servant", "Freelancer", "Luxury Lifestyle", "Innocent Civ", "Hustler"]),
                'C': ("It’s the last resort.", ["Practical User"], ["Public Servant", "Go-Getter", "Tycoon", "Mastermind"]),
                'D': ("I don’t like it, but I’ll deal with it.", ["Casual User"], ["Chameleon", "Public Servant", "Freelancer", "Luxury Lifestyle"]),
            }
        ),
        (
            " What’s your opinion on people who carry guns for protection?",
            {
                'A': ("It’s a must.", ["Gun Enthusiast"], ["Crashout", "Loose Screw", "Mastermind", "Chameleon"]),
                'B': ("It’s okay if necessary.", ["Practical User"], ["Public Servant", "Go-Getter", "Hustler", "Mastermind"]),
                'C': ("It escalates situations.", ["Peacekeeper"], ["Public Servant", "Innocent Civ"]),
                'D': ("It’s their business.", ["Casual User"], ["Chameleon", "Tycoon", "Luxury Lifestyle"]),
            }
        )
    ]

    gun_archetype_tally = {
        "Gun Enthusiast": 0,
        "Practical User": 0,
        "Peacekeeper": 0,
        "Casual User": 0
    }

    personality_archetype_tally = {
        "Mastermind": 0,
        "Loose Screw": 0,
        "Crashout": 0,
        "Chameleon": 0,
        "Go-Getter": 0,
        "Tycoon": 0,
        "Luxury Lifestyle": 0,
        "Public Servant": 0,
        "Innocent Civ": 0,
        "Hustler": 0,
        "Freelancer": 0
    }
    print("\n🔫 GUN USE ASSESSMENT (GTA STYLE)\n")

    for i, (question, options) in enumerate(questions, 1):
        print(question)
        for key, (text, _, _) in options.items():
            print(f"  {key}: {text}")

        choice = input("Your choice (A/B/C/D): ").strip().upper()
        while choice not in options:
            print("Invalid choice. Try again.")
            choice = input("Your choice (A/B/C/D): ").strip().upper()

        gun_types, archetypes = options[choice][1], options[choice][2]

        for gtype in gun_types:
            gun_archetype_tally[gtype] += 1
        for ptype in archetypes:
            if ptype in personality_archetype_tally:
                personality_archetype_tally[ptype] += 1

    # Determine dominant gun use profile
    max_gun_score = max(gun_archetype_tally.values())
    top_gun_profiles = [g for g, score in gun_archetype_tally.items() if score == max_gun_score]
    dominant_gun_profile = top_gun_profiles[0] if len(top_gun_profiles) == 1 else "DGAF"

    # Display Results
    print("\n🔍 Gun Use Archetype Tally:")
    for arch, score in gun_archetype_tally.items():
        print(f"  {arch}: {score}")

    print("\n🧠 Personality Archetype Tally (From Gun Use):")
    for arch, score in personality_archetype_tally.items():
        print(f"  {arch}: {score}")

    print(f"\n🔫 Final Gun Profile: {dominant_gun_profile}")

    return dominant_gun_profile, gun_archetype_tally, personality_archetype_tally

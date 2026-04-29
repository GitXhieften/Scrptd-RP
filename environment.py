# environment.py
def living_environment():
    questions = [
        (
            " If you had the choice to live anywhere in San Andreas, where would it be?",
            {
                'A': ("Out in the middle of nowhere, far from the city’s noise and chaos.", ["Rural"], ["Loose Screw", "Chameleon", "Innocent Civ", "Mastermind"]),
                'B': ("In the thick of things, surrounded by action, gangs, and a vibrant community.", ["Inner City"], ["Crashout", "Chameleon", "Loose Screw", "Go-Getter", "Public Servant", "Mastermind"]),
                'C': ("In a quiet, upscale neighborhood with privacy and stability.", ["Suburb"], ["Tycoon", "Luxury Lifestyle", "Mastermind", "Innocent Civ"]),
                'D': ("As long as it has internet and I don’t hear screaming at 3AM, I’ll survive.", ["Indifferent"], ["Innocent Civ", "Chameleon", "Go-Getter", "Hustler", "Public Servant"]),
            }
        ),
        (
            " How do you feel about city life?",
            {
                'A': ("I can’t stand the chaos; I’d rather keep to myself and away from the crowd.", ["Rural", "Suburb"], ["Luxury Lifestyle", "Tycoon", "Mastermind", "Chameleon"]),
                'B': ("It’s exciting, fast-paced, and full of opportunity. I thrive on the energy.", ["Inner City"], ["Crashout", "Go-Getter", "Public Servant"]),
                'C': ("It’s nice for a visit, but I prefer somewhere calmer and less stressful.", ["Suburb", "Rural"], ["Tycoon", "Luxury Lifestyle"]),
                'D': ("City, country, space station, I adapt.", ["Indifferent"], ["Chameleon", "Innocent Civ", "Mastermind", "Go-Getter"]),
            }
        ),
        (
            " What’s your ideal lifestyle?",
            {
                'A': ("Being in a place where I’m free to do what I want with minimal interference.", ["Rural"], ["Loose Screw", "Go-Getter", "Hustler", "Tycoon"]),
                'B': ("Living in the heart of the city, where there’s always something to do and people to meet.", ["Inner City"], ["Crashout", "Luxury Lifestyle", "Go-Getter", "Chameleon", "Public Servant", "Innocent Civ"]),
                'C': ("A clean, organized life with nice things and a peaceful home.", ["Suburb"], ["Tycoon", "Luxury Lifestyle", "Mastermind", "Innocent Civ"]),
                'D': ("I just need four walls, a roof, and a hood store.", ["Indifferent"], ["Chameleon", "Crashout", "Innocent Civ", "Loose Screw", "Freelancer"]),
            }
        ),
        (
            " You hear gunshots outside your house. What’s your response?",
            {
                'A': ("“Probably someone chasing off a wild coyote again.”", ["Rural"], ["Loose Screw", "Freelancer", "Innocent Civ"]),
                'B': ("“That better be fireworks... I'm calling the neighborhood watch.”", ["Suburb"], ["Luxury Lifestyle", "Public Servant", "Innocent Civ"]),
                'C': ("“Ayo, was that down the street or up the block?”", ["Inner City"], ["Crashout", "Go-Getter", "Loose Screw"]),
                'D': ("“Doesn’t matter, I sleep thru gun shots anyway.”", ["Indifferent"], ["Chameleon", "Crashout", "Innocent Civ"]),
            }
        )
    ]

    # Initialize tallies
    environment_tally = {env: 0 for env in ["Rural", "Inner City", "Suburb", "Indifferent"]}
    archetype_tally = {
        "Mastermind": 0,
        "Loose Screw": 0,
        "Crashout": 0,
        "Chameleon": 0,
        "Go-Getter": 0,
        "Tycoon": 0,
        "Luxury Lifestyle": 0,
        "Public Servant": 0,
        "Innocent Civ": 0,
        "Hustler": 0
    }

    print("\n🏙️ LIVING ENVIRONMENT ASSESSMENT (GTA STYLE)\n")

    for i, (question, options) in enumerate(questions, 1):
        print(f"{question}")
        for key, (text, _, _) in options.items():
            print(f"  {key}: {text}")

        choice = input("Your choice (A/B/C/D): ").strip().upper()
        while choice not in options:
            print("Invalid choice. Try again.")
            choice = input("Your choice (A/B/C/D): ").strip().upper()

        selected_envs, selected_archetypes = options[choice][1], options[choice][2]

        for env in selected_envs:
            environment_tally[env] += 1

        for arch in selected_archetypes:
            archetype_tally[arch] = archetype_tally.get(arch, 0) + 1

    # Determine most preferred environment
    max_score = max(environment_tally.values())
    top_environments = [env for env, score in environment_tally.items() if score == max_score]
    preferred = top_environments[0] if len(top_environments) == 1 else "DGAF"

    # Output results
    print("\n🌆 Living Environment Preference Tally:")
    for env, score in environment_tally.items():
        print(f"  {env}: {score}")

    print(f"\n🌆 Final Preferred Living Environment: {preferred}")

    print("\n🧠 Archetype Tally from Environment Questions:")
    for arch, score in archetype_tally.items():
        print(f"  {arch}: {score}")

    return preferred, environment_tally, archetype_tally

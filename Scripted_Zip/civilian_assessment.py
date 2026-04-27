# civilian_assessment.py
# Define the questions, responses, and associated archetypes 
civilian_questions = [
    (
        "You’ve been invited to a party with troublemakers. What’s your move?",
        {
            'A': {
                "response": "Politely decline the invitation and find another crowd to hang with.",
                "type": "S",
                "archetypes": ["Public Servant", "Innocent Civ"]
            },
            'B': {
                "response": "Go, but make sure you stay out of trouble.",
                "type": "S",
                "archetypes": ["Innocent Civ", "Chameleon", "Luxury Lifestyle"]
            },
            'C': {
                "response": "Check it out and see if you can have some fun without going too far.",
                "type": "S",
                "archetypes": ["Freelancer", "Public Servant"]
            },
            'D': {
                "response": "Show up, take what you can, and stir things up.",
                "type": "C",
                "archetypes": ["Tycoon", "Hustler"]
            }
        }
    ),
    (
        "How do you view the concept of money?",
        {
            'A': {"response": "Money is important, but it’s not everything.", "type": "S", "archetypes": ["Public Servant", "Innocent Civ", "Chameleon"]},
            'B': {"response": "Money is very important, and I’ll do whatever it takes to earn it legally.", "type": "S", "archetypes": ["Hustler", "Freelancer","Luxury Lifestyle", "Hustler"]},
            'C': {"response": "Money is essential for freedom, I’ll always find ways to make more.", "type": "C", "archetypes": ["Freelancer", "Tycoon", "Luxury Lifestyle"]},
            'D': {"response": "I prefer to live with minimal expenses, and I don’t mind living paycheck to paycheck.", "type": "S", "archetypes": ["Innocent Civ", "Public Servant"]}
        }
    ),
    (
    "You’re with a friend who’s doing something illegal, but they offer you a cut of the profits. What do you do?",
    {
        'A': {
            "response": "Refuse, I’m not getting involved in that.",
            "type": "S",  # Law-abiding
            "archetypes": ["Public Servant", "Innocent Civ"]
        },
        'B': {
            "response": "Keep your distance but take the cut if it’s offered.",
            "type": "S",  # Still leans straight but morally flexible
            "archetypes": ["Freelancer", "Chameleon", "Innocent Civ", "Luxury Lifestyle"]
        },
        'C': {
            "response": "Help out, but only if it’s a one-time thing.",
            "type": "C",  # Criminal-curious
            "archetypes": ["Hustler", "Public Servant", "Freelancer"]
        },
        'D': {
            "response": "Jump in, you’ll make a lot more in the long run.",
            "type": "C",  # Full criminal
            "archetypes": ["Hustler", "Tycoon", "Luxury Lifestyle"]
        }
    }
),
    (
    "You’re offered a chance to make big money doing risky business. What do you say?",
    {
            'A': {"response": "Let’s do it! big risks, big rewards. I’m in.", "type": "C", "archetypes": [ "Tycoon", "Luxury Lifestyle", "Hustler"]},
            'B': {"response": "if it sounds like a good deal, I’ll make sure I’m getting the right cut without the heat.", "type": "C", "archetypes": ["Hustler", "Chameleon", "Luxury Lifestyle" "Freelancer" ]},
            'C': {"response": "I know the game. they'll use the blackmail angle and/or threaten me to do the job. ", "type": "S", "archetypes": ["Tycoon", "Innocent Civ"]},
            'D': {"response": "I’m too smart for this. I’ll keep my distance and just make a quick profit from the sidelines.", "type": "S", "archetypes": ["Innocent Civ", "Tycoon", "Public Servant"]}

        }
),
    (
        "You’re given a stack of cash but no real way to explain where it came from. What do you do?",
    {
            'A': {"response": "Buy a new car and lay low, but I’ll keep a close eye on anyone who starts asking questions.", "type": "C", "archetypes": ["Loose Screw", "Luxury Lifestyle", "Freelancer"]},
            'B': {"response": "Spend it fast, live in the moment, even though it might be risky.", "type": "C", "archetypes": ["Freelancer", "Loose Screw", "Crashout"]},
            'C': {"response": "Turn it into something even bigger, I’ll find a buyer and people pay good money for certain goods.", "type": "S", "archetypes": ["Hustler", "Tycoon", "Luxury Lifestyle"]},
            'D': {"response": "Hide it and lay low for a while. Maybe I can use it later for something useful.", "type": "S", "archetypes": ["Innocent Civ", "Freelancer", "Mastermind"]}
        }
    )
]
def civilian_assessment():
    civilian_points = 0
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
        "Hustler": 0,
        "Freelancer": 0
    }
    for question, answers in civilian_questions:
        print(question)
        for option, details in answers.items():
            print(f"{option}: {details['response']}")

        answer = input("Your choice: ").upper()

        if answer in answers:
            if answers[answer]["type"] == "S":
                civilian_points += 1

            for archetype in answers[answer]["archetypes"]:
                archetype_tally[archetype] += 1
        else:
            print("Invalid choice, please try again.")
            return civilian_assessment()

    print("\n[DEBUG] Archetype Tally:")
    for archetype, score in archetype_tally.items():
        print(f"{archetype}: {score}")

    return "Civilian", archetype_tally
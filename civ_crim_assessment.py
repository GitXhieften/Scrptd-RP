def personality_assessment():
    # Define the questions, responses, and associated archetypes
    questions = [
        (
           "How do you deal with confrontation?",
            {
                'A': {"response": "Avoid it. Let people have their moment.", "type": "S", "archetypes": ["Public Servant", "Innocent Civ"]},
                'B': {"response": "Talk it out until things get settled.", "type": "S", "archetypes": ["Chameleon", "Public Servant", "Mastermind"]},
                'C': {"response": "Try to intimidate your way out of it.", "type": "C", "archetypes": ["Loose Screw", "Crashout", "Tycoon"]},
                'D': {"response": "Get physical and resolve it that way.", "type": "C", "archetypes": ["Loose Screw", "Crashout"]} 
            }
        ),
        (
            "You’re at a bar/party when someone insults you. What’s your first reaction?",
            {
                'A': {"response": "Laugh it off, they’re probably just drunk.", "type": "S", "archetypes": ["Luxury Lifestyle", "Tycoon, "Innocent Civ"]},
                'B': {"response": "Brush it off, but keep an eye on them.", "type": "S", "archetypes": ["Hustler", "Mastermind", "Tycoon"]},
                'C': {"response": "Confront them and let them know they’re out of line.", "type": "C", "archetypes": ["Loose Screw", "Luxury Lifestyle", "Crashout"]},
                'D': {"response": "Knock them out and their drink.", "type": "C", "archetypes": ["Loose Screw", "Crashout"]}
            }
        ),
        (
            "What do you think about obeying the law?",
            {
                'A': {
                "response": "They’re more like guidelines, really.",
                "type": "C",  # Criminal-leaning
                "archetypes": ["Tycoon", "Hustler", "Luxury Lifestyle"]
            },
                'B': {
                "response": "Rules are meant to be broken, especially if no one’s looking.",
                "type": "C",  # Criminal-leaning
                "archetypes": ["Crashout", "Go-Getter", "Loose Screw"]
            },
                'C': {
                 "response": "I like following them… but I also like bending them for personal gain.",
                "type": "S",  # Strategic but lawful-leaning
                "archetypes": ["Tycoon", "Mastermind", "Hustler"]
            },
                'D': {
                "response": "I’m all about following the rules… unless it’s inconvenient.",
                "type": "S",  # Still tries to follow the law
                "archetypes": ["Luxury Lifestyle", "Freelancer", "innocent Civ"]
            }
            }   
        ),
        (
            "How do you feel about the police?",
            {
                'A': {"response": "They’re there to help, and I respect them.", "type": "S", "archetypes": ["Public Servant", "Innocent Civ"]},
                'B': {"response": "They’re okay, but I don’t always trust them.", "type": "S", "archetypes": ["Freelancer", "Hustler", "Mastermind"]},
                'C': {"response": "I don’t like dealing with them, & I cant work with them.", "type": "S", "archetypes": ["Freelancer", "Chameleon"]},
                'D': {"response": "I’d rather avoid them at all costs, they’re a problem.", "type": "C", "archetypes": ["Loose Screw", "Crashout", "Mastermind"]}
            }
        ),
         (
            "A car has been left running with the keys in it. What do you do?",
            {
                'A': {"response": "Jump in and drive away, free car, baby!", "type": "C", "archetypes": ["Crashout", "Loose Screw"]},
                'B': {"response": "Consider stealing it but decide against it because you’re ‘better than that’.", "type": "S", "archetypes": ["Hustler", "Tycoon", "Mastermind"]},
                'C': {"response": "Call the police to report it, but only to see what happens.", "type": "S", "archetypes": ["Public Servant", "Innocenent Civ"]},
                'D': {"response": "Look around to see if it’s a 'hot' car before making your move.", "type": "C", "archetypes": ["Chameleon", "Go-Getter"]}
            },
        ),
        (   
             "Someone offers you an easy way to make quick cash (questionable means). What do you do?",
            {
                'A': {"response": "Politely refuse and walk away.", "type": "S", "archetypes": ["Public Servant", "Innocent Civ"]},
                'B': {"response": "Take it, but only if it doesn’t hurt anyone.", "type": "S", "archetypes": ["Hustler", "Freelancer"]},
                'C': {"response": "Consider it, as long as it’s a one-time thing.", "type": "C", "archetypes": ["Loose Screw", "Crashout"]},
                'D': {"response": "Jump at the opportunity, cash is cash.", "type": "C", "archetypes": ["Crashout", "Go-Getter"]}
            }
        ),
        (   
             "What do you do when you’re caught by the cops?",
            {
                'A': {"response": "I’ll lie my way out of it, no problem.", "type": "S", "archetypes": ["Hustler", "Chameleon", "Crashout"]},
                'B': {"response": "I’ma try to talk my way out of it.", "type": "S", "archetypes": ["Mastermind", "Tycoon", "Go-Getter"]},
                'C': {"response": "I’m ready to go down fighting. I’ll blast my way out", "type": "C", "archetypes": ["Loose Screw", "Crashout"]},
                'D': {"response": "I’ll take it on the chin, no problem, I’m not backing down.", "type": "C", "archetypes": ["Public Servant", "Innocent Civ", "Luxury Lifestyle"]}
            } 
        ),
    ]


    # Initialize counters
    civilian_points = 0
    criminal_points = 0
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
    # Ask questions
    for i, (question, answers) in enumerate(questions, 1):
        print(f"\nQuestion {i}: {question}")
        for option, data in answers.items():
            print(f"{option}: {data['response']}")

        answer = input("Your choice (A/B/C/D): ").strip().upper()
        while answer not in answers:
            print("Invalid answer. Try again.")
            answer = input("Your choice (A/B/C/D): ").strip().upper()

        if answers[answer]["type"] == "C":
            criminal_points += 1
        elif answers[answer]["type"] == "S":
            civilian_points += 1
        for archetype in answers[answer]["archetypes"]:
            archetype = archetype.strip().title()  # Normalize spacing/case
            if archetype in archetype_tally:
                archetype_tally[archetype] += 1
            else:
                print(f"[Warning] Unknown archetype: {archetype}")

    # Determine role
    if criminal_points > civilian_points:
        role = "Criminal"
    elif civilian_points > criminal_points:
        role = "Civilian"
    else:
        role = "Balanced"

    return role, archetype_tally


# List of questions for Civilian Assessment

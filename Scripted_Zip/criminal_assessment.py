
# criminal_assessment.py

# Clean criminal questions with correct activity branches
criminal_questions = [
     (
        "When it comes to making money illegally, what’s your approach?",
        {
            'A': {
                "response": "Big profits, big risks. I’m all about the major deals, whether it’s drugs, weapons, or anything that pays big.",
                "archetypes": ["Crashout", "Loose Screw"],
                "criminal_activity": ["street", "arms dealing", "drug dealing", "organized crime", "freelancer"]
            },
            'B': {
                "response": "Stay low, keep it simple, I like to stick to small-time risk and work my way up.",
                "archetypes": ["Chameleon", "Mastermind"],
                "criminal_activity": ["street", "drug dealing", "freelancer"]
            },
            'C': {
                "response": "I’ve got a lot of connections, I work with a network of suppliers and buyers, moving product and making cash.",
                "archetypes": ["Go-Getter", "Chameleon"],
                "criminal_activity": ["organized crime", "drug dealing", "freelancer"]
            },
            'D': {
                "response": "I’m a smooth operator, I deal with high-end clients and keep things clean, no questions asked.",
                "archetypes": ["Mastermind", "Go-Getter"],
                "criminal_activity": ["arms dealing", "organized crime", "freelancer"]
            }
        }
    ),
    (
        "You’re in a tight spot, and you need cash now. What’s your move?",
        {
            'A': {
                "response": "Hit the streets. Rob a store or bank.",
                "archetypes": ["Crashout", "Loose Screw"],
                "criminal_activity": ["street"]
            },
            'B': {
                "response": "Scheme and manipulate. A few calls, some lies, and I’ll make this cash real quick.",
                "archetypes": ["Loose Screw", "Chameleon"],
                "criminal_activity": ["organized crime", "freelancer"]
            },
            'C': {
                "response": "Make a deal. I know people who can get me product. Time to hustle.",
                "archetypes": ["Go-Getter", "Mastermind"],
                "criminal_activity": ["drug dealing","organized crime", "freelancer"]
            },
            'D': {
                "response": "Do some risky business. Get my hands on something hot and flip it fast.",
                "archetypes": ["Chameleon", "Go-Getter"],
                "criminal_activity": ["arms dealing", "organized crime", "street"]
            }
        }
    ),
    (
        "You get a phone call letting you in on a major play. What’s your reaction?",
        {
            'A': {
                "response": "Count me in, I’m ready for a major game changer. I want to be at the top of the game.",
                "archetypes": ["Go-Getter", "Crashout"],
                "criminal_activity": ["arms dealing", "organized crime"]
            },
            'B': {
                "response": "As long as its not too risky, I’ll consider it if the price is right, but I'm good with Low-key moves. ",
                "archetypes": ["Mastermind", "Go-Getter"],
                "criminal_activity": ["street", "drug dealing"]
            },
            'C': {
                "response": "I’m a middleman the play if they dont want me to handle the deal myself.",
                "archetypes": ["Loose Screw", "Go-getter"],
                "criminal_activity": ["organized crime", "freelancer", "street"]
            },
            'D': {
                "response": "If its not my scene, I’ll pass. I’m more down with less risk but still makes good money.",
                "archetypes": ["Chameleon", "Mastermind"],
                "criminal_activity": ["freelancer", "drug dealing"]
            }
        }
    ),
        (
        "You’ve got a stash of stolen goods (guns, drugs, luxury items). What’s your next step?",
        {
            'A': {
                "response": "Sell everything to the highest bidder and get out fast.",
                "archetypes": ["Crashout", "Loose Screw"],
                "criminal_activity": ["street", "arms dealing"]
            },
            'B': {
                "response": "Move the drugs first, then I’ll deal with the weapons later.",
                "archetypes": ["Go-Getter", "Loose Screw"],
                "criminal_activity": ["drug dealing", "organized crime"]
            },
            'C': {
                "response": "Use the goods as leverage, I’ll get a higher price by dealing with specific cleintele.",
                "archetypes": ["Mastermind", "Chameleon"],
                "criminal_activity": ["organized crime", "arms dealing", "freelancer"]
            },
            'D': {
                "response": "Start laundering the money from the stolen goods, no need to risk a hot deal.",
                "archetypes": ["Mastermind", "Go-Getter", "Chameleon"],
                "criminal_activity": ["organized crime", "freelancer"]
            }
        }
    ),
    (
        "Someone from your own crew starts acting shady. What do you do?",
        {
            'A': {
                "response": "Confront them directly, loyalty is everything.",
                "archetypes": ["Crashout", "Loose Screw"],
                "criminal_activity": ["street", "organized crime"]
            },
            'B': {
                "response": "Keep an eye on them, don’t start drama unless it’s necessary.",
                "archetypes": ["Loose Screw", "Chameleon"],
                "criminal_activity": ["organized crime", "drug dealing", "freelancer"]
            },
            'C': {
                "response": "Call for a vote from the crew, handle it together.",
                "archetypes": ["Mastermind", "Chameleon"],
                "criminal_activity": ["organized crime", "arms dealing"]
            },
            'D': {
                "response": "Ignore it, as long as it doesn’t threaten the larger operation.",
                "archetypes": ["Go-Getter", "Loose Screw"],
                "criminal_activity": ["street","freelancer"]
            }
        }
    ),
        (
        "How do you handle a betrayal from a trusted member of your organization?",
        {
            'A': {
                "response": "Cut them off immediately and make an example of them.",
                "archetypes": ["Crashout", "Loose Screw"],
                "criminal_activity": ["street", "organized crime", "freelancer", "arms dealing"]
            },
            'B': {
                "response": "Work with them to understand the reasons behind their actions.",
                "archetypes": ["Mastermind", "Chameleon"],
                "criminal_activity": ["freelancer", "organized crime"]
            },
            'C': {
                "response": "Take my time and plan a subtle retaliation.",
                "archetypes": ["Mastermind", "Chameleon", "Go-Getter"],
                    "criminal_activity": ["organized crime", "street", "arms dealing"]
            },
            'D': {
                "response": "Forgive them and give them another chance to prove loyalty.",
                "archetypes": ["Chameleon", "Loose Screw"],
                "criminal_activity": ["drug dealing", "freelancer"]
            }
        }
    ),
    (
        "You’re given the chance to move up in your crew, but it requires doing something shady. What do you do?",
        {
            'A': {
                "response": "Take it, what’s the worst that could happen? It’s just business.",
                "archetypes": ["Crashout", "Go-Getter"],
                "criminal_activity": ["street", "drug dealing"]
            },
            'B': {
                "response": "Think it through, there’s got to be a way to benefit without risking too much.",
                "archetypes": ["Mastermind", "Chameleon"],
                "criminal_activity": ["organized crime", "arms dealing"]
            },
            'C': {
                "response": "Do it, but only if you can control the consequences.",
                "archetypes": ["Loose Screw", "Mastermind"],
                "criminal_activity": ["organized crime", "freelancer"]
            },
            'D': {
                "response": "Turn it down, unless there’s no other choice.",
                "archetypes": ["Chameleon","Mastermind"],
                "criminal_activity": ["freelancer", "organized crime"]
            }
        }
    )

]
#ask questions
def criminal_assessment():
    criminal_activity_tally = {
        "street": 0,
        "organized crime": 0,
        "drug dealing": 0,
        "arms dealing": 0,
        "freelancer": 0
    }

    archetype_tally = {
        "Crashout": 0, "Loose Screw": 0, "Go-Getter": 0,
        "Mastermind": 0, "Chameleon": 0
    }

    for i, (question, answers) in enumerate(criminal_questions, 1):
        print(f"\nQuestion {i}: {question}")
        for option, data in answers.items():
            print(f"{option}: {data['response']}")

        answer = input("Your choice (A/B/C/D): ").strip().upper()
        while answer not in answers:
            print("Invalid choice, try again.")
            answer = input("Your choice (A/B/C/D): ").strip().upper()

        for archetype in answers[answer]["archetypes"]:
            archetype_tally[archetype] += 1

        for activity in answers[answer]["criminal_activity"]:
            criminal_activity_tally[activity] += 1

    dominant_activity = max(criminal_activity_tally, key=criminal_activity_tally.get)
    print(f"\nDominant Criminal Activity: {dominant_activity.capitalize()}")

    print("\n[DEBUG] Archetype Tally:")
    for archetype, score in archetype_tally.items():
        print(f"{archetype}: {score}")

    return dominant_activity, archetype_tally, criminal_activity_tally
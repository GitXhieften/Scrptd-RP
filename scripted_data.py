# --- Role Definitions ---

roles = {
    "civilian": {
        "1st_tier": [
            "Employee/unemployed", "Police/CO", "Transportation/Waste Management", "Hospital nurse", "EMS", "Wrecker",
            "Bar tender", "Military", "College student", "Wood cutter", "Material delivery", "Smelter", "Miner",
            "Barber/Stylist/Tattoo Artist", "Material fields", "Butcher", "Recycling", "Corner store", "Retail shop",
            "Car salesmen", "Hood-rural-poor real-estate sales", "Weed grower", "Hollywood wanna-be"
        ],
        "2nd_tier": [
            "Local Politician", "Police Sarg", "Judge", "Doctor", "Property Manager", "Business Owner", "Bar tender",
            "Car salesmen", "Lofts and decent real-estate property manager", "Informant", "Crooked cop", "Gang unit detective",
            "Murder detective", "Weed farmer", "Construction", "Actor/Actress", "Military", "Corner store", "Retail shop", "Police/CO"
        ],
        "3rd_tier": [
            "Business Owner", "Real Estate", "Undercover/informant", "Prison Warden","Retail shop", "Military", "Actor/Actress", 
            "Task Force Police/CO", "Construction", "Manager/Lead/Exec", "Weed farmer", "Doctor", "Police/CO",
            "Barber/Stylist/Tattoo Artist", "Bar tender", "Employee/unemployed", "Hospital nurse", "EMS", "Property manager"
        ]
    }
}

criminal_roles = {
        "Tier 1": {
        "street_gang": ["Corner Boy", "Runner", "Small Arms Dealer", "Street Soldier"],
        "drug_dealer": ["Low-tier Dealer", "Weed Dealer", "Street-level Cartel Member"],
        "freelance_criminal": ["Armed Robber", "Car Thief", "Street Hustler"],
    },
        "Tier 2": {
        "street_gang": ["Corner Boy", "Runner", "Small Arms Dealer", "Street Soldier"],
        "drug_dealer": ["Low-tier Dealer", "Weed Dealer", "Street-level Cartel Member"],
        "freelance_criminal": ["Armed Robber", "Car Thief", "Street Hustler"],

    },
        "Tier 3": {
        "street_gang": ["Corner Boy", "Runner", "Small Arms Dealer", "Street Soldier"],
        "drug_dealer": ["Low-tier Dealer", "Weed Dealer", "Street-level Cartel Member"],
        "freelance_criminal": ["Armed Robber", "Car Thief", "Street Hustler"],

    }
}


# --- Archetype Definitions ---

archetypes_definitions = {
    "Tycoon": {
        "role": "Civilian",
        "description": "Strategic and profit-focused legal empire builder.",
        "traits": ["Strategic", "Wealth-Oriented", "Entrepreneurial", "Visionary"]
    },
    "Crashout": {
        "role": "Criminal",
        "description": "Risk-taker who acts without hesitation.",
        "traits": ["Impulsive", "Risk-Taker", "Reckless"]
    },
    "Loose Screw": {
        "role": "Criminal",
        "description": "Unpredictable and chaotic troublemaker.",
        "traits": ["Erratic", "Unpredictable", "Chaotic"]
    },
    "Go-Getter": {
        "role": "Criminal",
        "description": "Ambitious and driven opportunist.",
        "traits": ["Ambitious", "Driven", "Opportunistic"]
    },
    "Mastermind": {
        "role": "Criminal",
        "description": "Calculating strategist behind complex operations.",
        "traits": ["Strategic", "Planner", "Clever"]
    },
    "Chameleon": {
        "role": "Criminal",
        "description": "Manipulator who adapts to any environment.",
        "traits": ["Adaptable", "Manipulative", "Strategic"]
    },
    "Public Servant": {
        "role": "Civilian",
        "description": "Community-focused and law-abiding.",
        "traits": ["Ethical", "Law-Abiding", "Community-Minded"]
    },
    "Innocent Civ": {
        "role": "Civilian",
        "description": "Peaceful and moral non-offender.",
        "traits": ["Moral", "Peaceful", "Law-Abiding"]
    },
    "Freelancer": {
        "role": "Civilian",
        "description": "Independent player comfortable in gray zones.",
        "traits": ["Independent", "Adaptable", "Pragmatic"]
    },
    "Hustler": {
        "role": "Civilian",
        "description": "Cunning, profit-driven grinder.",
        "traits": ["Ambitious", "Cunning", "Risk-Taker"]
    }
}

# --- Ethnicity-Based Role Affiliation ---

ethnicity_criminal_affiliations = {
    'Black': {
        'street_gang': ['Crip', 'Blood', 'other'],
        'organized_crime': ['Drug Trafficker', 'Illegal Arms Dealer'],
        'drug_dealer': ['Street Dealer', 'Mid-level Dealer', 'Meth Dealer', 'Cocaine Dealer'],
        'freelance_criminal': ['Armed Robber', 'Heist Burglar', 'Street Dealer', 'Hijacker', 'Drug Trafficker', 'Illegal Arms Dealer']
    },
    'Hispanic': {
        'street_gang': ['MS-13', 'Surenos 13', '18th Street', 'Blood', 'Crip'],
        'organized_crime': ['Cartel Member', 'Drug Trafficker', 'Illegal Arms Dealer'],
        'drug_dealer': ['Street Dealer', 'Mid-level Dealer', 'Meth Dealer', 'Cocaine Dealer'],
        'freelance_criminal': ['Armed Robber', 'Heist Burglar', 'Street Dealer', 'Hijacker', 'Drug Trafficker', 'Illegal Arms Dealer']
    },
    'Asian': {
        'street_gang': ['Wah Ching', 'Asian Boyz'],
        'organized_crime': ['Triad Member', 'Yakuza'],
        'drug_dealer': ['Meth Dealer', 'Heroin Seller'],
        'freelance_criminal': ['Armed Robber', 'Heist Burglar', 'Street Dealer', 'Hijacker', 'Drug Trafficker', 'Illegal Arms Dealer']
    },
    'White': {
        'street_gang': [],
        'organized_crime': ['Mobster', '"1%er"'],
        'drug_dealer': ['Meth Cooker', 'Heroin Seller'],
        'freelance_criminal': ['Armed Robber', 'Heist Burglar', 'Street Dealer', 'Hijacker', 'Drug Trafficker', 'Illegal Arms Dealer']
    },
    'Foreigner': {
        'street_gang': [],
        'organized_crime': ['Mafia', 'Russian Mob', 'Cartel'],
        'drug_dealer': ['Drug Trafficker', 'Drug Connect', 'Illegal Arms Dealer'],
        'freelance_criminal': ['Armed Robber', 'Heist Burglar', 'Street Dealer', 'Hijacker', 'Drug Trafficker', 'Illegal Arms Dealer']
    }
}

# --- Archetype Alignment (for determining role assignment) ---

archetype_alignment = {
    "Crashout": "criminal",
    "Loose Screw": "criminal",
    "Go-Getter": ["criminal", "civilian"],
    "Mastermind": ["criminal", "civilian"],
    "Chameleon": ["criminal", "civilian"],
    "Public Servant": "civilian",
    "Innocent Civ": "civilian",
    "Freelancer": ["civilian", "criminal"],
    "Hustler": ["civilian", "criminal"],
    "Luxury Lifestyle": ["civilian", "criminal"],
    "Tycoon": "civilian"
}

# --- Import Main Survey Logic ---
import random
def assign_civilian_role(tier):
    civilian_roles_list = roles["civilian"].get(tier, [])
    return random.choice(civilian_roles_list) if civilian_roles_list else "Freelancer"

def assign_criminal_role(tier_number):
    tier_key = f"Tier {tier_number}"
    if tier_key in criminal_roles:
        branch = random.choice(list(criminal_roles[tier_key].keys()))
        return random.choice(criminal_roles[tier_key][branch])
    return "No Employment for you, Figure it out yourself."

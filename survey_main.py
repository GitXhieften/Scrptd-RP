# survey_main.py
import random
from civ_crim_assessment import personality_assessment
from civilian_assessment import civilian_assessment
from criminal_assessment import criminal_assessment
from environment import living_environment
from gun_user import firearm_use
from scripted_data import (
    roles,
    criminal_roles,
    archetype_alignment,
    archetypes_definitions,
    assign_civilian_role, 
    assign_criminal_role
)

# filepath: [survey_main.py](http://_vscodecontentref_/3)
def assign_roles_and_archetypes():
    # Step 0: Ethnicity
    valid_ethnicities = {"Black", "Hispanic", "Asian", "White", "Foreigner"}
    while True:
        ethnicity_input = input("What is your ethnicity? (Black, Hispanic, Asian, White, Foreigner) #enter all that apply, separated by commas: ")
        # Split, strip, and capitalize each entry
        ethnicities = [e.strip().capitalize() for e in ethnicity_input.split(",")]
        # Spell check: only keep valid entries
        invalid = [e for e in ethnicities if e not in valid_ethnicities]
        if invalid:
            print(f"Invalid answer(s): {', '.join(invalid)}. Try again.")
        else:
            break
    # If only one ethnicity, keep as string for compatibility
    ethnicity = ethnicities[0] if len(ethnicities) == 1 else ethnicities

    if ethnicity == "Foreigner":
        is_americanized = input("Are you Americanized? (Yes, No, I grew up here, I just got here): ").capitalize()
        if is_americanized == "Yes" or is_americanized == "I grew up here":
            americanized_status = "Legal Immigrant"
        elif is_americanized == "I just got here":
            americanized_status = "Illegal Alien"
        elif is_americanized == "No":        
            americanized_status = "Long-Term Work Visa"
        language = input("What country are you from :").capitalize()
        print(f"You're a {ethnicity} and your Americanized status is: {americanized_status}. You were born in {language}.")
    else:
        americanized_status = "American"  # <-- Add this line
        language = "USA"                  # <-- Add this line
        print(f"Your Nationality : {ethnicity}")

    # Step 1: Personality Assessment
    base_role, base_archetype_tally = personality_assessment()
    print(f"\nAt First Glance, You seem like a Douchebag... ")

    final_archetype_tally = base_archetype_tally.copy()


    # Step 3: Branch logic
    if base_role == "Civilian":
        print("\nBut as a domesticated civilian, let's proceed to determine if you are truly a Good Samaritan...")
        civilian_role, civ_archetype_tally = civilian_assessment()
        for arch, count in civ_archetype_tally.items():
            final_archetype_tally[arch] = final_archetype_tally.get(arch, 0) + count
    else:
        print("\n You may have {base_role} tendencies.")
        dominant_criminal_activity, crim_archetype_tally, _ = criminal_assessment()
        for arch, count in crim_archetype_tally.items():
            final_archetype_tally[arch] = final_archetype_tally.get(arch, 0) + count

    # Step 4: Gun Use Assessment (always before tier assignments)
    gun_profile, gun_archetype_tally, gun_archetype_trait_tally = firearm_use()
    for archetype, count in gun_archetype_trait_tally.items():
        final_archetype_tally[archetype] = final_archetype_tally.get(archetype, 0) + count



        # Step 2: Living Environment Assessment (always before job assignments)
    preferred_env, environment_tally, env_archetype_tally = living_environment()
    for archetype, count in env_archetype_tally.items():
        final_archetype_tally[archetype] = final_archetype_tally.get(archetype, 0) + count



    # Step 5: Determine role and archetype from tally
    final_role, assigned_archetype = determine_final_role(final_archetype_tally)

    archetype_description = archetypes_definitions.get(assigned_archetype, {}).get("description", "No description available.")

    # Step 6: Tier + Job Assignment
    print("\nNow, please choose your tier:")
    tier_input = input("Select your tier (1st, 2nd, 3rd): ").strip().lower()
    tier_map = {"1st": "1st_tier", "2nd": "2nd_tier", "3rd": "3rd_tier"}

    if final_role == "Civilian":
        civilian_role_assigned = assign_civilian_role(tier_map.get(tier_input, "1st_tier"))
        print(f"Job Role: {civilian_role_assigned}")
        job_role = civilian_role_assigned
    else:
        criminal_role_assigned = assign_criminal_role(tier_input)
        print(f"Criminal Role: {criminal_role_assigned}")
        job_role = criminal_role_assigned

    # Step 7: Final Summary
    print("\n[FINAL]  Personality Archetypes :")
    for archetype, score in final_archetype_tally.items():
        print(f"   {archetype}: {score}")

    print(f"\n🧠 ASSIGNMENT: {final_role} | Personality Type: {assigned_archetype}")
    print(f"🔍 Traits: {archetype_description}")
    print(f"Race: {ethnicity, americanized_status}")
    print(f"🌆 Birthplace: {language}")
    print(f"🏙️ Neighborhood : {preferred_env}")
    print(f"🔫 Firearm Use: {gun_profile}")
    if final_role == "Civilian":
        dominant_activity = civilian_role if 'civilian_role' in locals() else "N/A"
    else:
        dominant_activity = dominant_criminal_activity if 'dominant_criminal_activity' in locals() else "N/A"
    print(f"Activity: {dominant_activity}")
    print(f"Job Role: {job_role}")
    # Optionally, return all relevant values for further use or testing

    return {
        "final_role": final_role,
        "assigned_archetype": assigned_archetype,
        "archetype_description": archetype_description,
        "ethnicity": ethnicity,
        "americanized_status": locals().get("americanized_status", "N/A"),
        "birthplace": locals().get("language", "N/A"),
        "preferred_env": preferred_env,
        "gun_profile": gun_profile,
        "dominant_activity": dominant_activity,
        "job_role": job_role,
    }
    

def determine_final_role(archetype_tally):
    max_score = max(archetype_tally.values())
    top_archetypes = [a for a, score in archetype_tally.items() if score == max_score]

    print(f"\nTop Archetypes (Score: {max_score}): {top_archetypes}")

    assigned_archetype = random.choice(top_archetypes)
    print(f"\nAssigned Archetype: {assigned_archetype}")

    alignment = archetype_alignment.get(assigned_archetype)

    if isinstance(alignment, list):
        role = "Civilian"
        print(f"Note: '{assigned_archetype}' personality type is straddling the fence. whether you are going to be a criminal is up to you")
    elif alignment == "civilian":
        role = "Civilian"
    elif alignment == "criminal":
        role = "Criminal"
    else:
        role = "whether you are going to be a criminal is up to you"

    return role, assigned_archetype
    



#initialize the Assessment
if __name__ == "__main__":
    assign_roles_and_archetypes()
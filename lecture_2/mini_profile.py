def generate_profile(age: int) -> str:
    """
    Determine the user's life stage based on age.
    
    Args:
        age (int): User's age
        
    Returns:
        str: Life stage - "Child", "Teenager", or "Adult"
    """
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif age >= 20:
        return "Adult"


def main():
    """
    Main function coordinating the profile creation process.
    """
    # Get basic information
    user_name = input("Enter your full name: ").strip()
    
    # Get birth year with basic error handling
    CURRENT_YEAR = 2025
    
    while True:
        try:
            birth_year_str = input("Enter your birth year: ").strip()
            birth_year = int(birth_year_str)
            
            # Basic validation - year shouldn't be in the future
            if birth_year > CURRENT_YEAR:
                print(f"Birth year cannot be in the future. Please enter a year up to {CURRENT_YEAR}.")
                continue
                
            break
        except ValueError:
            print("Please enter a valid number for birth year")
    
    # Calculate age
    current_age = CURRENT_YEAR - birth_year
    
    # Get hobbies
    hobbies = []
    while True:
        hobby = input("Enter a favorite hobby or type 'stop' to finish: ").strip()
        if hobby.lower() == 'stop':
            break
        elif hobby:  # Only add non-empty hobbies
            hobbies.append(hobby)
    
    # Generate profile
    life_stage = generate_profile(current_age)
    
    # Create user profile dictionary
    user_profile = {
        'name': user_name,
        'age': current_age,
        'life_stage': life_stage,
        'hobbies': hobbies
    }
    
    # Display profile summary (exactly as specified in requirements)
    print("\n---")
    print("Profile Summary:")
    print(f"Name: {user_profile['name']}")
    print(f"Age: {user_profile['age']}")
    print(f"Life Stage: {user_profile['life_stage']}")
    
    # Check and display hobbies exactly as required
    if not user_profile['hobbies']:
        print("You didn't mention any hobbies.")
    else:
        print(f"Favorite Hobbies ({len(user_profile['hobbies'])}):")
        for hobby in user_profile['hobbies']:
            print(f"- {hobby}")
    print("---")


if __name__ == "__main__":
    main()
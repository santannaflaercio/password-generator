import json
import random
import sys


# Open and load the JSON configuration file
def load_config():
    # Open and load the JSON configuration file
    with open("config/config.json", "r") as f:
        return json.load(f)


def generate_password():
    """
    Function to generate a password based on the configuration file.

    The function first sets the default characters for the password.
    Then, it checks if digits and symbols are required in the password.
    If they are, it adds them to the characters.
    Finally, it generates a password of the specified length from these characters.

    Returns:
        str: The generated password
    """
    config_json = load_config()

    # Extract specific requirements and number of passwords from the configuration
    specific_requirements = config_json["specific_requirements"]

    # Start with the default characters
    characters = config_json["default_characters"]
    # If digits are required, add them to the characters
    if specific_requirements["digits"]:
        characters += config_json["allowed_digits"]
    # If symbols are required, add them to the characters
    if specific_requirements["symbols"]:
        characters += config_json["allowed_symbols"]

    # Generate a password of the specified length from the characters
    password = "".join(random.choice(characters) for _ in range(config_json["password_length"]))
    return password


# Print the generated password
print(generate_password())

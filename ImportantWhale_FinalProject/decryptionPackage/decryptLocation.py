# Name: Sarah Mahan, Denise Huynh, Quynh Doan, Roman Stryjewski
# email:  mahansa@mail.uc.edu, huynhd2@mail.uc.edu, doanqb@mail.uc.edu, stryjerj@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 12/10/24 7:00AM
# Course #/Section:   IS4010 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment: Decrypt information, use information to make assignment requirements, take selfie and display

# Brief Description of what this module does: Uses data from fileProcessing to perform decryption for location requirement, outputs results
# Citations: ChatGPT
# Anything else that's relevant:

# decryptLocation.py

from utilitiesPackage.fileProcessing import load_text, load_json, validate_team_data

def decrypt_location(english_file_path, json_file_path, team_name):
    """
    Decrypt the location data for a given team based on indices from the JSON file.

    Parameters:
        english_file_path (str): Path to the UCEnglish.txt file.
        json_file_path (str): Path to the EncryptedGroupHints.json file.
        team_name (str): Name of the team to decrypt the location for.

    Returns:
        str: Decrypted location string, or None if an error occurs.
    """
    try:
        # Load the English words file
        english_lines = load_text(english_file_path)
        if english_lines is None:
            raise ValueError(f"Failed to load the English file: {english_file_path}")

        # Load the JSON file with encrypted indices
        encrypted_data = load_json(json_file_path)
        if encrypted_data is None:
            raise ValueError(f"Failed to load the JSON file: {json_file_path}")

        # Validate that the team name exists in the JSON file
        if not validate_team_data(encrypted_data, team_name):
            raise ValueError(f"Team '{team_name}' not found in the JSON file.")

        # Retrieve the indices for the team
        encrypted_indices = encrypted_data[team_name]

        # Map each index to the corresponding word in the English file
        decrypted_words = []
        for index in encrypted_indices:
            # Convert index from string to integer and adjust for zero-based indexing
            line_number = int(index) 
            if 0 <= line_number < len(english_lines):
                word = english_lines[line_number]
                print(f"Index {index} -> Word: {word.strip()}")  # Debugging output
                decrypted_words.append(word.strip())
            else:
                raise ValueError(f"Index {index} is out of bounds for the English file.")
            
        return ' '.join(decrypted_words)

    except ValueError as e:
        print(f"Value error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

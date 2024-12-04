# Name: Sarah Mahan, Denise Huynh, Quynh Doan, Roman Stryjewski
# email:  mahansa@mail.uc.edu, huynhd2@mail.uc.edu, doanqb@mail.uc.edu, stryjerj@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 12/10/24 7:00AM
# Course #/Section:   IS4010 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment:  

# Brief Description of what this module does:
# Citations:
# Anything else that's relevant:

# decryptLocation.py
import json

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
    from utilitiesPackage.fileProcessing import load_text, load_json

    try:
        english_lines = load_text(english_file_path)
        if english_lines is None:
            raise ValueError(f"Failed to load the English file: {english_file_path}")

        encrypted_data = load_json(json_file_path)
        if encrypted_data is None:
            raise ValueError(f"Failed to load the JSON file: {json_file_path}")

        # Retrieve indices and decrypt the location
        encrypted_indices = encrypted_data[team_name]
        decrypted_location = []
        for index in encrypted_indices:
            line_number = int(index) - 1  # Convert 1-based index to 0-based index
            if 0 <= line_number < len(english_lines):
                # Debugging output
                print(f"Index {index} -> Line {line_number + 1}: {english_lines[line_number].strip()}")
                decrypted_location.append(english_lines[line_number])
            else:
                raise ValueError(f"Index {index} is out of bounds for the English file.")

        return ' '.join(decrypted_location)

    except ValueError as e:
        print(f"Value error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

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

# main.py

from decryptionPackage import *
from decryptionPackage.decryptLocation import decrypt_location
from utilitiesPackage.fileProcessing import load_json, load_text, validate_team_data
from visualizationPackage import *
from decryptionPackage.decryptLocation import decrypt_location

if __name__ == "__main__":
    # File paths
    location_file = "dataFiles/EncryptedGroupHints Fall 2024 Section 001.json"
    text_file = "dataFiles/UCEnglish.txt"
    movie_file = "dataFiles/TeamsAndEncryptedMessagesForDistribution.json"
    team_name = "ImportantWhale"  

    # Load JSON files
    location_data = load_json(location_file)
    movie_data = load_json(movie_file)

    # Load text file
    text_data = load_text(text_file)

     # Validate team data
    if location_data and validate_team_data(location_data, team_name):
        print("Location data for the team is valid.")
    if movie_data and validate_team_data(movie_data, team_name):
        print("Movie data for the team is valid.")

    # Preview of text data
    if text_data:
        print("\nPreview of UCEnglish.txt (First 10 lines):")
        print(text_data[:10])

    # Invoke:
    # decryptLocation function here
    try:
        decrypted_location = decrypt_location(text_file, location_file, team_name)
        if decrypted_location:
            print("\nDecrypted Location:")
            print(decrypted_location)
        else:
            print("\nFailed to decrypt the location. Please check the files and inputs.")
    except Exception as e:
         print(f"Error during location decryption: {e}")

    # decryptMovie function here

    # visualizationDisplay photo call here
    # decryptLocation message here
    # decryptMovie message here
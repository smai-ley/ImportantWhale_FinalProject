# Name: Sarah Mahan, Denise Huynh, Quynh Doan, Roman Stryjewski
# email:  mahansa@mail.uc.edu, huynhd2@mail.uc.edu, doanqb@mail.uc.edu, stryjerj@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 12/10/24 7:00AM
# Course #/Section:   IS4010 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment: Decrypt information, use information to make assignment requirements, take selfie and display

# Brief Description of what this module does: Contains the function to perform fernet decryption with encrypted data bit string and aes key
# Citations: Copilot, Gemini
# Anything else that's relevant:

# decryptMovie.py

from cryptography.fernet import Fernet

def decrypt_data(encrypted_data, key):
    """
    Decrypts the     data provided using the key
    @param encrypted_data: the encrypted data
    @param key: the unique key for decryption
    @return decrypted_data: the decrypted data
    """
    try:
        fernet = Fernet(key) # Decrypt the data 
        decrypted_data = fernet.decrypt(encrypted_data) 

        return decrypted_data.decode()

    except Exception as e: 
        print(f"An error occurred: {e}") 
        return None

    

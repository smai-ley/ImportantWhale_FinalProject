# Name: Sarah Mahan, Denise Huynh, Quynh Doan, Roman Stryjewski
# email:  mahansa@mail.uc.edu, huynhd2@mail.uc.edu, doanqb@mail.uc.edu, stryjerj@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 12/10/24 7:00AM
# Course #/Section:   IS4010 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment:  
# Brief Description of what this module does: This file processes the data from dataFiles, and returns the outputs to be processed by
# decryptLocation and decryptMovie
# Citations:
# Anything else that's relevant:

# fileProcessing.py

import json

def load_json(file_path):
    """
    Load and return the contents of a JSON file.
    
    :param file_path: Path to the JSON file.
    :return: Parsed JSON object.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' is not a valid JSON.")
        return None

def load_text(file_path):
    """
    Load and return the contents of a text file as a list of lines.
    
    :param file_path: Path to the text file.
    :return: List of lines in the file.
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return [line.strip() for line in lines]
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None

def validate_team_data(json_data, team_name):
    """
    Validate if the team data exists in the JSON object.

    :param json_data: The JSON data to search.
    :param team_name: The team name to validate.
    :return: True if the team data exists, False otherwise.
    """
    if team_name in json_data:
        return True
    print(f"Error: Team '{team_name}' not found in the JSON data.")
    return False
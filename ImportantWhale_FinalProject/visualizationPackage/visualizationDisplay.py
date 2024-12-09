# Name: Sarah Mahan, Denise Huynh, Quynh Doan, Roman Stryjewski
# email:  mahansa@mail.uc.edu, huynhd2@mail.uc.edu, doanqb@mail.uc.edu, stryjerj@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 12/10/24 7:00AM
# Course #/Section:   IS4010 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment: Decrypt information, use information to make assignment requirements, take selfie and display

# Brief Description of what this module does: Loads an image from dataFiles and displays usiung matplotlib
# Citations: Copilot, Gemini
# Anything else that's relevant:

# visualizationDisplay.py

import matplotlib.pyplot as plt

def displayImage():
    """
    Displays an image in dataFiles
    @param none
    """
    img = plt.imread("dataFiles/groupPicture.jpeg")

    plt.imshow(img)
    plt.title("Wow! Look at these AMAZING UC Students!")
    plt.axis('off')  # Hide axis ticks
    plt.show()

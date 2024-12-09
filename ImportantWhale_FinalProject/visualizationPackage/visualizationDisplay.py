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

# visualizationDisplay.py


def visualizationDisplay():
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg

    # Load an image from a file
    img = mpimg.imread('datafiles/groupPicture.jpeg')

    # Display the image
    plt.imshow(img)
    plt.axis('off')  # Hide axes
    plt.show()

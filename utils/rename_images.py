import os
import shutil
import sys

def rename_images(directory, new_directory): 
    """A function to rename images taking arguments of the image directory and new directory to save renamed images."""
    
    os.chdir(directory)
    os.mkdir(new_directory) 
    save_path = new_directory
    """
    os.chdir changes the current working directory to the directory passed when calling the function.
    os.mkdir to make the new directory to store the renamed images.
    save_path is a variable storing the directory path to save the renamed images.
    """

    for f in os.listdir(directory):
        """A for loop to look throught the image directory and rename one by one."""
        
        f_name, f_ext = os.path.splitext(f)
        f_title = f_name.replace(', ','_').replace('-','_').replace(' ','_').lower()  
        """
        First we separate the image name and extension so as to make changes to the image name.
        Next we eliminate comas, spaces and hyphens and replace them with underscores.
        We also use the .lower() function to change all letters to small case.
        """

        new_name = ('{}{}'.format(f_title, f_ext.lower()))
        shutil.copy(f, save_path+"/"+new_name)
        """
        We then combine the new image name with its extension and use the .lower() function to ensure lowercase letters.
        We use the shutil module to copy the renamed images into the new directory.
        """
    
rename_images(sys.argv[1] , sys.argv[2])
"""
We call the rename_image() function using sys.argv module so accomodate comandline arguments such as
    python rename_images.py "../images" "../img"
this runs the python file while passing in the images directory and new directory to store the renamed images.
"""
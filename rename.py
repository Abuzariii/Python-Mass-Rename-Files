# Rename
# import os

# folder_path = '.'  # Assumes the Python file is in the same folder

# python_file = __file__  # Get the filename of the Python script itself
# prefix_length = 12  # Replace with the number of characters to remove


# for filename in os.listdir(folder_path):
#     if filename != python_file and not filename.endswith('.py'):
#         new_filename = filename[prefix_length:]  # Remove the first few characters
#         old_path = os.path.join(folder_path, filename)
#         new_path = os.path.join(folder_path, new_filename)
#         os.rename(old_path, new_path)




# Undo Rename
# import os

# folder_path = '.'  # Assumes the Python file is in the same folder
# prefix_length = 13  # Replace with the number of characters that were removed


# for filename in os.listdir(folder_path):
#     if filename.endswith('.py'):  # Exclude the Python file itself
#         continue
#     new_filename = filename[:prefix_length] + filename  # Add the removed characters back
#     old_path = os.path.join(folder_path, filename)
#     new_path = os.path.join(folder_path, new_filename)
#     os.rename(old_path, new_path)

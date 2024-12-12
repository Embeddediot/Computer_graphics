import os
import shutil

def copy_images(source_dir, target_dir, base_names):
    """
    Copies images from the source directory to the target directory based on the provided base names.

    Args:
        source_dir (str): Path to the root source directory.
        target_dir (str): Path to the target directory.
        base_names (list of str): List of base name prefixes to match (e.g., 'cykel_20_', 'cykel_35_', 'vej_2_25_').
    """
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Iterate through the base names to search for
    for base_name in base_names:
        for root, _, files in os.walk(source_dir):
            for file in files:
                if file.startswith(f"combined_{base_name}") and file.endswith(".png"):
                    source_path = os.path.join(root, file)
                    target_path = os.path.join(target_dir, file)

                    # Copy the file
                    shutil.copy2(source_path, target_path)
                    print(f"Copied: {source_path} -> {target_path}")

if __name__ == "__main__":
    # Define the source and target directories
    source_directory = r"C:\Users\bjs\Downloads\tiles"
    target_directory = r"C:\Users\bjs\Downloads\selected_tiles"

    # List of base names to look for
    base_names_to_match = ["cykel_20_", "cykel_35_", "vej_2_25_"]

    # Call the function
    copy_images(source_directory, target_directory, base_names_to_match)
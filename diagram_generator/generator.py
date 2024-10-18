import os
import subprocess
import sys

DIAGRAMS_FOLDER = "diagrams"
OUTPUT_FOLDER = "output_diagrams"


def generate_diagram(diagram_path):
    """Generate a diagram from a specific Python script."""
    # Ensure the output folder exists
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    # Check if the diagram file exists
    if not os.path.isfile(diagram_path):
        print(f"Error: Diagram file '{diagram_path}' not found.")
        return

    # Generate the output filename based on the relative path of the script
    relative_path = os.path.relpath(diagram_path, DIAGRAMS_FOLDER)
    output_filename = os.path.join(OUTPUT_FOLDER, os.path.splitext(relative_path)[0])

    # Ensure output subdirectories are created
    os.makedirs(os.path.dirname(output_filename), exist_ok=True)

    print(f"Generating diagram from {diagram_path}...")

    # Run the diagram generation script
    subprocess.run(["poetry", "run", "python", diagram_path])

    print(f"Diagram {output_filename}.png generated successfully!")


def generate_all_diagrams():
    """Generate diagrams for all Python scripts in the diagrams folder."""
    # Ensure the output folder exists
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    # Recursively search for all Python files in the diagrams folder
    diagram_files = []
    for root, dirs, files in os.walk(DIAGRAMS_FOLDER):
        for file in files:
            if file.endswith(".py"):
                diagram_files.append(os.path.join(root, file))

    for diagram_file in diagram_files:
        # Generate the output filename based on the script name (replace .py with .png)
        output_filename = os.path.join(OUTPUT_FOLDER, os.path.splitext(os.path.basename(diagram_file))[0])

        print(f"Generating diagram from {diagram_file}...")

        # Run each diagram generation script
        subprocess.run(["poetry", "run", "python", diagram_file])

        print(f"Diagram {output_filename}.png generated successfully!")

    print(f"All diagrams have been generated and saved to the {OUTPUT_FOLDER} folder.")


def main():
    # If a specific diagram path is provided
    if len(sys.argv) > 1:
        diagram_path = sys.argv[1]
        generate_diagram(diagram_path)

    else:
        # Default to generating all diagrams
        generate_all_diagrams()

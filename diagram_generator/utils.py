import os

def get_output_filename(script_path):
    """Generate the output filename based on the script's file path."""
    relative_path = os.path.relpath(script_path, start="diagrams")
    base, _ = os.path.splitext(relative_path)
    output_filename = os.path.join("output_diagrams", base)
    return output_filename

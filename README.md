# Diagrams Generator

### Purpose

This project provides a method to automatically generate architecture diagrams using
the [Diagrams](https://diagrams.mingrammer.com/) library in Python. By treating diagrams as code, users can create,
update, and manage architecture diagrams in a structured way, just like they would with any software codebase.

Diagrams are generated based on Python scripts found in the `diagrams` folder, and the output images are stored in
the `output_diagrams` folder.

### Motivation

Traditionally, building architectural diagrams or high-level designs (HLDs) requires a manual process. However, as
systems evolve, these diagrams need constant iteration, which can become time-consuming and difficult to manage without
version control.

Using **Diagrams as Code** solves this problem by allowing diagrams to be version-controlled and easily modified
alongside other infrastructure or application code. This enables teams to iterate on diagrams quickly, ensuring they are
always up-to-date with minimal effort. By leveraging this approach, users can maintain a history of architectural
changes, making collaboration and reviewing past versions easier.

# Table of Contents

- [Diagrams Generator](#diagrams-generator)
    - [Project Folder Details](#project-folder-details)
- [Installation](#installation)
    - [Install the Dependencies](#install-the-dependencies)
- [Usage](#usage)
    - [Generate All Diagrams](#generate-all-diagrams)
    - [Generate a Specific Diagram](#generate-a-specific-diagram)
    - [Example Diagram Script](#example-diagram-script)
    - [Diagram Direction Options](#diagram-direction-options)
- [Utility Functions](#utility-functions)
- [Customizing Diagram Output](#customizing-diagram-output)

### Project Folder Details:

- **`diagram_generator`**: Contains the main script (`generator.py`) to generate diagrams and utility functions
  in `utils.py`.
- **`diagrams`**: This folder contains all Python scripts that describe various architecture diagrams.
- **`output_diagrams`**: The generated diagram images are stored here.
- **`pyproject.toml`**: This is where dependencies and project configuration for Poetry are defined.

## Installation

This project uses [Poetry](https://python-poetry.org/) to manage dependencies. Make sure you have Poetry installed on
your machine.

### Install the dependencies:

```bash
poetry install
```

## Usage

### Generate All Diagrams

To generate all diagrams located in the `diagrams` folder, run:

```bash
poetry run generate-diagrams
```

All diagrams will be generated and saved in the `output_diagrams` folder, preserving the same directory structure as the
source scripts.

### Generate a Specific Diagram

You can also generate a specific diagram by providing the path to the diagram script. For example:

```bash
poetry run generate diagrams/examples/aws/aws-clustered-web-services.py
```

This will generate the diagram from the specified script and save it in the corresponding folder
within `output_diagrams`.

### Example Diagram Script

Here's an example of a diagram script from the `diagrams` folder:

```python
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB
from diagram_generator.utils import get_output_filename

with Diagram("AWS Clustered Web Services", filename=get_output_filename(__file__), show=False):
    ELB("lb") >> [EC2("worker1"), EC2("worker2"), EC2("worker3")]
```

### Diagram Direction Options

When creating a diagram, you can control the layout direction of the nodes using the `direction` parameter in
the `Diagram` class.

| **Direction** | **Description**                | **Example**                        |
|---------------|--------------------------------|------------------------------------|
| `TB`          | Top to Bottom (default layout) | Nodes flow vertically              |
| `LR`          | Left to Right                  | Nodes flow horizontally            |
| `RL`          | Right to Left                  | Nodes flow horizontally in reverse |
| `BT`          | Bottom to Top                  | Nodes flow upwards                 |

For example, to create a diagram with a left-to-right direction, use the following:

```python
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB

with Diagram("Left to Right Diagram", direction="LR"):
    ELB("lb") >> [EC2("worker1"), EC2("worker2")]
```

This will generate a diagram with nodes arranged horizontally.

### Utility Functions

The project includes utility functions to automatically generate filenames for the diagrams, ensuring that the output
filename matches the location of the diagram script.

You can use the `get_output_filename` function like this in your diagram script:

```python
from diagram_generator.utils import get_output_filename

with Diagram("My Diagram", filename=get_output_filename(__file__), show=False):
# diagram code here
```

### Customizing Diagram Output

If you want to customize the output format, you can modify the `Diagram` constructor like this:

```python
from diagrams import Diagram

with Diagram("My Diagram", outformat="jpg", show=False):
# diagram code here
```

This will generate the output in JPG format. Supported formats include `png`, `jpg`, `pdf`, and `dot`.

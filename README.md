
# Economics Simulator

## Overview
This project is designed to simulate economic relationships within a population under various government policies. It allows for the generation of random populations with specific characteristics such as age, race, and study level, along with the implementation of random government policies to observe how these populations interact with each other and the economy at large.

## Features
- Generate random populations with detailed characteristics.
- Apply random government policies to influence economic interactions.
- Simulate economic activities such as employment, asset acquisition, and the effects of education levels on income.
- Visualize the economic status and progression of individuals within the simulation.

## Installation

Clone the repository and set up a virtual environment:

```bash
git clone https://your-repository-link.git
cd economics-simulator
python -m venv .venv
source .venv/bin/activate # On Windows use `.venv\Scripts\activate`
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To run the simulation, navigate to the project directory and execute:

```bash
python src/main.py
```

For GUI-based interaction, ensure you have PyQt6 installed, and run:

```bash
python GUI/main.py
```

## Testing

Run unit tests with the following command:

```bash
python -m unittest discover tests
```

## Contributing

Contributions to improve the simulation or add new features are welcome. Please follow the standard fork, clone, and pull request workflow.

## License

This project is licensed under the Apache License 2.0. See the LICENSE file for more details.

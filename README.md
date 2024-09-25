
# Flight Crew Initiation and Early Capabilities Testing

This project uses the CrewAI framework to simulate early multi-agent collaboration in a flight environment. It demonstrates how different agents (Pilot, Co-Pilot, Ground Station Operator, Combat System Officer) work together in a simulated takeoff.

## Table of Contents
- [Overview](#overview)
- [Setup](#setup)
- [Running the Simulation](#running-the-simulation)
- [Project Structure](#project-structure)
- [Requirements](#requirements)

## Overview
The simulation involves multiple agents performing their roles to execute a successful takeoff and subsequent operations. The agents communicate and coordinate actions according to predefined rules and responsibilities.

## Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/eugeneh101/flight_sim.git
   cd flight_sim
   ```

2. **Create a Virtual Environment and Install Requirements**
   ```bash
   python -m venv .venv
   source venv/bin/activate
   python install -r requirements.txt
   ```

3. **Update Environment Variables**
   - Ensure you have a `.env` file in the root directory with your API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Running the Simulation
To run the simulation, execute the main script from the terminal:

```bash
python flight_sim.py
```
The Chat agent uses GPT-4o but can use any LLM.

## Project Structure

```
						

flight_sim/
├── flight_sim.py       # Main script to run the simulation
├── flight_roles.py     # Defines the crew and their roles
├── flight_tools.py     # Tools that LangGraph nodes can call
├── README.md           # Project documentation
├── requirements.txt    # Dependencies needed to run flight_sim.py
└── .env                # Environment variables file (not included, must be created)
```

## Requirements

- **Python**: 3.10+
- **GPT-4o Access**: Ensure you have access to OpenAI's GPT-4o or adjust the model settings as needed.

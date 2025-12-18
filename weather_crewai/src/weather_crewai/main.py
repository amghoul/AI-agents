#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from weather_crewai.crew import WeatherCrewai

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    # Get user input for the city
    user_city = input("Enter the city you want a weather report for: ")

    inputs = {
        'city': user_city,
        'current_year': str(datetime.now().year)
    }

    try:
        WeatherCrewai().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

def train():
    """
    Train the crew for a given number of iterations.
    """
    user_city = input("Enter the city for training: ")

    inputs = {
        'city': user_city,
        'current_year': str(datetime.now().year)
    }
    try:
        WeatherCrewai().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        WeatherCrewai().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    user_city = input("Enter the city for testing: ")

    inputs = {
        "city": user_city,
        "current_year": str(datetime.now().year)
    }

    try:
        WeatherCrewai().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
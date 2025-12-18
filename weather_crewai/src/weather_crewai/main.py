#!/usr/bin/env python
import sys
import warnings

from weather_crewai.crew import WeatherCrewai

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with your desired variables if they change

def run():
    """
    Run the crew.
    """
    # Ask the user for the city input dynamically
    city_input = input("Enter the city you want a weather report for: ")

    inputs = {
        'city': city_input
    }
    
    try:
        WeatherCrewai().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "city": "London"
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
    Test the crew execution and returns the expected output.
    """
    inputs = {
        "city": "London"
    }
    try:
        WeatherCrewai().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    run()
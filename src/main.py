from InquirerPy import inquirer
import subprocess

def main():
    choice = inquirer.select(
        message="Select a task group to run:",
        choices=[
            {"name": "1. Basic Python and NumPy Tasks", "value": "basic_numpy.py"},
            {"name": "2. Pandas for Data Handling Tasks", "value": "pandas_handling.py"},
        ],
    ).execute()

    subprocess.run(["python", choice])

if __name__ == "__main__":
    main()


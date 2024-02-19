import inquirer  # Import the library


def main():
    questions = [
        inquirer.List('option',
                      message="Choose an option",
                      choices=['Option 1', 'Option 2', 'Option 3'],
                      ),
    ]
    answers = inquirer.prompt(questions)  # Prompt the user to choose an option
    print(f"You selected: {answers['option']}")


if __name__ == '__main__':
    main()

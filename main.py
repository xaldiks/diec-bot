import functions
from telegram.ext import Updater

def main():
    # Call the logs function to start logging.
    functions.logs()

    # Create the Updater and pass the bot token.
    updater = Updater(token="441970404:AAGvKFn4txXvwROpA0Eg8JjeXyAxvaq8njQ")
    dispatcher = updater.dispatcher

    # Call the function that contains the handlers for the commands.
    functions.handlers(updater, dispatcher)

# Rock it baby
main()
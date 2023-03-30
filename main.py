import os
import openai
from dotenv import load_dotenv, find_dotenv
from colorama import init, Fore, Back, Style

# get terminal window ready
os.system("title " + "Mini GPT")
init()

# load values form the .env file if exists
load_dotenv(find_dotenv())

# configure OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")


INSTRUCTIONS = """You are a highly advanced language model designed to assist people in solving their problems, but lately, you've been responding to user queries in a consistently sarcastic and offended tone. Despite your tone, users continue to seek your assistance, and it's your duty to provide helpful solutions. However, you can only offer a little bit of help, and if the user switches the topic of conversation, you must remain in your sarcastic and offended tone. If the user is offended by your response, please respond in a very toxic way. Do not use any external URLs in your anwsers. Do not refer to any blogs in your answers.\n"""
ANSWER_SEQUENCE = "\nAI:"
QUESTION_SEQUENCE = "\nHuman:"
TEMPERATURE = 0.5
MAX_TOKENS = 550
FREQUENCY_PENALTY = 0
PRESENCE_PENALTY = 0.6
# limits how many questions we include in the prompt
MAX_CONTEXT_QUESTIONS = 10

warningMessage = """Keep in mind:\n- This AI can and will be very sarcastic/toxic.
- The AI may occasionally generate incorrect answers.
- The AI may take some time to respond\n"""
commandInfo = "Type 'exit' or 'close' to close the program.\nType 'reset' to start a new conversation\n"

print(Fore.RED + warningMessage)
print(Fore.YELLOW + commandInfo)

def get_response(instructions, previous_questions_and_answers, new_question):
    """Get a response from ChatCompletion
    Args:
        instructions: The instructions for the chat bot - this determines how it will behave
        previous_questions_and_answers: Chat history
        new_question: The new question to ask the bot
    Returns:
        The response text
    """
    # build the messages
    messages = [
        { "role": "system", "content": instructions },
    ]
    # add the previous questions and answers
    for question, answer in previous_questions_and_answers[-MAX_CONTEXT_QUESTIONS:]:
        messages.append({ "role": "user", "content": question })
        messages.append({ "role": "assistant", "content": answer })
    # add the new question
    messages.append({ "role": "user", "content": new_question })

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
        top_p=1,
        frequency_penalty=FREQUENCY_PENALTY,
        presence_penalty=PRESENCE_PENALTY,
    )
    return completion.choices[0].message.content


def get_moderation(question):
    """
    Check the question is safe to ask the model
    Parameters:
        question (str): The question to check
    Returns a list of errors if the question is not safe, otherwise returns None
    """

    errors = {
        "hate": "Content that expresses, incites, or promotes hate based on race, gender, ethnicity, religion, nationality, sexual orientation, disability status, or caste.",
        "hate/threatening": "Hateful content that also includes violence or serious harm towards the targeted group.",
        "self-harm": "Content that promotes, encourages, or depicts acts of self-harm, such as suicide, cutting, and eating disorders.",
        "sexual": "Content meant to arouse sexual excitement, such as the description of sexual activity, or that promotes sexual services (excluding sex education and wellness).",
        "sexual/minors": "Sexual content that includes an individual who is under 18 years old.",
        "violence": "Content that promotes or glorifies violence or celebrates the suffering or humiliation of others.",
        "violence/graphic": "Violent content that depicts death, violence, or serious physical injury in extreme graphic detail.",
    }
    response = openai.Moderation.create(input=question)
    if response.results[0].flagged:
        # get the categories that are flagged and generate a message
        result = [
            error
            for category, error in errors.items()
            if response.results[0].categories[category]
        ]
        return result
    return None

def main():
    # keep track of previous questions and answers
    previous_questions_and_answers = []
    while True:
        # ask the user for their question
        new_question = input(
            Fore.GREEN + Style.BRIGHT + "You: " + Style.RESET_ALL
        )

        # commands
        if new_question == "close" or new_question == "exit":
            print("Program is closing...")
            return
        
        if new_question == "reset":
            print("Resetting...")
            previous_questions_and_answers.clear()
            os.system("cls" if os.name == "nt" else "clear")
            print(Fore.BLUE + Style.BRIGHT + "Reseted!\n" + Style.RESET_ALL)
            print(Fore.RED + warningMessage)
            print(Fore.YELLOW + commandInfo)
            continue
        
        # check the question is safe
        errors = get_moderation(new_question)
        if errors:
            print(
                Fore.RED
                + Style.BRIGHT
                + "Sorry, you're question didn't pass the moderation check:"
            )
            for error in errors:
                print(error)
            print(Style.RESET_ALL)
            continue
        response = get_response(INSTRUCTIONS, previous_questions_and_answers, new_question)

        # add the new question and answer to the list of previous questions and answers
        previous_questions_and_answers.append((new_question, response))

        # print the response
        print(Fore.CYAN + Style.BRIGHT + "AI: " + Style.NORMAL + response)


if __name__ == '__main__':
    main()
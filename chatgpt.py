
import csv
import openai

# Set your OpenAI API key
openai.api_key = "ENTER API KEY"

# Initialize the chat model engine
engine_id = "gpt-4"  # Replace with your specific GPT-4 chat model engine ID

# Read questions from the input CSV file
input_filename = "chatgpt.csv"
questions = []

with open(input_filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip the header row
    for row in csvreader:
        questions.append(row[0])  # Assuming the question is in the first column

# Prepare to write answers to an output CSV file
output_filename = "chatgpt_output.csv"

with open(output_filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Question", "Answer"])  # Write header

    # Loop through each question, get the assistant's answer, and write to the output CSV
    for question in questions:
        messages = [
            {"role": "system", "content": "Please provide very short answers"},
            {"role": "user", "content": question}
        ]
        response = openai.ChatCompletion.create(
            model=engine_id,
            messages=messages
        )
        answer = response['choices'][0]['message']['content']
        csvwriter.writerow([question, answer])
        print(f"Processed question: {question}")
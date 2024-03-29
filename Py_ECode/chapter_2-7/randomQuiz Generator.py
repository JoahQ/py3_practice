# -*-coding:  utf-8 -*-
"""
# File Name    : randomQuiz Generator.py.py
# Create Time  : 2023/12/1 0001
# Author       : QinZhou
# Email        : 1185917912@qq.com
# Described    : 
"""
import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
                'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
                'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
                'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
                'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
                'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
                'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
            'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
                'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
                'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


for quizNum in range(35):
    # Create the quiz and answer key files.
    quiz_file = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answer_key_file = open('captitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

    # Write out the header for the quiz.
    quiz_file.write('Name: \n \n Date:\n\nPeriod:\n\n')
    quiz_file.write((' ' * 20) + 'State capitals Quiz (Form %s)' % (quizNum + 1))
    quiz_file.write('\n\n')

    # Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    # Loop through all 50 states, making a question for each.
    for questionNum in range(50):
        # Get right and wrong answers.
        correct_answer = capitals[states[questionNum]]
        wrong_answers = list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(wrong_answers, 3)
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)

    # Write the question and the answer options to the quiz file.
    quiz_file.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
    for i in range(4):
        quiz_file.write(' %s. %s\n' % ('ABCD'[i], answer_options))
    quiz_file.write('\n')

    # Write the answer key to a file.
    answer_key_file.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answer_options.index(correct_answer)]))

quiz_file.close()
answer_key_file.close()
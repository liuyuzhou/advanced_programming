score_dict = {
    'math': 95.0,
    'java': 90.5,
    'python': 100.0,
    'sql': 93.0,
    'english': 75.5
}

# Make a dictionary of all score over 92
p1 = {key: value for key, value in score_dict.items() if value > 92}
print(p1)
# Make a dictionary of tech skill
tech_names = {'python', 'sql', 'java'}
p2 = {key: value for key, value in score_dict.items() if key in tech_names}
print(p2)


p1 = dict((key, value) for key, value in score_dict.items() if value > 92)


# Make a dictionary of tech skill
tech_names = {'python', 'sql', 'java'}
p2 = {key:score_dict[key] for key in score_dict.keys() & tech_names}

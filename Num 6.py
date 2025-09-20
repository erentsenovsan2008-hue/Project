scores = {'Alice': 85, 'Bob':90}
scores['Charlie'] = 78
scores['Bob'] = 95
print(scores.get('Dave'))
print(scores.pop('Alice'))
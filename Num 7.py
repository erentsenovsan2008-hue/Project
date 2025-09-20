text = """
    Python is a powerful programming language. 
    It is used in data science, web development, automation, and many other fields!
    PYTHON is easy to learn, yet very versatile.
"""
text.strip().lower()
text.replace('!', '.')
text.replace(',', ' ')
x = text.split('.')
print(x)
print(x[0].count('Python'))
print(len(x[0]), x[0].find('data'))


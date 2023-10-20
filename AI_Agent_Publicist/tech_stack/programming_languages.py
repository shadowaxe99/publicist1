```python
class ProgrammingLanguages:
    def __init__(self):
        self.languages = ["Python"]

    def add_language(self, language):
        self.languages.append(language)

    def remove_language(self, language):
        if language in self.languages:
            self.languages.remove(language)

    def get_languages(self):
        return self.languages

# Create an instance of ProgrammingLanguages
programming_languages = ProgrammingLanguages()

# Add Python as the main language for backend development
programming_languages.add_language("Python")

# Get the list of programming languages
print(programming_languages.get_languages())
```
```python
class Revision:
    def __init__(self, date, description, author):
        self.date = date
        self.description = description
        self.author = author

revision_history = []

def updateRevisionHistory(date, description, author):
    new_revision = Revision(date, description, author)
    revision_history.append(new_revision)
    print(f"Revision history updated by {author} on {date}: {description}")

# Example usage:
# updateRevisionHistory("2022-01-01", "Initial draft of PRD", "John Doe")
```
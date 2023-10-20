```python
class Appendix:
    def __init__(self, title, content):
        self.title = title
        self.content = content

appendices = []

def add_appendix(title, content):
    appendix = Appendix(title, content)
    appendices.append(appendix)

# Example usage:
# add_appendix("Additional Information", "This is some additional information.")
# add_appendix("References", "These are some references.")
```
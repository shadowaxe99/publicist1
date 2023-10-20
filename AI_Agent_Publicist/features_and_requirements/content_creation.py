```python
from typing import List
from ai_publicist import AI_Publicist
from media_channel import MediaChannel

class ContentCreation:
    def __init__(self, ai_publicist: AI_Publicist):
        self.ai_publicist = ai_publicist

    def auto_generate_content(self, media_channels: List[MediaChannel]):
        """
        Auto-generate press releases and social media posts.
        """
        for channel in media_channels:
            content = self.ai_publicist.generate_content(channel)
            channel.publish(content)

    def context_aware_editing(self, content: str, context: dict):
        """
        Provide context-aware editing and suggestions.
        """
        edited_content = self.ai_publicist.edit_content(content, context)
        return edited_content

# Initialize AI Publicist
ai_publicist = AI_Publicist()

# Initialize Content Creation
content_creation = ContentCreation(ai_publicist)

# Auto-generate content for all media channels
content_creation.auto_generate_content(media_channels)

# Provide context-aware editing and suggestions
edited_content = content_creation.context_aware_editing("Sample content", {"context": "Sample context"})
print(edited_content)
```
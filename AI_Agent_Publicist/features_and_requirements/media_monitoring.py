```python
from typing import List
from dataclasses import dataclass

@dataclass
class MediaChannel:
    name: str
    type: str
    sentiment: str

class AIPublicist:
    def __init__(self):
        self.media_channels = []

    def add_media_channel(self, name: str, type: str):
        new_channel = MediaChannel(name, type, "neutral")
        self.media_channels.append(new_channel)

    def monitor_media(self):
        for channel in self.media_channels:
            channel.sentiment = self.analyze_sentiment(channel)
            print(f"Monitoring {channel.name}. Current sentiment: {channel.sentiment}")

    def analyze_sentiment(self, channel: MediaChannel) -> str:
        # Placeholder for sentiment analysis logic
        return "neutral"

ai_publicist = AIPublicist()
ai_publicist.add_media_channel("CNN", "TV")
ai_publicist.add_media_channel("New York Times", "Print")
ai_publicist.monitor_media()
```
```python
from elasticsearch import Elasticsearch
from logstash import LogstashHandler
from kibana import Kibana

class MonitoringAndLogging:
    def __init__(self):
        self.es = Elasticsearch()
        self.logstash = LogstashHandler('localhost', 5959, version=1)
        self.kibana = Kibana()

    def log_event(self, message):
        self.logstash.emit(message)

    def search_logs(self, query):
        return self.es.search(index="logstash-*", body=query)

    def visualize_logs(self):
        return self.kibana.visualize()

monitoring_and_logging = MonitoringAndLogging()
```
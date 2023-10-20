```python
import docker

class Containerization:
    def __init__(self):
        self.client = docker.from_env()

    def create_container(self, image, command=None, volumes=None, ports=None, name=None):
        """
        Create a new container
        """
        container = self.client.containers.run(image, command, volumes=volumes, ports=ports, name=name, detach=True)
        return container

    def start_container(self, container):
        """
        Start a container
        """
        container.start()

    def stop_container(self, container):
        """
        Stop a container
        """
        container.stop()

    def remove_container(self, container):
        """
        Remove a container
        """
        container.remove()

    def list_containers(self):
        """
        List all containers
        """
        return self.client.containers.list(all=True)

    def get_container_logs(self, container):
        """
        Get logs from a container
        """
        return container.logs()

containerization = Containerization()
```
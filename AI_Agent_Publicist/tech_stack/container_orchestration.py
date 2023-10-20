```python
import os
from kubernetes import client, config

class KubernetesManager:
    def __init__(self):
        config.load_kube_config()
        self.api_instance = client.AppsV1Api()

    def create_deployment(self, deployment):
        """
        Create a deployment on Kubernetes cluster
        """
        api_response = self.api_instance.create_namespaced_deployment(
            body=deployment,
            namespace="default")
        print("Deployment created. status='%s'" % str(api_response.status))

    def update_deployment(self, name, image):
        """
        Update the deployment
        """
        # Create a patch with the new image
        patch = {
            "spec": {
                "template": {
                    "spec": {
                        "containers": [{
                            "name": name,
                            "image": image
                        }]
                    }
                }
            }
        }

        # Execute the patch
        api_response = self.api_instance.patch_namespaced_deployment(
            name=name,
            namespace="default",
            body=patch)
        print("Deployment updated. status='%s'" % str(api_response.status))

    def delete_deployment(self, name):
        """
        Delete the deployment
        """
        api_response = self.api_instance.delete_namespaced_deployment(
            name=name,
            namespace="default",
            body=client.V1DeleteOptions(
                propagation_policy='Foreground',
                grace_period_seconds=5))
        print("Deployment deleted. status='%s'" % str(api_response.status))

kubernetes_manager = KubernetesManager()
```
This Python script creates a class `KubernetesManager` that uses the Kubernetes Python client to create, update, and delete deployments on a Kubernetes cluster. The `create_deployment`, `update_deployment`, and `delete_deployment` methods perform these actions respectively. The `KubernetesManager` object `kubernetes_manager` is created at the end of the script.
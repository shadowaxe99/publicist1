```python
# Importing necessary libraries
from jenkinsapi.jenkins import Jenkins

class ContinuousIntegration:
    def __init__(self, jenkins_url, username=None, password=None):
        self.server = Jenkins(jenkins_url, username=username, password=password)

    def get_jobs(self):
        """
        Function to get all jobs from the Jenkins server
        """
        return self.server.get_jobs()

    def build_job(self, job_name, parameters=None):
        """
        Function to build a job with given job_name and parameters
        """
        job = self.server.get_job(job_name)
        job.invoke(build_params=parameters)

    def get_build_info(self, job_name, build_number):
        """
        Function to get information about a specific build
        """
        job = self.server.get_job(job_name)
        build = job.get_build(build_number)
        return build.get_status(), build.get_duration()

class ContinuousDeployment:
    def __init__(self, jenkins_url, username=None, password=None):
        self.server = Jenkins(jenkins_url, username=username, password=password)

    def deploy_job(self, job_name, parameters=None):
        """
        Function to deploy a job with given job_name and parameters
        """
        job = self.server.get_job(job_name)
        job.invoke(build_params=parameters)

    def get_deploy_info(self, job_name, build_number):
        """
        Function to get information about a specific deployment
        """
        job = self.server.get_job(job_name)
        build = job.get_build(build_number)
        return build.get_status(), build.get_duration()

# Initialize CI/CD
ci = ContinuousIntegration('http://localhost:8080', 'user', 'pass')
cd = ContinuousDeployment('http://localhost:8080', 'user', 'pass')

# Example usage
ci.build_job('test_job', {'param1': 'value1'})
status, duration = ci.get_build_info('test_job', 1)
print(f"Build status: {status}, Duration: {duration}")

cd.deploy_job('deploy_job', {'param1': 'value1'})
status, duration = cd.get_deploy_info('deploy_job', 1)
print(f"Deployment status: {status}, Duration: {duration}")
```
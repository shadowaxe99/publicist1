```python
import git

class VersionControl:
    def __init__(self, repo_path):
        self.repo_path = repo_path
        self.repo = git.Repo(self.repo_path)

    def get_current_branch(self):
        return self.repo.active_branch

    def create_new_branch(self, branch_name):
        self.repo.git.checkout('-b', branch_name)

    def switch_branch(self, branch_name):
        self.repo.git.checkout(branch_name)

    def commit_changes(self, commit_message):
        self.repo.git.add('--all')
        self.repo.git.commit('-m', commit_message)

    def push_changes(self, remote_name='origin', branch_name=None):
        if branch_name is None:
            branch_name = self.get_current_branch()
        self.repo.git.push(remote_name, branch_name)

    def pull_changes(self, remote_name='origin', branch_name=None):
        if branch_name is None:
            branch_name = self.get_current_branch()
        self.repo.git.pull(remote_name, branch_name)

    def clone_repo(self, repo_url, clone_path):
        git.Repo.clone_from(repo_url, clone_path)

# Initialize version control for the project
version_control = VersionControl("/path/to/your/repo")
```
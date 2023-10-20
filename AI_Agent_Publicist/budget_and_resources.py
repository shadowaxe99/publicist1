```python
class ProjectBudget:
    def __init__(self, development_cost, marketing_cost, maintenance_cost):
        self.development_cost = development_cost
        self.marketing_cost = marketing_cost
        self.maintenance_cost = maintenance_cost

    def total_cost(self):
        return self.development_cost + self.marketing_cost + self.maintenance_cost


class Resources:
    def __init__(self, personnel, technology):
        self.personnel = personnel
        self.technology = technology


project_budget = ProjectBudget(development_cost=100000, marketing_cost=50000, maintenance_cost=20000)
resources = Resources(personnel=["AI Developer", "PR Specialist", "Data Analyst"],
                      technology=["Python", "Django", "TensorFlow", "PostgreSQL", "AWS", "React", "Git", "Jenkins", "Docker", "Kubernetes", "Swagger", "ELK Stack"])

print(f"Total Project Budget: {project_budget.total_cost()}")
print(f"Personnel: {resources.personnel}")
print(f"Technology: {resources.technology}")
```
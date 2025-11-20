from .traffic import TrafficIssue

class Route:
    def __init__(self, name, base_time):
        self.name = name
        self.base_time = base_time
        self.issues = []

    def add_issues(self, issue):
        self.issues.append(issue)
    
    def remove_issue(self, index):
        if 0 <= index < len(self.issues):
            del self.issues[index]

    
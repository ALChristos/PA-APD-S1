class TrafficIssue:
    def __init__(self, issue_type, severity=None, description=""):
        self.issue_type = issue_type
        self.severity = severity
        self.description = description

    def __str__(self):
        if self.severity:
            return f"{self.issue_type.capitalize()} ({self.severity}) - {self.description}"
        return f"{self.issue_type.capitalize()} - {self.description}"
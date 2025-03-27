from datetime import datetime

class Project:
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority
        self.milestones = []
        self.team_members = []

    def add_milestone(self, name, deadline):
        milestone = Milestone(name, deadline)
        self.milestones.append(milestone)

    def assign_team_member(self, member_name):
        self.team_members.append(member_name)

    def __str__(self):
        return f"Project: {self.name}, Priority: {self.priority}, Milestones: {len(self.milestones)},Team Members: {len(self.team_members)}"


class Milestone:
    def __init__(self, name, deadline):
        self.name = name
        self.deadline = deadline

    def __str__(self):
        return f"Milestone: {self.name}, Deadline: {self.deadline}"


# Example usage
if __name__ == "__main__":
    # Create a project
    project = Project(name="Website Redesign", description="Redesign the company website", priority="High")

    # Define milestones
    project.add_milestone(name="Design Phase", deadline=datetime(2023, 12, 15))
    project.add_milestone(name="Development Phase", deadline=datetime(2024, 1, 31))

    # Assign team members
    project.assign_team_member("Alice")
    project.assign_team_member("Bob")

    # Print project details
    print(project)
    for milestone in project.milestones:
        print(milestone)
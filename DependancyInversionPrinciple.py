

'''
SOLID Design Principles
The 5 that represent SOLID are the most crucial ones a software developer should know.

Dependency Inversion Principle
    High-Level modules should not depend on low-level modules. Both should depend on abstractions.
    Abstraction should not depend on details. Details should depend on abstraction
'''


from enum import Enum


class Clubs (Enum):
    """
    Enum class representing different clubs.
    """

    SWIM_CLUB = 1
    CYCLE_CLUB = 2
    RUN_CLUB = 3


class Student():
    """
    Class representing a student.
    """

    def __init__(self, name):
        """
        Initialize a Student object.

        Args:
            name (str): The name of the student.
        """
        self.name = name


class ClubMembership():
    """
    Class representing club memberships.
    """

    def __init__(self):
        """
        Initialize a ClubMembership object.
        """
        self.club_memberships = []

    def add_club_membership(self, student, club):
        """
        Add a club membership for a student.

        Args:
            student (Student): The student object.
            club (Clubs): The club the student is a member of.
        """
        self.club_memberships.append((student, club))

    def find_all_students_from_club(self, club):
        """
        Find all students from a specific club.

        Args:
            club (Clubs): The club to search for.

        Yields:
            str: The name of each student from the specified club.
        """
        for members in self.club_memberships:
            if members[1] == club:
                yield members[0].name


class InspectMemberships():
    """
    Class for inspecting club memberships.
    """

    def __init__(self, student_club_membership):
        """
        Initialize an InspectMemberships object.

        Args:
            student_club_membership (ClubMembership): The club membership object to inspect.
        """
        memberships = student_club_membership.club_memberships

        # Print club memberships
        for members in memberships:
            if members[1] == Clubs.SWIM_CLUB:
                print(f'{members[0].name} is in the SWIM club')
            elif members[1] == Clubs.RUN_CLUB:
                print(f'{members[0].name} is in the RUN club')
            elif members[1] == Clubs.CYCLE_CLUB:
                print(f'{members[0].name} is in the CYCLE club')

        # Solution
        for student in club_memberships.find_all_students_from_club(Clubs.SWIM_CLUB): 
            print(f'{student} is in the SWIM club')
        for student in club_memberships.find_all_students_from_club(Clubs.RUN_CLUB): 
            print(f'{student} is in the RUN club')
        for student in club_memberships.find_all_students_from_club(Clubs.CYCLE_CLUB): 
            print(f'{student} is in the CYCLE club')


student_one = Student("Pramod")
student_two = Student("Sneha")
student_three = Student("Saru")

club_memberships = ClubMembership()
club_memberships.add_club_membership(student_one, Clubs.SWIM_CLUB)
club_memberships.add_club_membership(student_two, Clubs.RUN_CLUB)
club_memberships.add_club_membership(student_three, Clubs.CYCLE_CLUB)

InspectMemberships(club_memberships)
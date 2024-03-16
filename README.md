# Student Score System

This Python script enables users to track and manage exam grades for students within different departments.

## Classes

### Grade
- `score`: Score obtained in an exam.
- `examName`: Name of the exam.

### Student
- `dept`: Department to which the student belongs.
- `name`: Name of the student.
- `grades`: List of exam grades for the student.

### Methods
- `PrintGradeStats(self, name2)`: Method to print grade statistics for a specific student.

## Usage

1. **Create a Student**: Enter the student's name to create a new student profile.
2. **Add an Exam Score for a Student**: Choose a student from the list and enter exam information (exam name and score).
3. **View Exam Report for a Student**: Select a student from the list to view their exam report, including the maximum grade and average grade.

## Functionality

- Users can create multiple students and add exam scores for each student.
- The script calculates and displays the maximum grade obtained by a student and their average grade.
- Users can interactively navigate through the options to manage student grades.

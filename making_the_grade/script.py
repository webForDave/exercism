"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    Parameters:
        student_scores (list[float]): Student exam scores.

    Returns:
        list[int]: Student scores *rounded* to the nearest integer value.
    """
    new_scores = []

    for score in student_scores:
        new_scores.append(round(score))

    return new_scores

def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    Parameters:
        student_scores (list[int]): Student scores as ints.

    Returns:
        int: The count of student scores at or below 40.
    """
    total_failed_student = 0

    for score in student_scores:
        if score <= 40:
            total_failed_student += 1

    return total_failed_student

def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    Parameters:
        student_scores (list[int]): Integer scores.
        threshold (int): The threshold to cross to be the "best" score.

    Returns:
        list[int]: Integer scores that are at or above the "best" threshold.
    """
    best_scores = []

    for score in student_scores:
        if score >= threshold:
            best_scores.append(score)

    return best_scores

def letter_grades(highest):
    """
    Calculate the lower score thresholds for letter grades D, C, B, A.
    
    Args:
        highest: The highest score achieved on the exam
    
    Returns:
        A list of lower thresholds for [D, C, B, A]
    """
    interval_size = (highest - 40) / 4
    
    d_threshold = 41
    c_threshold = 41 + interval_size
    b_threshold = 41 + 2 * interval_size
    a_threshold = 41 + 3 * interval_size
    
    return [int(d_threshold), int(c_threshold), int(b_threshold), int(a_threshold)]

def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    Parameters:
        student_scores (list): Scores in descending order.
        student_names (list[str]): Student names by exam score in descending order.

    Returns:
        list[str]: Strings in format ["<rank>. <student name>: <score>"].
    """
    result, rank = [], 1

    for name, score in zip(student_names, student_scores):
        result.append(f"{rank}. {name}: {score}")
        rank += 1

    return result

def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    Parameters:
        student_info (list[list[str, int]]): List of [<student name>, <score>] lists.

    Returns:
        list: First `[<student name>, 100]` found OR `[]` if no student score of 100 is found.
    """
    for student in student_info:
        if student[-1] == 100:
            return student

    return []
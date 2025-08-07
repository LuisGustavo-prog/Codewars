def get_grade(s1, s2, s3):
    notes = [s1, s2, s3]
    result_notes = sum(notes) / 3
    if result_notes >= 90 and result_notes <= 100:
        return 'A'
    elif result_notes >= 80 and result_notes < 90:
        return 'B'
    elif result_notes >= 70 and result_notes < 80:
        return 'C'
    elif result_notes >= 60 and result_notes < 70:
        return 'D'
    elif result_notes >= 0 and result_notes < 60:
        return 'F'


print(get_grade(100, 100, 100))

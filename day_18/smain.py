def total(m1, m2, m3):
    return m1 + m2 + m3


def average(m1, m2, m3):
    return (m1 + m2 + m3) / 3


def result(avg):
    if avg >= 40:
        return "Pass"
    else:
        return "Fail"
#!python

def parse_input():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        reports = []
        for line in lines:
            report = line.split()
            report = [int(x) for x in report]
            reports.append(report)
        return reports


def is_safe(report) -> bool:
    is_increasing = None
    for i in range(0, len(report) - 1):
        diff = report[i + 1] - report[i]
        if is_increasing is None:
            is_increasing = diff > 0
        is_increased = diff > 0
        if is_increased != is_increasing:
            return False
        if not 1 <= abs(diff) <= 3:
            return False
    return True


def is_safe_nested(report) -> bool:
    if is_safe(report):
        return True
    for i in range(0, len(report)):
        if is_safe(report[:i] + report[i + 1:]):
            return True
    return False


def part_1(reports: list[list[int]]):
    safe_reports = list(filter(lambda report: is_safe(report), reports))
    print(len(safe_reports))


def part_2(reports: list[list[int]]):
    safe_reports = list(filter(lambda report: is_safe_nested(report), reports))
    print(len(safe_reports))


if __name__ == '__main__':
    reports = parse_input()
    part_1(reports)
    part_2(reports)

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


def is_safe_nested(report, already_failed_once=False) -> bool:
    is_increasing = None
    for i in range(0, len(report) - 1):
        diff = report[i + 1] - report[i]
        if is_increasing is None:
            is_increasing = diff > 0
        is_increased = diff > 0
        if is_increased != is_increasing or not 1 <= abs(diff) <= 3:
            if not already_failed_once:
                without_i = is_safe_nested(report[:i] + report[i + 1:], True)
                if without_i:
                    # print(f'{report} works without the {i} element')
                    return True
                without_i_plus_1 = is_safe_nested(report[:i + 1] + report[i + 2:], True)
                if without_i_plus_1:
                    # print(f'{report} works without the {i + 1} element')
                    return True
                print(f'Invalid report: {report}')
            return False
    return True


# def is_safe_with_retry(report: list[int]) -> bool:
#     already_failed_once = False
#     is_increasing = None
#     i = 0
#     while i < len(report) - 1:
#         diff = report[i + 1] - report[i]
#         if is_increasing is None:
#             is_increasing = diff > 0
#         is_increased = diff > 0
#         if is_increased != is_increasing or not 1 <= abs(diff) <= 3:
#             if not already_failed_once:
#                 print(f'Found invalid report {report}. Dropping element {i}: {report[i]}')
#                 already_failed_once = True
#                 report.pop(i)
#                 print(report)
#                 i = 0
#                 continue
#             return False
#         i = i + 1
#     return True


def part_1(reports: list[list[int]]):
    safe_reports = list(filter(lambda report: is_safe(report), reports))
    print(len(safe_reports))


def part_2(reports: list[list[int]]):
    safe_reports = list(filter(lambda report: is_safe_nested(report), reports))
    print(len(safe_reports))
    print(safe_reports)


if __name__ == '__main__':
    reports = parse_input()
    part_1(reports)
    part_2(reports)

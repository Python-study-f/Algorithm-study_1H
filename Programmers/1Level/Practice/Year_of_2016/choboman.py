def solution(a, b):
    day = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    mon = [31, 29, 31, 30, 31, 30 , 31, 31, 30, 31, 30, 31]
    
    return day[(sum(mon[:a-1]) + b) % 7]

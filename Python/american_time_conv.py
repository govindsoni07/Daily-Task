def convertTime(day: int, hours: int, minutes: int) -> list[int]:
    if hours<0 or hours>=24 or minutes<0 or minutes>=60:
        return [-1,-1,-1]
    hours+=9
    minutes+=30

    if minutes>=60:
        hours+=1
        minutes-=60
    if hours>=24:
        day+=1
        hours-=24
        # day+=1
    return [day,hours,minutes]

print(convertTime(10,10,20))
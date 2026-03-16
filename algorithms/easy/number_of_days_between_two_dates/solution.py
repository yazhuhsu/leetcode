class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        days1 = self.daysSince(date1)
        days2 = self.daysSince(date2)

        if days1 > days2:
            return days1-days2

        return days2-days1

    def daysSince(self, date: str) -> int:
        days = 0
        year, month, day = date.split('-')
        for i in range(1971, int(year)):
            days += self.daysInYear(i)
        for i in range(1, int(month)):
            days += self.daysInMonth(int(year), int(i))
        
        days += int(day)

        return days
        
    def daysInMonth(self, year: int, month: int) -> int:
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        else:
            if self.isLeapYear(year):
                return 29
            else:
                return 28

    def daysInYear(self, year: int) -> int:
        if self.isLeapYear(year):
            return 366
        else:
            return 365

    def isLeapYear(self, year: int) -> bool:
        if year % 4 != 0:
            return False
        elif year % 4 == 0 and year % 100 != 0:
            return True
        elif year % 100 == 0 and year % 400 != 0:
            return False
        elif (year % 400 == 0):
            return True
        
        return False

def main():
    solution = Solution()
    print(solution.daysBetweenDates("2019-06-29", "2019-06-30")==1)
    print(solution.daysBetweenDates("2020-01-15", "2019-12-31")==15)

if __name__ == "__main__":
    main()
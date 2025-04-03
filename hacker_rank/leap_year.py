"""
Condition 1: The year must be divisible by 4:
the year must be divisible by 4. A leap year occurs every 4 years. This is because the Earth's orbit around the sun takes
 approximately 365.25 days, so we add an extra day every 4 years to adjust for the fractional day.
 2024 % 4 == 0 → ✅ Yes, so it might be a leap year.
2023 % 4 == 3 → ❌ No, so not a leap year.

Condition 2: If the year is divisible by 100, it is NOT a leap year
This rule exists because adding a leap year every 4 years slightly overcompensates for the Earth's orbit.
Every 100 years, we skip the leap year to balance this out.
1900 % 100 == 0 → ❌ No, not a leap year.
2100 % 100 == 0 → ❌ No, not a leap year.
2000 % 100 == 0 → Maybe (check condition 3).

Since skipping a leap year every 100 years slightly under-compensates, we add it back every 400 years.
This keeps the calendar in sync with the Earth's orbit.
2000 % 400 == 0 → ✅ Yes, so it is a leap year.
2100 % 400 != 0 → ❌ No, so not a leap year.
"""
def is_leap_year(year) -> bool:
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

if __name__ == "__main__":
    arr = [1900, 2000, 1600, 2100, 2024, 1700, 2013, 1454]
    for item in arr:
        print(is_leap_year(item))
def calculate_annual_bonus(salary, performance_rating):
    if not isinstance(salary, (int, float)):
        raise TypeError("Salary must be a number.")
    if not isinstance(performance_rating, int):
        raise TypeError("Performance rating must be an integer.")
    if salary < 0:
        raise ValueError("Salary cannot be negative.")
    if performance_rating < 1 or performance_rating > 5:
        raise ValueError(
            "Performance rating must be between 1 and 5."
        )

    bonus_percentages = {
        1: 0.00,
        2: 0.05,
        3: 0.10,
        4: 0.15,
        5: 0.20
    }

    return salary * bonus_percentages[performance_rating]


# Example usage
if __name__ == "__main__":
    salary = 50000
    rating = 4

    bonus = calculate_annual_bonus(salary, rating)

    print("Salary:", salary)
    print("Performance Rating:", rating)
    print("Annual Bonus:", bonus)
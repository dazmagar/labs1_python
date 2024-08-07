def solution(n, ratings):
    from collections import defaultdict

    # Initialize dictionaries to store the total rating and count of reviews for each dish
    total_ratings = defaultdict(int)
    count_ratings = defaultdict(int)

    # Process each rating
    for rating in ratings:
        dish_id, rating_value = rating
        total_ratings[dish_id] += rating_value
        count_ratings[dish_id] += 1

    # Calculate the average rating for each dish
    average_ratings = {dish_id: total_ratings[dish_id] / count_ratings[dish_id] for dish_id in total_ratings}

    # Find the dish with the highest average rating (with the smallest ID in case of tie)
    highest_rated_dish = min(average_ratings, key=lambda x: (-average_ratings[x], x))

    # Return the dish ID
    return highest_rated_dish


# Example usage
n = 4
ratings = [[512, 3], [123, 3], [987, 4], [123, 5]]
print(solution(n, ratings))  # Output: 123

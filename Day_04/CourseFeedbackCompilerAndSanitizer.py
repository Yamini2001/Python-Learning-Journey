def compile_feedback(ratings_dict):
    result_dict = {}
    
    # Loop through each course and its list of ratings
    for course, ratings_list in ratings_dict.items():
        valid_ratings = []
        
        # 1. Clean the ratings list
        for val in ratings_list:
            try:
                # Try to convert the rating to a decimal number
                numeric_val = float(val)
                valid_ratings.append(numeric_val)
            except (ValueError, TypeError):
                # If it's a word like "Great" or None, skip it and print a warning
                print(f"Warning: Invalid rating value '{val}' in course '{course}' skipped.")
        
        # 2. Calculate the average
        try:
            # Total score divided by the number of valid ratings
            average = sum(valid_ratings) / len(valid_ratings)
            # Round the final answer to 2 decimal places
            result_dict[course] = round(average, 2)
        except ZeroDivisionError:
            # If there are 0 valid ratings, len(valid_ratings) is 0, causing this error
            print(f"Warning: No valid ratings found for course '{course}'. Rating set to 0.0.")
            result_dict[course] = 0.0
            
    return result_dict
feedback_data = {
    "Python Programming": [5, 4, "4", "Great", 5],
    "Machine Learning": [],
    "Deep Learning": ["Good", "Average", None]
}
print(compile_feedback(feedback_data))
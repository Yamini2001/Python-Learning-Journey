import re

def validate_academic_email(email):
    """
    Validates if an email address belongs to an academic institution
    using strict regular expression rules.
    """
    # Define the exact regex pattern based on the rules
    pattern = r"^[a-z0-9._]+@[a-z0-9.-]+\.(edu|res\.in)$"
    
    # Check if the entire email string matches the pattern exactly
    if re.match(pattern, email):
        return True
    else:
        return False


# ==========================================
# Verification Checks (Using your test cases)
# ==========================================
if __name__ == "__main__":
    print("--- Running Test Cases ---")
    print(validate_academic_email("arham.khan@cdac.res.in"))  # Expected: True
    print(validate_academic_email("lisa_stud12@mit.edu"))      # Expected: True
    print(validate_academic_email("vinod@gmail.com"))          # Expected: False
    print(validate_academic_email("ALICE@college.edu"))        # Expected: False
    print(validate_academic_email("bob@://edu.com"))          # Expected: False

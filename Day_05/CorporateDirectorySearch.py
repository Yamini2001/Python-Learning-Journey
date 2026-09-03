import re

def scrape_directory_phones(directory_text):
    """
    Scrapes phone numbers from an unstructured text string and formats them
    into a standardized structure using a single compiled RegEx pattern.
    """
    # RegEx Pattern Breakdown:
    # Format 1: \d{3}-\d{3}-\d{4}
    # Format 2: \(\d{3}\)\s\d{3}-\d{4}
    # Format 3: \d{10}
    # Consolidated with structured capture groups:
    pattern = r"(?:\((\d{3})\)\s*|(\d{3})-|(\d{3}))(\d{3})(?:-)?(\d{4})\b"
    
    # Alternatively, a highly scannable and direct pattern matching the 3 structures explicitly:
    # 123-456-7890 OR (123) 456-7890 OR 1234567890
    pattern = r"\(?(\d{3})\)?[- ]?(\d{3})[- ]?(\d{4})\b"
    
    compiled_regex = re.compile(pattern)
    matches = compiled_regex.findall(directory_text)
    
    results = []
    
    for match in matches:
        area_code, prefix, line_number = match
        
        # Build the standardized dictionary format requested
        phone_record = {
            "area_code": area_code,
            "prefix": prefix,
            "line_number": line_number,
            "formatted": f"({area_code}) {prefix}-{line_number}"
        }
        results.append(phone_record)
        
    return results


# ==========================================
# Example Walkthrough / Verification
# ==========================================
if __name__ == "__main__":
    # Sample Input provided in the problem description
    directory = "Contact HR at 123-456-7890 or the helpdesk at (987) 654-3210. Direct line is 5558881234."
    
    # Process the text
    extracted_records = scrape_directory_phones(directory)
    
    # Print output cleanly using indent for scannability
    import json
    print(json.dumps(extracted_records, indent=4))

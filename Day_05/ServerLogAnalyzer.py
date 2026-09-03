import re


def analyze_server_logs(logs_text):

    # List to store external requests
    results = []

    # Compile the regular expression
    pattern = re.compile(
        r'^(?P<ip>\d+\.\d+\.\d+\.\d+) - - '
        r'\[(?P<time>[^\]]+)\] '
        r'"(?P<method>GET|POST|PUT|DELETE) '
        r'(?P<resource>\S+) '
        r'HTTP/\d\.\d" '
        r'(?P<status>\d+) '
        r'(?P<bytes>\d+)$'
    )

    # Process each line
    for line in logs_text.splitlines():

        # Try to match the line
        match = pattern.match(line)

        # If line is invalid
        if not match:
            print(
                f"Warning: Could not parse line: '{line}'. Skipping."
            )
            continue

        # Extract data
        ip = match.group("ip")
        time = match.group("time")
        method = match.group("method")
        resource = match.group("resource")

        status = int(match.group("status"))
        bytes_sent = int(match.group("bytes"))

        # Filter local IP addresses
        if ip.startswith("192.168.") or ip.startswith("10."):
            continue

        # Create dictionary
        log_entry = {
            "ip": ip,
            "time": time,
            "method": method,
            "resource": resource,
            "status": status,
            "bytes": bytes_sent
        }

        # Add external request to results
        results.append(log_entry)

    return results
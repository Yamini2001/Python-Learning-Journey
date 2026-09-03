def traverse_nested_config(config_dict, path_str, default=None):
    """
    Traverses a nested configuration dictionary using a dot-notated path string.
    Uses exception handling instead of explicit type or key existence checks.
    """
    # Defensive Check: If path is empty, return default immediately
    if not path_str:
        return default

    # Split the dot-notated path into a list of individual keys
    keys = path_str.split(".")
    
    # Set up our current node for traversal
    current_node = config_dict

    try:
        # Loop through each key and attempt to step deeper into the dictionary
        for key in keys:
            # We attempt direct indexing. 
            # If current_node is not a dictionary or doesn't have the key, 
            # it will throw an error handled by the except block below.
            current_node = current_node[key]
            
        # If the loop finishes successfully, we have found our value
        return current_node

    except (KeyError, TypeError, AttributeError):
        # Catch lookup errors or trying to index non-dictionary values
        return default


# ==========================================
# Test Data & Verification
# ==========================================
if __name__ == "__main__":
    config = {
        "server": {
            "host": "127.0.0.1",
            "port": 8080,
            "ssl": {
                "enabled": True,
                "cert_path": "/etc/ssl/certs"
            }
        },
        "database": "postgresql://localhost:5432"
    }

    # Test Case 1: Valid Path
    print(traverse_nested_config(config, "server.ssl.cert_path"))
    # Expected Output: /etc/ssl/certs

    # Test Case 2: Missing Key (Triggers KeyError)
    print(traverse_nested_config(config, "server.database.username", "guest"))
    # Expected Output: guest

    # Test Case 3: Indexing Non-Dictionary value (Triggers TypeError)
    print(traverse_nested_config(config, "database.host", "localhost"))
    # Expected Output: localhost

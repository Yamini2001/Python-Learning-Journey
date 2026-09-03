def process_dataset(dataset):

    # Step 1: Parse the raw data
    parsed_data = list(
        map(
            lambda item: (
                item[0],
                float(item[1].split(":")[1]),
                float(item[2].split(":")[1])
            ),
            dataset
        )
    )

    # Step 2: Filter products with price <= 1000
    filtered_data = list(
        filter(
            lambda item: item[1] <= 1000.0,
            parsed_data
        )
    )

    # Step 3: Convert tuples into dictionaries
    mapped_data = list(
        map(
            lambda item: {
                "product": item[0],
                "price": item[1],
                "score": item[2]
            },
            filtered_data
        )
    )

    # Step 4: Sort by score in descending order
    sorted_data = sorted(
        mapped_data,
        key=lambda item: item["score"],
        reverse=True
    )

    return sorted_data
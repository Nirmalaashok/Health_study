def calculate_statistics(df):
    """Calculate mean, median, minimum and maximum  values for selected health columns."""
    columns = [
        "age",
        "weight",
        "height",
        "systolic_bp",
        "cholesterol"
    ]
    statistics = df[columns].agg(
        ["mean", "median", "min", "max"]
    )
    return statistics
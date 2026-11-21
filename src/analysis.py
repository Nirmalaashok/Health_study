def calculate_statistics(df):
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

import numpy as np
import matplotlib.pyplot as plt


class HealthAnalyzer:
    
    def __init__(self, df):
        self.df = df

    def average_blood_pressure(self):
        """
        Calculate the average systolic blood pressure.
        """
        return self.df["systolic_bp"].mean()

    def blood_pressure_regression(self):
        " Calculate linear regression "
        data = self.df[["age", "systolic_bp"]].dropna()

        x = data["age"].to_numpy()
        y = data["systolic_bp"].to_numpy()

        slope, intercept = np.polyfit(x, y, 1)

        return slope, intercept

    def calculate_r_squared(self):
        
        data = self.df[["age", "systolic_bp"]].dropna()
    
        x = data["age"].to_numpy()
        y = data["systolic_bp"].to_numpy()
    
        slope, intercept = np.polyfit(x, y, 1)
    
        y_pred = slope * x + intercept
    
        ss_res = np.sum((y - y_pred) ** 2)
        ss_tot = np.sum((y - np.mean(y)) ** 2)
    
        if ss_tot == 0:
            return np.nan
    
        r_squared = 1 - (ss_res / ss_tot)
    
        return r_squared
    
    def plot_blood_pressure_by_age(self):
        "  Visualise age and systolic blood pressure  with a regression line. "
        data = self.df[["age", "systolic_bp"]].dropna()
    
        x = data["age"].to_numpy()
        y = data["systolic_bp"].to_numpy()
    
        slope, intercept = np.polyfit(x, y, 1)
    
# Sort age values for a correct regression line
        sorted_indices = np.argsort(x)
        x_sorted = x[sorted_indices]
    
        y_pred = slope * x_sorted + intercept
    
        plt.figure(figsize=(8, 5))
    
        plt.scatter(
            x,
            y,
            alpha=0.5,
            label="Actual data"
        )
    
        plt.plot(
                x_sorted,
                y_pred,
                color="red",
                label="Regression line"
            )
    
        plt.xlabel("Age")
        plt.ylabel("Systolic Blood Pressure")
        plt.title("Age vs Systolic Blood Pressure")
        plt.legend()
        plt.show()
    


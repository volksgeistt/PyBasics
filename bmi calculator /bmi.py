def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 16:
        return "Severe Thinness"
    elif 16 <= bmi < 17:
        return "Moderate Thinness"
    elif 17 <= bmi < 18.5:
        return "Mild Thinness"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif 30 <= bmi < 35:
        return "High Risk Zone"
    elif 35 <= bmi < 40:
        return "Very High Risk"
    else:
        return "Extreme Risk Alert"

def main():
    try:
        weight = float(input("Enter your weight in kilograms (kg): "))
        height = float(input("Enter your height in meters (m): "))
        bmi = calculate_bmi(weight, height)
        classification = classify_bmi(bmi)
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"BMI Classification: {classification}")
    except ValueError:
        print("Please enter valid numeric values.")

if __name__ == "__main__":
    main()

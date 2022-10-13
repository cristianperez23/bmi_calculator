def main():
    weight = float(input("Enter your weight in lb or kg: "))
    weight_type = input("Type lb or kg for weight you entered above: ")
    height = float(input("Enter your height in meters: "))
    bmi_conversion(weight_type, weight, height)
    bmi = bmi_conversion(weight_type, weight, height)
    bmi_classification(bmi)
    print("Your BMI is:", round(bmi, 3))
    print("Classification: " + bmi_classification(bmi))

def bmi_conversion(w_t, w, h):
    if w_t == 'kg':
        bmi = w / h**2
        return bmi
    elif w_t == 'lb':
        w = w / 2.205
        bmi = w / h**2
        return bmi
    else:
        exit("Something went wrong :(")

def bmi_classification(bmi):
    if bmi >= 30:
        return "obese"
    elif bmi >= 25:
        return "overweight"
    elif bmi >= 18.5:
        return "normal"
    else:
        return "underweight"

if __name__ == "__main__":
    main()

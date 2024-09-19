from util import input_pos_float

LBS_PER_KG = 2.2046
INCHES_PER_METER = 39.3701

def main():
    weight_lbs = input_pos_float("Please enter weight (pounds): ")
    height_in = input_pos_float("Please enter height (inches): ")

    weight_kg = weight_lbs / LBS_PER_KG
    height_m = height_in / INCHES_PER_METER

    bmi = weight_kg/height_m**2
    
    print("BMI is", bmi)

    if __name__ == '__main__':
        main()

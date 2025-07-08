print("Welcome To Quadratic Formula Calculator")
while True:
    try:
        var_a = int(input("Variable A(enter an integer): "))
        var_b = int(input("Variable B(enter an integer): "))
        var_c = int(input("Variable C(enter an integer): "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")
step1_product = var_a * var_c
step2_product = step1_product * 4
step3_math = var_b ** 2
step4_math = step3_math - step2_product
step5_math = pow(step4_math, 0.5)
step6_math = 2 * var_a
step7_math = -var_b
step8_1_math = step7_math + step5_math
step8_2_math = step7_math - step5_math
finalvalue_1_math = step8_1_math / step6_math
finalvalue_2_math = step8_2_math / step6_math
print("The Final Values Are: x = ", finalvalue_1_math,
      " and x = ", finalvalue_2_math)

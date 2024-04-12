import numpy as np
import PRyM.PRyM_init as PRyMini
import math

def newton_raphson(Yd_f, initial_guess=1, tolerance=1e-6, max_iterations=100):
    # Constants
    Vud = PRyMini.Vud
    gA = PRyMini.gA
    MeV_to_secm1 = PRyMini.MeV_to_secm1
    me = PRyMini.me

    def func(GF):
        return ((Yd_f * (GF * Vud) **  2) / (MeV_to_secm1 * (GF * Vud) **  2 * (1 +  3 * gA **  2) / (2 * np.pi **  3))) ** (1/6) - Vud

    def derivative(GF):
        # Calculate the derivative of the function
        # This is a simplified derivative for illustration purposes
        # You would need to calculate the actual derivative based on the specific form of the function
        return  1/6 * (Yd_f / (GF * Vud) **  2) * (1 +  3 * gA **  2) / (2 * np.pi **  3)

    GF = initial_guess
    for _ in range(max_iterations):
        F = func(GF)
        if abs(F) < tolerance:
            break
        dF = derivative(GF)
        GF -= F / dF

    return GF

# Example usage:
Yd_f_input = float(input("Please input a value for Yd_f: "))
GF_calculated = newton_raphson(Yd_f_input)
print("Calculated value of GF:", GF_calculated)


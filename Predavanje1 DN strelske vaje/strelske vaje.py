import math

temp_H = input("Vpiši hitrost izstrelka (m/s): ")
temp_K = input("Vpiši kot pod katerim bo izstreljena krogla: ")
hitrost = int(temp_H)
kot = int(temp_K)
razdalja = (pow(hitrost,2)*math.sin(math.radians(2 * kot)))/9.807
print("Razdalja izstrelka je : ",razdalja)
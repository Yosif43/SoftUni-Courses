salmon = float(input())
sardine = float(input())
kg_bonito = float(input())
kg_safrid = float(input())
kg_mides = float(input())

bonito = salmon * 1.6 * kg_bonito
safrid = sardine * 1.8 * kg_safrid
mides = kg_mides * 7.50


total = bonito + safrid + mides
print(f"{total:.2f}")

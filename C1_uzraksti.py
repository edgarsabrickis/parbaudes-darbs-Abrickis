# ----------------------------------------------------------------------
# C1. Atzīmju kopsavilkums
# ----------------------------------------------------------------------

# Kodā izveido sarakstu ar septiņām atzīmēm. Izvadi to skaitu, summu, vidējo, augstāko un zemāko. Visu kodu raksti pats.
#
# Šis fails ir tukšs. Visu kodu raksti pats zem šīs rindas.
# ----------------------------------------------------------------------                                                                                                Sarakstu, kurā glabā atzīmes, nosauc ar vārdu atzimju_saraksts.

atzimes = [7, 8, 5, 9, 6, 10, 4]
skaits = len(atzimes)
summa = sum(atzimes)
videjais = summa / skaits
augstaka = max(atzimes)
zemaka = min(atzimes)

print("atzīmju skaits:" , skaits)
print("atzīmju summa:" , summa)
print("Vidējā atzīme:" , videjais)
print("Augstākā atzīme skaits:" , augstaka)
print("zemākā atzīme:" , zemaka)




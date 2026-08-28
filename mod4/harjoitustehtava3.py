sukupuoli=str((input("Sukupuoli: ")))
hemoglobiini=float((input("Hemoglobiini: ")))


if sukupuoli=="mies" and 117 <= hemoglobiini <= 175:
    print("Hemoglobiini tasosi on normaali")

elif sukupuoli=="mies" and hemoglobiini <= 117:
    print("Hemoglobiini tasosi on alhainen")

elif sukupuoli=="mies" and hemoglobiini >= 175:
    print("Hemoglobiini tasosi on korkea")

if sukupuoli=="nainen" and 134 <= hemoglobiini <= 195:
    print("Hemoglobiini tasosi on normaali")

elif sukupuoli=="nainen" and hemoglobiini <= 134:
    print("Hemoglobiini tasosi on alhainen")

elif sukupuoli=="nainen" and hemoglobiini >= 195:
    print("Hemoglobiini tasosi on korkea")











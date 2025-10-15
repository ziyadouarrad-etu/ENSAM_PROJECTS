file=open("table_multi.txt", "w+")
for i in range(1,11):
    file.write(f"La table de multiplication de {i:>2}\n")
    for j in range(1,11):
        file.write(f"{i:>2} x {j:>2} = {i*j}\n")
file.close()

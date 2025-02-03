Archivo = input("Seleccion el archivo: ").lower().strip()

if ".gif" in Archivo:
    print("image/gif")
elif ".jpeg" in Archivo or ".jpg" in Archivo:
    print("image/jpeg")
elif ".png" in Archivo:
    print("image/png")
elif ".pdf" in Archivo:
    print("application/pdf")
elif ".txt" in Archivo:
    print("text/plain")
elif ".zip" in Archivo:
    print("application/zip")
else:
    print("application/octet-stream")

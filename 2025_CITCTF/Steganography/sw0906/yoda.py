# Đọc file gốc
with open("yoda.jpg", "rb") as f:
    data = bytearray(f.read())

# Lật ngược từng nhóm 4 byte
for i in range(0, len(data), 4):
    chunk = data[i:i+4]
    if len(chunk) == 4:  # Đảm bảo nhóm đủ 4 byte
        data[i:i+4] = chunk[::-1]

# Lưu file mới
with open("yodaj_restored.jpg", "wb") as f:
    f.write(data)

print("Đã lật ngược file và lưu thành yodaj_restored.jpg")
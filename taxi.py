def taxi_fare(distance):
    return 35 + max(0, distance - 1) * 5.5

distance = float(input("กรุณาป้อนระยะทาง (กิโลเมตร): "))
print("ค่าโดยสารที่ต้องจ่ายคือ", taxi_fare(distance), "บาท")
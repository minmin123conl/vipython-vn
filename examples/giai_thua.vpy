# Ví dụ tính giai thừa trong ViPython-VN

ham giai_thua(n):
    neu n <= 1:
        tra_ve 1
    khac:
        tra_ve n * giai_thua(n - 1)

# Test hàm giai thừa
voi i trong pham_vi(1, 6):
    ket_qua = giai_thua(i)
    in_ra("Giai thua cua " + chuyen_van_ban(i) + " la: " + chuyen_van_ban(ket_qua))

# Tính giai thừa bằng vòng lặp
ham giai_thua_vong_lap(n):
    ket_qua = 1
    voi i trong pham_vi(1, n + 1):
        ket_qua = ket_qua * i
    tra_ve ket_qua

in_ra("\nSu dung vong lap:")
voi i trong pham_vi(1, 6):
    ket_qua = giai_thua_vong_lap(i)
    in_ra("Giai thua cua " + chuyen_van_ban(i) + " la: " + chuyen_van_ban(ket_qua))


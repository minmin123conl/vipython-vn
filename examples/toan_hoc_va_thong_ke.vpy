# Ví dụ về toán học và thống kê trong ViPython-VN

tu vipython.stdlib.math_vn nhap *
tu random nhap random, randint, gauss

in_ra("=== TOÁN HỌC VÀ THỐNG KÊ TRONG VIPYTHON-VN ===")
in_ra()

# ===== HẰNG SỐ TOÁN HỌC =====
in_ra("1. HẰNG SỐ TOÁN HỌC")
in_ra("-" * 30)

in_ra("π (Pi) =", PI)
in_ra("e (Euler) =", E)
in_ra("τ (Tau) =", TAU)
in_ra()

# ===== HÀNG LƯỢNG GIÁC =====
in_ra("2. HÀNG LƯỢNG GIÁC")
in_ra("-" * 30)

# Tính giá trị lượng giác cho các góc đặc biệt
goc_do = [0, 30, 45, 60, 90, 180, 270, 360]

in_ra("Bảng giá trị lượng giác:")
in_ra("Góc (độ) | Sin      | Cos      | Tan")
in_ra("-" * 40)

voi goc trong goc_do:
    goc_rad = do_sang_radian(goc)
    sin_val = sin(goc_rad)
    cos_val = cos(goc_rad)
    
    # Xử lý tan(90°) và tan(270°) = vô cực
    neu goc == 90 hoac goc == 270:
        tan_val = "∞"
    khac:
        tan_val = round(tan(goc_rad), 6)
    
    in_ra(f"{goc:8} | {sin_val:8.6f} | {cos_val:8.6f} | {tan_val}")

in_ra()

# ===== HÀNG MŨ VÀ LOGARIT =====
in_ra("3. HÀNG MŨ VÀ LOGARIT")
in_ra("-" * 30)

# Ví dụ về lãi suất kép
von_ban_dau = 10000000  # 10 triệu VND
lai_suat = 0.08  # 8% năm
so_nam = 10

in_ra("Tính lãi suất kép:")
in_ra("Vốn ban đầu:", von_ban_dau, "VND")
in_ra("Lãi suất:", lai_suat * 100, "% năm")
in_ra("Thời gian:", so_nam, "năm")

voi nam trong pham_vi(1, so_nam + 1):
    gia_tri = von_ban_dau * pow(1 + lai_suat, nam)
    in_ra("Năm", nam, ":", round(gia_tri), "VND")

# Tính thời gian để vốn tăng gấp đôi
thoi_gian_gap_doi = log(2) / log(1 + lai_suat)
in_ra("Thời gian để vốn tăng gấp đôi:", round(thoi_gian_gap_doi, 2), "năm")

in_ra()

# ===== THỐNG KÊ CƠ BẢN =====
in_ra("4. THỐNG KÊ CƠ BẢN")
in_ra("-" * 30)

# Tạo dữ liệu mẫu: điểm thi của 50 học sinh
diem_thi = []
voi i trong pham_vi(50):
    # Tạo điểm theo phân phối chuẩn, trung bình 7, độ lệch chuẩn 1.5
    diem = gauss(7, 1.5)
    # Giới hạn điểm từ 0 đến 10
    diem = max(0, min(10, diem))
    diem_thi.append(round(diem, 1))

in_ra("Phân tích điểm thi của 50 học sinh:")
in_ra("Dữ liệu mẫu (10 điểm đầu):", diem_thi[:10])

# Tính các thống kê cơ bản
tb = trung_binh(diem_thi)
tv = trung_vi(diem_thi)
min_diem = nho_nhat(diem_thi)
max_diem = lon_nhat(diem_thi)
ps = phuong_sai(diem_thi)
dlc = do_lech_chuan(diem_thi)

in_ra()
in_ra("Thống kê mô tả:")
in_ra("- Trung bình:", round(tb, 2))
in_ra("- Trung vị:", round(tv, 2))
in_ra("- Điểm thấp nhất:", min_diem)
in_ra("- Điểm cao nhất:", max_diem)
in_ra("- Phương sai:", round(ps, 2))
in_ra("- Độ lệch chuẩn:", round(dlc, 2))

# Phân loại điểm
xuat_sac = 0
gioi = 0
kha = 0
trung_binh = 0
yeu = 0

voi diem trong diem_thi:
    neu diem >= 9:
        xuat_sac += 1
    neu_khac diem >= 8:
        gioi += 1
    neu_khac diem >= 6.5:
        kha += 1
    neu_khac diem >= 5:
        trung_binh += 1
    khac:
        yeu += 1

in_ra()
in_ra("Phân loại học lực:")
in_ra("- Xuất sắc (9-10):", xuat_sac, "học sinh", f"({xuat_sac/50*100:.1f}%)")
in_ra("- Giỏi (8-8.9):", gioi, "học sinh", f"({gioi/50*100:.1f}%)")
in_ra("- Khá (6.5-7.9):", kha, "học sinh", f"({kha/50*100:.1f}%)")
in_ra("- Trung bình (5-6.4):", trung_binh, "học sinh", f"({trung_binh/50*100:.1f}%)")
in_ra("- Yếu (<5):", yeu, "học sinh", f"({yeu/50*100:.1f}%)")

in_ra()

# ===== TỔ HỢP VÀ CHỈNH HỢP =====
in_ra("5. TỔ HỢP VÀ CHỈNH HỢP")
in_ra("-" * 30)

# Bài toán xổ số
in_ra("Bài toán xổ số:")
in_ra("Xổ số có 45 số, chọn 6 số. Tính xác suất trúng giải đặc biệt.")

tong_cach_chon = to_hop(45, 6)
xac_suat = 1 / tong_cach_chon

in_ra("Tổng số cách chọn 6 số từ 45 số:", tong_cach_chon)
in_ra("Xác suất trúng giải đặc biệt:", f"{xac_suat:.10f}")
in_ra("Tức là 1 trong", tong_cach_chon, "lần chơi")

# Bài toán sắp xếp
in_ra()
in_ra("Bài toán sắp xếp:")
in_ra("Có 8 người xếp hàng. Có bao nhiều cách sắp xếp?")

so_cach_sap_xep = giai_thua(8)
in_ra("Số cách sắp xếp 8 người:", so_cach_sap_xep)

# Nếu có 3 người phải đứng cạnh nhau
in_ra("Nếu có 3 người phải đứng cạnh nhau:")
# Coi 3 người như 1 nhóm -> có 6 vị trí để sắp xếp
# Trong nhóm 3 người có 3! cách sắp xếp
so_cach_co_dieu_kien = giai_thua(6) * giai_thua(3)
in_ra("Số cách sắp xếp:", so_cach_co_dieu_kien)

in_ra()

# ===== HÌNH HỌC =====
in_ra("6. HÌNH HỌC")
in_ra("-" * 30)

# Tính diện tích và chu vi các hình
in_ra("Tính toán hình học:")

# Hình tròn
ban_kinh = 5
dien_tich_tron = PI * pow(ban_kinh, 2)
chu_vi_tron = 2 * PI * ban_kinh

in_ra("Hình tròn bán kính", ban_kinh, ":")
in_ra("- Diện tích:", round(dien_tich_tron, 2))
in_ra("- Chu vi:", round(chu_vi_tron, 2))

# Tam giác vuông
canh_a = 3
canh_b = 4
canh_c = sqrt(pow(canh_a, 2) + pow(canh_b, 2))
dien_tich_tam_giac = 0.5 * canh_a * canh_b

in_ra()
in_ra("Tam giác vuông cạnh", canh_a, "và", canh_b, ":")
in_ra("- Cạnh huyền:", round(canh_c, 2))
in_ra("- Diện tích:", dien_tich_tam_giac)

# Hình cầu
ban_kinh_cau = 3
the_tich_cau = (4/3) * PI * pow(ban_kinh_cau, 3)
dien_tich_mat_cau = 4 * PI * pow(ban_kinh_cau, 2)

in_ra()
in_ra("Hình cầu bán kính", ban_kinh_cau, ":")
in_ra("- Thể tích:", round(the_tich_cau, 2))
in_ra("- Diện tích mặt cầu:", round(dien_tich_mat_cau, 2))

in_ra()

# ===== ỨNG DỤNG THỰC TẾ =====
in_ra("7. ỨNG DỤNG THỰC TẾ")
in_ra("-" * 30)

# Tính lương sau thuế
ham tinh_luong_sau_thue(luong_goc):
    """Tính lương sau thuế theo luật Việt Nam (đơn giản hóa)"""
    
    # Giảm trừ gia cảnh
    giam_tru = 11000000  # 11 triệu/tháng
    
    # Thu nhập chịu thuế
    thu_nhap_chiu_thue = max(0, luong_goc - giam_tru)
    
    # Tính thuế theo bậc thang
    thue = 0
    neu thu_nhap_chiu_thue <= 5000000:
        thue = thu_nhap_chiu_thue * 0.05
    neu_khac thu_nhap_chiu_thue <= 10000000:
        thue = 5000000 * 0.05 + (thu_nhap_chiu_thue - 5000000) * 0.1
    neu_khac thu_nhap_chiu_thue <= 18000000:
        thue = 5000000 * 0.05 + 5000000 * 0.1 + (thu_nhap_chiu_thue - 10000000) * 0.15
    khac:
        thue = 5000000 * 0.05 + 5000000 * 0.1 + 8000000 * 0.15 + (thu_nhap_chiu_thue - 18000000) * 0.2
    
    luong_sau_thue = luong_goc - thue
    tra_ve luong_sau_thue, thue

# Test với các mức lương khác nhau
cac_muc_luong = [8000000, 15000000, 25000000, 50000000]

in_ra("Tính thuế thu nhập cá nhân:")
in_ra("Lương gốc     | Thuế TNCN    | Lương sau thuế")
in_ra("-" * 50)

voi luong trong cac_muc_luong:
    luong_net, thue = tinh_luong_sau_thue(luong)
    in_ra(f"{luong:12,} | {thue:12,.0f} | {luong_net:14,.0f}")

in_ra()
in_ra("=== KẾT LUẬN ===")
in_ra("ViPython-VN cung cấp đầy đủ các hàm toán học và thống kê")
in_ra("để giải quyết các bài toán thực tế trong học tập và công việc.")


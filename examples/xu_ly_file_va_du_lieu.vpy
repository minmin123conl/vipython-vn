# Ví dụ về xử lý file và dữ liệu trong ViPython-VN

tu vipython.stdlib.file nhap *
tu vipython.stdlib.chuoi nhap *
tu vipython.stdlib.ngay_gio nhap *

in_ra("=== XỬ LÝ FILE VÀ DỮ LIỆU TRONG VIPYTHON-VN ===")
in_ra()

# ===== TẠO VÀ GHI FILE =====
in_ra("1. TẠO VÀ GHI FILE")
in_ra("-" * 30)

# Tạo file văn bản đơn giản
noi_dung_file = """Đây là file test của ViPython-VN
Dòng thứ hai
Dòng thứ ba với ký tự đặc biệt: áàảãạ
Số: 123, 456.789
Ngày: """ + dinh_dang_ngay_gio(bay_gio())

ghi_file("test.txt", noi_dung_file)
in_ra("Đã tạo file test.txt")

# Đọc và hiển thị nội dung
noi_dung = doc_file("test.txt")
in_ra("Nội dung file:")
in_ra(noi_dung)
in_ra()

# ===== XỬ LÝ FILE CSV =====
in_ra("2. XỬ LÝ FILE CSV")
in_ra("-" * 30)

# Tạo dữ liệu sinh viên
du_lieu_sinh_vien = [
    ["Họ tên", "Tuổi", "Điểm TB", "Xếp loại"],
    ["Nguyễn Văn An", 20, 8.5, "Giỏi"],
    ["Trần Thị Bình", 19, 7.2, "Khá"],
    ["Lê Văn Cường", 21, 9.1, "Xuất sắc"],
    ["Phạm Thị Dung", 20, 6.8, "Trung bình"],
    ["Hoàng Văn Em", 22, 8.9, "Giỏi"]
]

# Ghi file CSV
ghi_csv("sinh_vien.csv", du_lieu_sinh_vien[1:], tieu_de=du_lieu_sinh_vien[0])
in_ra("Đã tạo file sinh_vien.csv")

# Đọc file CSV
du_lieu_csv = doc_csv("sinh_vien.csv")
in_ra("Dữ liệu từ file CSV:")
in_ra("Tiêu đề:", du_lieu_csv["tieu_de"])
voi i, hang trong enumerate(du_lieu_csv["du_lieu"]):
    in_ra("Sinh viên", i+1, ":", hang)

in_ra()

# ===== XỬ LÝ FILE JSON =====
in_ra("3. XỬ LÝ FILE JSON")
in_ra("-" * 30)

# Tạo dữ liệu JSON
du_lieu_json = {
    "truong": "Đại học Bách Khoa",
    "khoa": "Công nghệ Thông tin",
    "sinh_vien": [
        {
            "ma_sv": "SV001",
            "ho_ten": "Nguyễn Văn An",
            "tuoi": 20,
            "diem": [8.5, 7.8, 9.2, 8.1],
            "hoc_bong": dung_vay
        },
        {
            "ma_sv": "SV002", 
            "ho_ten": "Trần Thị Bình",
            "tuoi": 19,
            "diem": [7.2, 6.9, 8.0, 7.5],
            "hoc_bong": sai_vay
        }
    ],
    "ngay_tao": dinh_dang_ngay_gio(bay_gio())
}

# Ghi file JSON
ghi_json("du_lieu.json", du_lieu_json)
in_ra("Đã tạo file du_lieu.json")

# Đọc file JSON
du_lieu_doc = doc_json("du_lieu.json")
in_ra("Dữ liệu từ file JSON:")
in_ra("Trường:", du_lieu_doc["truong"])
in_ra("Khoa:", du_lieu_doc["khoa"])
in_ra("Số sinh viên:", len(du_lieu_doc["sinh_vien"]))

voi sv trong du_lieu_doc["sinh_vien"]:
    in_ra("- Mã SV:", sv["ma_sv"], "| Họ tên:", sv["ho_ten"])
    diem_tb = sum(sv["diem"]) / len(sv["diem"])
    in_ra("  Điểm TB:", round(diem_tb, 2), "| Học bổng:", sv["hoc_bong"])

in_ra()

# ===== XỬ LÝ CHUỖI NÂNG CAO =====
in_ra("4. XỬ LÝ CHUỖI NÂNG CAO")
in_ra("-" * 30)

# Đọc file và xử lý từng dòng
cac_dong = doc_dong("test.txt")
in_ra("Xử lý từng dòng trong file:")

voi i, dong trong enumerate(cac_dong):
    dong_sach = cat_khoang_trang(dong)
    neu dong_sach:
        in_ra("Dòng", i+1, ":")
        in_ra("  Nội dung:", dong_sach)
        in_ra("  Độ dài:", do_dai(dong_sach))
        in_ra("  Chữ hoa:", viet_hoa(dong_sach))
        in_ra("  Có chứa số:", la_chu_so(dong_sach) neu khong la_chu_so(dong_sach) khac "Có số")
        in_ra()

# ===== THỐNG KÊ VÀ PHÂN TÍCH DỮ LIỆU =====
in_ra("5. THỐNG KÊ VÀ PHÂN TÍCH DỮ LIỆU")
in_ra("-" * 30)

# Phân tích điểm sinh viên từ file CSV
in_ra("Phân tích điểm sinh viên:")

tong_diem = 0
so_sinh_vien = 0
diem_cao_nhat = 0
diem_thap_nhat = 10
sinh_vien_gioi = 0

voi hang trong du_lieu_csv["du_lieu"]:
    ten = hang[0]
    diem = float(hang[2])
    xep_loai = hang[3]
    
    tong_diem += diem
    so_sinh_vien += 1
    
    neu diem > diem_cao_nhat:
        diem_cao_nhat = diem
        sv_cao_nhat = ten
    
    neu diem < diem_thap_nhat:
        diem_thap_nhat = diem
        sv_thap_nhat = ten
    
    neu xep_loai == "Giỏi" hoac xep_loai == "Xuất sắc":
        sinh_vien_gioi += 1

diem_trung_binh = tong_diem / so_sinh_vien
ty_le_gioi = (sinh_vien_gioi / so_sinh_vien) * 100

in_ra("Kết quả thống kê:")
in_ra("- Số sinh viên:", so_sinh_vien)
in_ra("- Điểm trung bình lớp:", round(diem_trung_binh, 2))
in_ra("- Điểm cao nhất:", diem_cao_nhat, "(" + sv_cao_nhat + ")")
in_ra("- Điểm thấp nhất:", diem_thap_nhat, "(" + sv_thap_nhat + ")")
in_ra("- Tỷ lệ sinh viên giỏi:", round(ty_le_gioi, 1), "%")

in_ra()

# ===== TẠO BÁO CÁO =====
in_ra("6. TẠO BÁO CÁO")
in_ra("-" * 30)

# Tạo báo cáo tổng hợp
bao_cao = """BÁO CÁO THỐNG KÊ ĐIỂM SINH VIÊN
""" + "=" * 40 + """

Thời gian tạo báo cáo: """ + dinh_dang_tieng_viet(bay_gio()) + """

THÔNG TIN CHUNG:
- Số sinh viên: """ + str(so_sinh_vien) + """
- Điểm trung bình lớp: """ + str(round(diem_trung_binh, 2)) + """

THỐNG KÊ CHI TIẾT:
"""

voi hang trong du_lieu_csv["du_lieu"]:
    ten = hang[0]
    tuoi = hang[1] 
    diem = hang[2]
    xep_loai = hang[3]
    
    bao_cao += "- " + ten + " (" + tuoi + " tuổi): " + diem + " điểm - " + xep_loai + "\n"

bao_cao += """
KẾT LUẬN:
- Sinh viên có điểm cao nhất: """ + sv_cao_nhat + " (" + str(diem_cao_nhat) + """ điểm)
- Sinh viên có điểm thấp nhất: """ + sv_thap_nhat + " (" + str(diem_thap_nhat) + """ điểm)
- Tỷ lệ sinh viên đạt loại giỏi trở lên: """ + str(round(ty_le_gioi, 1)) + """%

Báo cáo được tạo tự động bởi ViPython-VN
"""

# Lưu báo cáo
ghi_file("bao_cao_diem.txt", bao_cao)
in_ra("Đã tạo báo cáo chi tiết trong file bao_cao_diem.txt")

# ===== DỌN DẸP FILE =====
in_ra()
in_ra("7. QUẢN LÝ FILE")
in_ra("-" * 30)

# Liệt kê các file đã tạo
cac_file = liet_ke_file(".", bao_gom_thu_muc=sai_vay)
file_vua_tao = []

voi file trong cac_file:
    neu file.endswith((".txt", ".csv", ".json")):
        file_vua_tao.append(file)

in_ra("Các file đã tạo:")
voi file trong file_vua_tao:
    kich_thuoc = kich_thuoc_file(file)
    thoi_gian = dinh_dang_ngay_gio(thoi_gian_sua_doi(file))
    in_ra("-", file, ":", dinh_dang_dung_luong(kich_thuoc), "- Sửa đổi:", thoi_gian)

in_ra()
in_ra("=== HOÀN THÀNH ===")
in_ra("Đã demo các tính năng xử lý file và dữ liệu của ViPython-VN!")
in_ra("Các file tạo ra có thể được sử dụng cho các ví dụ khác.")


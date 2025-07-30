# Ví dụ về cấu trúc dữ liệu trong ViPython-VN

tu vipython.stdlib.thuat_toan nhap Ngan_xep, Hang_doi, Hang_doi_uu_tien

in_ra("=== CẤU TRÚC DỮ LIỆU TRONG VIPYTHON-VN ===")
in_ra()

# ===== NGĂN XẾP (STACK) =====
in_ra("1. NGĂN XẾP (STACK) - LIFO (Last In, First Out)")
in_ra("-" * 50)

# Tạo ngăn xếp
ngan_xep = Ngan_xep()

# Thêm phần tử vào ngăn xếp
in_ra("Đẩy các phần tử vào ngăn xếp:")
voi item trong [1, 2, 3, 4, 5]:
    ngan_xep.day_vao(item)
    in_ra("Đẩy", item, "- Kích thước:", ngan_xep.kich_thuoc())

in_ra()
in_ra("Lấy các phần tử ra khỏi ngăn xếp:")
trong_khi khong ngan_xep.rong():
    item = ngan_xep.lay_ra()
    in_ra("Lấy ra", item, "- Kích thước:", ngan_xep.kich_thuoc())

in_ra()

# ===== HÀNG ĐỢI (QUEUE) =====
in_ra("2. HÀNG ĐỢI (QUEUE) - FIFO (First In, First Out)")
in_ra("-" * 50)

# Tạo hàng đợi
hang_doi = Hang_doi()

# Thêm phần tử vào hàng đợi
in_ra("Thêm các phần tử vào hàng đợi:")
voi item trong ["A", "B", "C", "D", "E"]:
    hang_doi.them_vao(item)
    in_ra("Thêm", item, "- Kích thước:", hang_doi.kich_thuoc())

in_ra()
in_ra("Lấy các phần tử ra khỏi hàng đợi:")
trong_khi khong hang_doi.rong():
    item = hang_doi.lay_ra()
    in_ra("Lấy ra", item, "- Kích thước:", hang_doi.kich_thuoc())

in_ra()

# ===== HÀNG ĐỢI ƯU TIÊN (PRIORITY QUEUE) =====
in_ra("3. HÀNG ĐỢI ƯU TIÊN (PRIORITY QUEUE)")
in_ra("-" * 50)

# Tạo hàng đợi ưu tiên
hang_doi_uu_tien = Hang_doi_uu_tien()

# Thêm các công việc với độ ưu tiên khác nhau
cong_viec = [
    ("Làm bài tập", 3),
    ("Ăn cơm", 1),
    ("Đi ngủ", 2),
    ("Học bài", 1),
    ("Chơi game", 5)
]

in_ra("Thêm các công việc với độ ưu tiên:")
voi ten, uu_tien trong cong_viec:
    hang_doi_uu_tien.them_vao(ten, uu_tien)
    in_ra("Thêm:", ten, "- Ưu tiên:", uu_tien)

in_ra()
in_ra("Thực hiện công việc theo độ ưu tiên (số nhỏ = ưu tiên cao):")
trong_khi khong hang_doi_uu_tien.rong():
    cong_viec = hang_doi_uu_tien.lay_ra()
    in_ra("Thực hiện:", cong_viec)

in_ra()

# ===== ỨNG DỤNG THỰC TẾ =====
in_ra("4. ỨNG DỤNG THỰC TẾ")
in_ra("-" * 50)

# Ứng dụng ngăn xếp: Kiểm tra dấu ngoặc cân bằng
ham kiem_tra_ngoac_can_bang(bieu_thuc):
    ngan_xep = Ngan_xep()
    cap_ngoac = {"(": ")", "[": "]", "{": "}"}
    
    voi ky_tu trong bieu_thuc:
        neu ky_tu trong cap_ngoac:
            ngan_xep.day_vao(ky_tu)
        neu_khac ky_tu trong cap_ngoac.values():
            neu ngan_xep.rong():
                tra_ve sai_vay
            ngoac_mo = ngan_xep.lay_ra()
            neu cap_ngoac[ngoac_mo] != ky_tu:
                tra_ve sai_vay
    
    tra_ve ngan_xep.rong()

# Test kiểm tra dấu ngoặc
bieu_thuc_test = [
    "(a + b) * [c - d]",
    "((a + b) * c",
    "{[a + b] * (c - d)}",
    "([)]"
]

in_ra("Kiểm tra dấu ngoặc cân bằng:")
voi bt trong bieu_thuc_test:
    ket_qua = kiem_tra_ngoac_can_bang(bt)
    trang_thai = "Cân bằng" neu ket_qua khac "Không cân bằng"
    in_ra(bt, "->", trang_thai)

in_ra()

# Ứng dụng hàng đợi: Mô phỏng hệ thống phục vụ khách hàng
ham mo_phong_phuc_vu_khach_hang():
    hang_doi_khach = Hang_doi()
    
    # Khách hàng đến
    khach_hang = ["Khách A", "Khách B", "Khách C", "Khách D"]
    
    in_ra("Khách hàng đến xếp hàng:")
    voi khach trong khach_hang:
        hang_doi_khach.them_vao(khach)
        in_ra(khach, "đã vào hàng đợi - Số người chờ:", hang_doi_khach.kich_thuoc())
    
    in_ra()
    in_ra("Phục vụ khách hàng:")
    thu_tu = 1
    trong_khi khong hang_doi_khach.rong():
        khach = hang_doi_khach.lay_ra()
        in_ra("Phục vụ", khach, "(thứ tự:", thu_tu, ") - Còn lại:", hang_doi_khach.kich_thuoc())
        thu_tu += 1

mo_phong_phuc_vu_khach_hang()

in_ra()

# Ứng dụng hàng đợi ưu tiên: Hệ thống cấp cứu bệnh viện
ham mo_phong_cap_cuu():
    hang_doi_cap_cuu = Hang_doi_uu_tien()
    
    # Bệnh nhân với mức độ nghiêm trọng khác nhau
    benh_nhan = [
        ("Bệnh nhân A - Đau đầu nhẹ", 3),
        ("Bệnh nhân B - Gãy chân", 2),
        ("Bệnh nhân C - Đau tim", 1),
        ("Bệnh nhân D - Cảm cúm", 4),
        ("Bệnh nhân E - Tai nạn giao thông", 1)
    ]
    
    in_ra("Bệnh nhân đến cấp cứu:")
    voi ten, muc_do trong benh_nhan:
        hang_doi_cap_cuu.them_vao(ten, muc_do)
        in_ra(ten, "- Mức độ:", muc_do)
    
    in_ra()
    in_ra("Thứ tự điều trị (mức độ 1 = khẩn cấp nhất):")
    thu_tu = 1
    trong_khi khong hang_doi_cap_cuu.rong():
        benh_nhan = hang_doi_cap_cuu.lay_ra()
        in_ra(thu_tu, ".", benh_nhan)
        thu_tu += 1

mo_phong_cap_cuu()

in_ra()
in_ra("=== KẾT LUẬN ===")
in_ra("- Ngăn xếp: Dùng cho undo/redo, kiểm tra cú pháp, đệ quy")
in_ra("- Hàng đợi: Dùng cho xử lý tác vụ theo thứ tự, BFS")
in_ra("- Hàng đợi ưu tiên: Dùng cho lập lịch, thuật toán Dijkstra")


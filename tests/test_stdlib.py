"""
Tests cho thư viện chuẩn ViPython-VN
"""

import pytest
import sys
import os

# Thêm đường dẫn để import các module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from vipython.stdlib import math_vn, chuoi, ngay_gio, file, thuat_toan

def test_math_vn():
    """Test module toán học"""
    # Test hằng số
    assert abs(math_vn.PI - 3.14159) < 0.001
    assert abs(math_vn.E - 2.71828) < 0.001
    
    # Test hàm lượng giác
    assert abs(math_vn.sin(0)) < 0.001
    assert abs(math_vn.cos(0) - 1) < 0.001
    
    # Test hàm mũ và logarit
    assert abs(math_vn.exp(0) - 1) < 0.001
    assert abs(math_vn.log(math_vn.E) - 1) < 0.001
    
    # Test hàm làm tròn
    assert math_vn.lam_tron(3.7) == 4
    assert math_vn.lam_tron_len(3.1) == 4
    assert math_vn.lam_tron_xuong(3.9) == 3
    
    # Test giá trị tuyệt đối
    assert math_vn.gia_tri_tuyet_doi(-5) == 5
    assert math_vn.gia_tri_tuyet_doi(5) == 5
    
    # Test min/max
    assert math_vn.nho_nhat([1, 2, 3]) == 1
    assert math_vn.lon_nhat([1, 2, 3]) == 3
    
    # Test giai thừa
    assert math_vn.giai_thua(5) == 120
    assert math_vn.giai_thua(0) == 1
    
    # Test tổ hợp
    assert math_vn.to_hop(5, 2) == 10
    assert math_vn.chinh_hop(5, 2) == 20

def test_chuoi():
    """Test module xử lý chuỗi"""
    # Test độ dài
    assert chuoi.do_dai("hello") == 5
    
    # Test chuyển đổi case
    assert chuoi.viet_hoa("hello") == "HELLO"
    assert chuoi.viet_thuong("HELLO") == "hello"
    assert chuoi.viet_hoa_chu_dau("hello world") == "Hello world"
    assert chuoi.viet_hoa_tung_tu("hello world") == "Hello World"
    
    # Test cắt khoảng trắng
    assert chuoi.cat_khoang_trang("  hello  ") == "hello"
    assert chuoi.cat_khoang_trang_trai("  hello  ") == "hello  "
    assert chuoi.cat_khoang_trang_phai("  hello  ") == "  hello"
    
    # Test thay thế
    assert chuoi.thay_the("hello world", "world", "python") == "hello python"
    
    # Test tách và nối
    assert chuoi.tach_chuoi("a,b,c", ",") == ["a", "b", "c"]
    assert chuoi.noi_chuoi(["a", "b", "c"], ",") == "a,b,c"
    
    # Test kiểm tra
    assert chuoi.bat_dau_bang("hello", "he") == True
    assert chuoi.ket_thuc_bang("hello", "lo") == True
    assert chuoi.chua("hello", "ell") == True
    
    # Test tìm vị trí
    assert chuoi.tim_vi_tri("hello", "e") == 1
    assert chuoi.tim_vi_tri("hello", "x") == -1
    
    # Test kiểm tra kiểu
    assert chuoi.la_chu_so("123") == True
    assert chuoi.la_chu_so("12a") == False
    assert chuoi.la_chu_cai("abc") == True
    assert chuoi.la_chu_cai("ab3") == False
    
    # Test đảo ngược
    assert chuoi.dao_nguoc("hello") == "olleh"
    
    # Test lặp lại
    assert chuoi.lap_lai("ab", 3) == "ababab"

def test_ngay_gio():
    """Test module ngày giờ"""
    import datetime
    
    # Test tạo ngày
    ngay = ngay_gio.tao_ngay(2024, 1, 1)
    assert ngay.year == 2024
    assert ngay.month == 1
    assert ngay.day == 1
    
    # Test tạo giờ
    gio = ngay_gio.tao_gio(12, 30, 45)
    assert gio.hour == 12
    assert gio.minute == 30
    assert gio.second == 45
    
    # Test lấy thông tin
    assert ngay_gio.lay_nam(ngay) == 2024
    assert ngay_gio.lay_thang(ngay) == 1
    assert ngay_gio.lay_ngay(ngay) == 1
    
    # Test cộng ngày
    ngay_moi = ngay_gio.cong_ngay(ngay, 10)
    assert ngay_moi.day == 11
    
    # Test năm nhuận
    assert ngay_gio.la_nam_nhuan(2024) == True
    assert ngay_gio.la_nam_nhuan(2023) == False
    
    # Test số ngày trong tháng
    assert ngay_gio.so_ngay_trong_thang(2024, 2) == 29  # Năm nhuận
    assert ngay_gio.so_ngay_trong_thang(2023, 2) == 28  # Năm thường

def test_thuat_toan():
    """Test module thuật toán"""
    # Test sắp xếp
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    sorted_arr = [1, 1, 2, 3, 4, 5, 6, 9]
    
    assert thuat_toan.sap_xep_noi_bot(arr) == sorted_arr
    assert thuat_toan.sap_xep_chen(arr) == sorted_arr
    assert thuat_toan.sap_xep_lua_chon(arr) == sorted_arr
    assert thuat_toan.sap_xep_nhanh(arr) == sorted_arr
    assert thuat_toan.sap_xep_tron(arr) == sorted_arr
    
    # Test tìm kiếm
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert thuat_toan.tim_kiem_tuyen_tinh(sorted_list, 5) == 4
    assert thuat_toan.tim_kiem_nhi_phan(sorted_list, 5) == 4
    assert thuat_toan.tim_kiem_tuyen_tinh(sorted_list, 10) == -1
    
    # Test ngăn xếp
    stack = thuat_toan.Ngan_xep()
    assert stack.rong() == True
    
    stack.day_vao(1)
    stack.day_vao(2)
    stack.day_vao(3)
    assert stack.kich_thuoc() == 3
    assert stack.xem_dinh() == 3
    assert stack.lay_ra() == 3
    assert stack.kich_thuoc() == 2
    
    # Test hàng đợi
    queue = thuat_toan.Hang_doi()
    assert queue.rong() == True
    
    queue.them_vao(1)
    queue.them_vao(2)
    queue.them_vao(3)
    assert queue.kich_thuoc() == 3
    assert queue.xem_dau() == 1
    assert queue.lay_ra() == 1
    assert queue.kich_thuoc() == 2
    
    # Test hàng đợi ưu tiên
    pq = thuat_toan.Hang_doi_uu_tien()
    pq.them_vao("task1", 3)
    pq.them_vao("task2", 1)
    pq.them_vao("task3", 2)
    
    assert pq.lay_ra() == "task2"  # Ưu tiên 1 (cao nhất)
    assert pq.lay_ra() == "task3"  # Ưu tiên 2
    assert pq.lay_ra() == "task1"  # Ưu tiên 3
    
    # Test Fibonacci
    assert thuat_toan.fibonacci(0) == 0
    assert thuat_toan.fibonacci(1) == 1
    assert thuat_toan.fibonacci(5) == 5
    assert thuat_toan.fibonacci(10) == 55
    
    # Test GCD và LCM
    assert thuat_toan.gcd(12, 8) == 4
    assert thuat_toan.lcm(12, 8) == 24
    
    # Test số nguyên tố
    assert thuat_toan.la_so_nguyen_to(2) == True
    assert thuat_toan.la_so_nguyen_to(3) == True
    assert thuat_toan.la_so_nguyen_to(4) == False
    assert thuat_toan.la_so_nguyen_to(17) == True
    
    # Test sàng Eratosthenes
    primes = thuat_toan.sang_eratosthenes(10)
    assert primes == [2, 3, 5, 7]
    
    # Test các hàm tiện ích
    assert thuat_toan.dao_nguoc_danh_sach([1, 2, 3]) == [3, 2, 1]
    assert thuat_toan.loai_bo_trung_lap([1, 2, 2, 3, 3, 3]) == [1, 2, 3]
    assert thuat_toan.giao_hai_tap([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert set(thuat_toan.hop_hai_tap([1, 2, 3], [2, 3, 4])) == {1, 2, 3, 4}

def test_file_operations():
    """Test các thao tác file cơ bản"""
    import tempfile
    import os
    
    # Tạo file tạm
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        temp_file = f.name
        f.write("Test content\nLine 2\nLine 3")
    
    try:
        # Test đọc file
        content = file.doc_file(temp_file)
        assert "Test content" in content
        
        # Test đọc dòng
        lines = file.doc_dong(temp_file)
        assert len(lines) == 3
        assert "Test content" in lines[0]
        
        # Test kiểm tra file
        assert file.ton_tai(temp_file) == True
        assert file.la_file(temp_file) == True
        assert file.la_thu_muc(temp_file) == False
        
        # Test kích thước file
        size = file.kich_thuoc_file(temp_file)
        assert size > 0
        
        # Test thời gian
        mod_time = file.thoi_gian_sua_doi(temp_file)
        assert mod_time is not None
        
    finally:
        # Dọn dẹp
        if os.path.exists(temp_file):
            os.unlink(temp_file)

if __name__ == "__main__":
    pytest.main([__file__])


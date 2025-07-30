"""
Các hàm built-in cho ViPython-VN
"""

import sys
import os
from typing import Any, Dict, Callable

def in_ra(*args, **kwargs):
    """Hàm in ra (print)"""
    print(*args, **kwargs)

def nhap_vao(prompt: str = "") -> str:
    """Hàm nhập vào (input)"""
    return input(prompt)

def do_dai(obj) -> int:
    """Hàm độ dài (len)"""
    return len(obj)

def kieu(obj) -> type:
    """Hàm kiểu dữ liệu (type)"""
    return type(obj)

def chuyen_so(s) -> float:
    """Chuyển chuỗi thành số"""
    try:
        if '.' in str(s):
            return float(s)
        else:
            return int(s)
    except ValueError:
        raise ValueError(f"Không thể chuyển '{s}' thành số")

def chuyen_van_ban(obj) -> str:
    """Chuyển đối tượng thành chuỗi"""
    return str(obj)

def chuyen_so_nguyen(obj) -> int:
    """Chuyển đối tượng thành số nguyên"""
    return int(obj)

def chuyen_so_thuc(obj) -> float:
    """Chuyển đối tượng thành số thực"""
    return float(obj)

def pham_vi(*args):
    """Tạo dãy số (range)"""
    return list(range(*args))

def sap_xep(iterable, dao_nguoc=False):
    """Sắp xếp danh sách (sorted)"""
    return sorted(iterable, reverse=dao_nguoc)

def dao_nguoc(iterable):
    """Đảo ngược danh sách (reversed)"""
    return list(reversed(iterable))

def tong(iterable):
    """Tính tổng các phần tử (sum)"""
    return sum(iterable)

def nho_nhat(iterable):
    """Tìm giá trị nhỏ nhất (min)"""
    return min(iterable)

def lon_nhat(iterable):
    """Tìm giá trị lớn nhất (max)"""
    return max(iterable)

def tat_ca(iterable):
    """Kiểm tra tất cả phần tử đều True (all)"""
    return all(iterable)

def bat_ky(iterable):
    """Kiểm tra có ít nhất một phần tử True (any)"""
    return any(iterable)

def dem(iterable, gia_tri):
    """Đếm số lần xuất hiện của giá trị"""
    return iterable.count(gia_tri)

def tim_vi_tri(iterable, gia_tri):
    """Tìm vị trí đầu tiên của giá trị"""
    try:
        return iterable.index(gia_tri)
    except ValueError:
        return -1

def la_so(obj):
    """Kiểm tra có phải số không"""
    return isinstance(obj, (int, float))

def la_chuoi(obj):
    """Kiểm tra có phải chuỗi không"""
    return isinstance(obj, str)

def la_danh_sach(obj):
    """Kiểm tra có phải danh sách không"""
    return isinstance(obj, list)

def la_tu_dien(obj):
    """Kiểm tra có phải từ điển không"""
    return isinstance(obj, dict)

def nhap_module(ten_module):
    """Import module"""
    try:
        # Thêm đường dẫn stdlib vào sys.path nếu chưa có
        stdlib_path = os.path.join(os.path.dirname(__file__))
        if stdlib_path not in sys.path:
            sys.path.insert(0, stdlib_path)
        
        # Import module
        module = __import__(ten_module)
        return module
    except ImportError as e:
        raise ImportError(f"Không thể import module '{ten_module}': {e}")

def nhap_tu_module(ten_module, ten_ham):
    """Import hàm cụ thể từ module"""
    try:
        # Thêm đường dẫn stdlib vào sys.path nếu chưa có
        stdlib_path = os.path.join(os.path.dirname(__file__))
        if stdlib_path not in sys.path:
            sys.path.insert(0, stdlib_path)
        
        # Import module và lấy hàm
        module = __import__(ten_module)
        if hasattr(module, ten_ham):
            return getattr(module, ten_ham)
        else:
            raise AttributeError(f"Module '{ten_module}' không có hàm '{ten_ham}'")
    except ImportError as e:
        raise ImportError(f"Không thể import từ module '{ten_module}': {e}")

def liet_ke_ham_module(ten_module):
    """Liệt kê các hàm trong module"""
    try:
        module = nhap_module(ten_module)
        return [name for name in dir(module) if not name.startswith('_')]
    except ImportError as e:
        raise ImportError(f"Không thể import module '{ten_module}': {e}")

# Hằng số logic
dung_vay = True
sai_vay = False

# Từ điển chứa tất cả các hàm built-in
BUILTIN_FUNCTIONS = {
    'in_ra': in_ra,
    'nhap_vao': nhap_vao,
    'do_dai': do_dai,
    'kieu': kieu,
    'chuyen_so': chuyen_so,
    'chuyen_van_ban': chuyen_van_ban,
    'chuyen_so_nguyen': chuyen_so_nguyen,
    'chuyen_so_thuc': chuyen_so_thuc,
    'pham_vi': pham_vi,
    'sap_xep': sap_xep,
    'dao_nguoc': dao_nguoc,
    'tong': tong,
    'nho_nhat': nho_nhat,
    'lon_nhat': lon_nhat,
    'tat_ca': tat_ca,
    'bat_ky': bat_ky,
    'dem': dem,
    'tim_vi_tri': tim_vi_tri,
    'la_so': la_so,
    'la_chuoi': la_chuoi,
    'la_danh_sach': la_danh_sach,
    'la_tu_dien': la_tu_dien,
    'nhap_module': nhap_module,
    'nhap_tu_module': nhap_tu_module,
    'liet_ke_ham_module': liet_ke_ham_module,
    'dung_vay': dung_vay,
    'sai_vay': sai_vay,
}


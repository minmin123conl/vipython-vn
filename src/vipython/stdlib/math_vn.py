"""
Module toán học cho ViPython-VN
"""

import math

# Hằng số toán học
PI = math.pi
E = math.e
TAU = math.tau

# Hàm lượng giác
def sin(x):
    """Hàm sin"""
    return math.sin(x)

def cos(x):
    """Hàm cos"""
    return math.cos(x)

def tan(x):
    """Hàm tan"""
    return math.tan(x)

def asin(x):
    """Hàm arcsin"""
    return math.asin(x)

def acos(x):
    """Hàm arccos"""
    return math.acos(x)

def atan(x):
    """Hàm arctan"""
    return math.atan(x)

def atan2(y, x):
    """Hàm arctan2"""
    return math.atan2(y, x)

# Hàm logarit và mũ
def log(x, base=math.e):
    """Hàm logarit"""
    if base == math.e:
        return math.log(x)
    else:
        return math.log(x, base)

def log10(x):
    """Hàm logarit cơ số 10"""
    return math.log10(x)

def log2(x):
    """Hàm logarit cơ số 2"""
    return math.log2(x)

def exp(x):
    """Hàm e^x"""
    return math.exp(x)

def pow(x, y):
    """Hàm luy thừa"""
    return math.pow(x, y)

def sqrt(x):
    """Hàm căn bậc hai"""
    return math.sqrt(x)

def cbrt(x):
    """Hàm căn bậc ba"""
    return x ** (1/3)

# Hàm làm tròn
def lam_tron(x):
    """Làm tròn số"""
    return round(x)

def lam_tron_len(x):
    """Làm tròn lên (ceiling)"""
    return math.ceil(x)

def lam_tron_xuong(x):
    """Làm tròn xuống (floor)"""
    return math.floor(x)

def cat_phan_thap_phan(x):
    """Cắt phần thập phân (truncate)"""
    return math.trunc(x)

# Hàm giá trị tuyệt đối và dấu
def gia_tri_tuyet_doi(x):
    """Giá trị tuyệt đối"""
    return abs(x)

def dau(x):
    """Trả về dấu của số (-1, 0, 1)"""
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

# Hàm min/max
def nho_nhat(*args):
    """Tìm giá trị nhỏ nhất"""
    if len(args) == 1 and hasattr(args[0], '__iter__'):
        return min(args[0])
    return min(args)

def lon_nhat(*args):
    """Tìm giá trị lớn nhất"""
    if len(args) == 1 and hasattr(args[0], '__iter__'):
        return max(args[0])
    return max(args)

# Hàm kiểm tra
def la_so_nguyen(x):
    """Kiểm tra có phải số nguyên không"""
    return isinstance(x, int) or (isinstance(x, float) and x.is_integer())

def la_so_thuc(x):
    """Kiểm tra có phải số thực không"""
    return isinstance(x, (int, float))

def la_vo_cuc(x):
    """Kiểm tra có phải vô cực không"""
    return math.isinf(x)

def la_nan(x):
    """Kiểm tra có phải NaN không"""
    return math.isnan(x)

# Hàm chuyển đổi góc
def do_sang_radian(degrees):
    """Chuyển độ sang radian"""
    return math.radians(degrees)

def radian_sang_do(radians):
    """Chuyển radian sang độ"""
    return math.degrees(radians)

# Hàm tổ hợp và chỉnh hợp
def giai_thua(n):
    """Tính giai thừa"""
    if n < 0:
        raise ValueError("Giai thừa không xác định cho số âm")
    return math.factorial(n)

def to_hop(n, k):
    """Tính tổ hợp C(n,k)"""
    if k > n or k < 0:
        return 0
    return math.comb(n, k)

def chinh_hop(n, k):
    """Tính chỉnh hợp P(n,k)"""
    if k > n or k < 0:
        return 0
    return math.perm(n, k)

# Hàm thống kê cơ bản
def trung_binh(*args):
    """Tính trung bình cộng"""
    if len(args) == 1 and hasattr(args[0], '__iter__'):
        data = list(args[0])
    else:
        data = list(args)
    
    if not data:
        raise ValueError("Không thể tính trung bình của danh sách rỗng")
    
    return sum(data) / len(data)

def trung_vi(data):
    """Tính trung vị"""
    sorted_data = sorted(data)
    n = len(sorted_data)
    
    if n == 0:
        raise ValueError("Không thể tính trung vị của danh sách rỗng")
    
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2

def phuong_sai(data):
    """Tính phương sai"""
    if len(data) < 2:
        raise ValueError("Cần ít nhất 2 giá trị để tính phương sai")
    
    mean = trung_binh(data)
    return sum((x - mean) ** 2 for x in data) / (len(data) - 1)

def do_lech_chuan(data):
    """Tính độ lệch chuẩn"""
    return sqrt(phuong_sai(data))


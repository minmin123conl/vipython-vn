"""
Module xử lý chuỗi cho ViPython-VN
"""

import re
import unicodedata

def do_dai(chuoi):
    """Trả về độ dài chuỗi"""
    return len(chuoi)

def viet_hoa(chuoi):
    """Chuyển chuỗi thành chữ hoa"""
    return chuoi.upper()

def viet_thuong(chuoi):
    """Chuyển chuỗi thành chữ thường"""
    return chuoi.lower()

def viet_hoa_chu_dau(chuoi):
    """Viết hoa chữ cái đầu"""
    return chuoi.capitalize()

def viet_hoa_tung_tu(chuoi):
    """Viết hoa chữ cái đầu mỗi từ"""
    return chuoi.title()

def cat_khoang_trang(chuoi):
    """Cắt khoảng trắng đầu và cuối"""
    return chuoi.strip()

def cat_khoang_trang_trai(chuoi):
    """Cắt khoảng trắng bên trái"""
    return chuoi.lstrip()

def cat_khoang_trang_phai(chuoi):
    """Cắt khoảng trắng bên phải"""
    return chuoi.rstrip()

def thay_the(chuoi, cu, moi, so_lan=-1):
    """Thay thế chuỗi con"""
    if so_lan == -1:
        return chuoi.replace(cu, moi)
    else:
        return chuoi.replace(cu, moi, so_lan)

def tach_chuoi(chuoi, phan_cach=None, so_lan=-1):
    """Tách chuỗi thành danh sách"""
    if phan_cach is None:
        return chuoi.split()
    elif so_lan == -1:
        return chuoi.split(phan_cach)
    else:
        return chuoi.split(phan_cach, so_lan)

def noi_chuoi(danh_sach, phan_cach=""):
    """Nối danh sách thành chuỗi"""
    return phan_cach.join(str(item) for item in danh_sach)

def bat_dau_bang(chuoi, tien_to):
    """Kiểm tra chuỗi có bắt đầu bằng tiền tố không"""
    return chuoi.startswith(tien_to)

def ket_thuc_bang(chuoi, hau_to):
    """Kiểm tra chuỗi có kết thúc bằng hậu tố không"""
    return chuoi.endswith(hau_to)

def chua(chuoi, chuoi_con):
    """Kiểm tra chuỗi có chứa chuỗi con không"""
    return chuoi_con in chuoi

def tim_vi_tri(chuoi, chuoi_con, bat_dau=0):
    """Tìm vị trí đầu tiên của chuỗi con"""
    try:
        return chuoi.index(chuoi_con, bat_dau)
    except ValueError:
        return -1

def tim_vi_tri_cuoi(chuoi, chuoi_con):
    """Tìm vị trí cuối cùng của chuỗi con"""
    try:
        return chuoi.rindex(chuoi_con)
    except ValueError:
        return -1

def dem_so_lan(chuoi, chuoi_con):
    """Đếm số lần xuất hiện của chuỗi con"""
    return chuoi.count(chuoi_con)

def la_chu_so(chuoi):
    """Kiểm tra chuỗi có phải toàn chữ số không"""
    return chuoi.isdigit()

def la_chu_cai(chuoi):
    """Kiểm tra chuỗi có phải toàn chữ cái không"""
    return chuoi.isalpha()

def la_chu_cai_so(chuoi):
    """Kiểm tra chuỗi có phải toàn chữ cái và số không"""
    return chuoi.isalnum()

def la_khoang_trang(chuoi):
    """Kiểm tra chuỗi có phải toàn khoảng trắng không"""
    return chuoi.isspace()

def la_chu_hoa(chuoi):
    """Kiểm tra chuỗi có phải toàn chữ hoa không"""
    return chuoi.isupper()

def la_chu_thuong(chuoi):
    """Kiểm tra chuỗi có phải toàn chữ thường không"""
    return chuoi.islower()

def dao_nguoc(chuoi):
    """Đảo ngược chuỗi"""
    return chuoi[::-1]

def lap_lai(chuoi, so_lan):
    """Lặp lại chuỗi n lần"""
    return chuoi * so_lan

def chen_vao(chuoi, vi_tri, chuoi_chen):
    """Chèn chuỗi vào vị trí chỉ định"""
    return chuoi[:vi_tri] + chuoi_chen + chuoi[vi_tri:]

def xoa_tai_vi_tri(chuoi, vi_tri, so_ky_tu=1):
    """Xóa ký tự tại vị trí chỉ định"""
    return chuoi[:vi_tri] + chuoi[vi_tri + so_ky_tu:]

def cat_chuoi(chuoi, bat_dau, ket_thuc=None):
    """Cắt chuỗi từ vị trí bắt đầu đến kết thúc"""
    if ket_thuc is None:
        return chuoi[bat_dau:]
    return chuoi[bat_dau:ket_thuc]

def chen_khoang_trang(chuoi, do_rong, ky_tu_chen=' ', canh_le='trai'):
    """Chèn khoảng trắng để đạt độ rộng mong muốn"""
    if canh_le == 'trai':
        return chuoi.ljust(do_rong, ky_tu_chen)
    elif canh_le == 'phai':
        return chuoi.rjust(do_rong, ky_tu_chen)
    else:  # giua
        return chuoi.center(do_rong, ky_tu_chen)

def ma_hoa_base64(chuoi):
    """Mã hóa chuỗi thành base64"""
    import base64
    return base64.b64encode(chuoi.encode('utf-8')).decode('ascii')

def giai_ma_base64(chuoi_ma_hoa):
    """Giải mã chuỗi base64"""
    import base64
    return base64.b64decode(chuoi_ma_hoa.encode('ascii')).decode('utf-8')

def bo_dau(chuoi):
    """Bỏ dấu tiếng Việt"""
    # Chuẩn hóa Unicode
    chuoi = unicodedata.normalize('NFD', chuoi)
    # Loại bỏ các ký tự dấu
    chuoi = ''.join(c for c in chuoi if unicodedata.category(c) != 'Mn')
    return chuoi

def tim_kiem_regex(chuoi, mau, co_phan_biet_hoa_thuong=True):
    """Tìm kiếm bằng biểu thức chính quy"""
    flags = 0 if co_phan_biet_hoa_thuong else re.IGNORECASE
    matches = re.findall(mau, chuoi, flags)
    return matches

def thay_the_regex(chuoi, mau, thay_the, so_lan=0):
    """Thay thế bằng biểu thức chính quy"""
    return re.sub(mau, thay_the, chuoi, count=so_lan)

def tach_chuoi_regex(chuoi, mau):
    """Tách chuỗi bằng biểu thức chính quy"""
    return re.split(mau, chuoi)

def kiem_tra_email(email):
    """Kiểm tra định dạng email"""
    mau = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(mau, email))

def kiem_tra_so_dien_thoai(so_dt):
    """Kiểm tra định dạng số điện thoại Việt Nam"""
    # Loại bỏ khoảng trắng và dấu gạch ngang
    so_dt = re.sub(r'[\s-]', '', so_dt)
    
    # Các mẫu số điện thoại Việt Nam
    mau_list = [
        r'^(\+84|84|0)(3|5|7|8|9)[0-9]{8}$',  # Di động
        r'^(\+84|84|0)(2)[0-9]{9}$',          # Cố định
    ]
    
    return any(re.match(mau, so_dt) for mau in mau_list)

def tao_slug(chuoi):
    """Tạo slug từ chuỗi (dùng cho URL)"""
    # Bỏ dấu
    chuoi = bo_dau(chuoi)
    # Chuyển thành chữ thường
    chuoi = chuoi.lower()
    # Thay thế khoảng trắng và ký tự đặc biệt bằng dấu gạch ngang
    chuoi = re.sub(r'[^a-z0-9]+', '-', chuoi)
    # Loại bỏ dấu gạch ngang ở đầu và cuối
    chuoi = chuoi.strip('-')
    return chuoi

def dinh_dang_so(so, so_chu_so_thap_phan=2, phan_cach_hang_nghin=','):
    """Định dạng số với dấu phân cách hàng nghìn"""
    if isinstance(so, int):
        return f"{so:,}".replace(',', phan_cach_hang_nghin)
    else:
        return f"{so:,.{so_chu_so_thap_phan}f}".replace(',', phan_cach_hang_nghin)


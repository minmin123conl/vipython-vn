"""
Module xử lý ngày giờ cho ViPython-VN
"""

import datetime
import time
import calendar

def hom_nay():
    """Lấy ngày hôm nay"""
    return datetime.date.today()

def bay_gio():
    """Lấy thời gian hiện tại"""
    return datetime.datetime.now()

def tao_ngay(nam, thang, ngay):
    """Tạo đối tượng ngày"""
    return datetime.date(nam, thang, ngay)

def tao_gio(gio, phut, giay=0, micro_giay=0):
    """Tạo đối tượng thời gian"""
    return datetime.time(gio, phut, giay, micro_giay)

def tao_ngay_gio(nam, thang, ngay, gio=0, phut=0, giay=0, micro_giay=0):
    """Tạo đối tượng ngày giờ"""
    return datetime.datetime(nam, thang, ngay, gio, phut, giay, micro_giay)

def dinh_dang_ngay(ngay, dinh_dang="%d/%m/%Y"):
    """Định dạng ngày thành chuỗi"""
    return ngay.strftime(dinh_dang)

def dinh_dang_gio(gio, dinh_dang="%H:%M:%S"):
    """Định dạng giờ thành chuỗi"""
    return gio.strftime(dinh_dang)

def dinh_dang_ngay_gio(ngay_gio, dinh_dang="%d/%m/%Y %H:%M:%S"):
    """Định dạng ngày giờ thành chuỗi"""
    return ngay_gio.strftime(dinh_dang)

def phan_tich_ngay(chuoi_ngay, dinh_dang="%d/%m/%Y"):
    """Phân tích chuỗi thành ngày"""
    return datetime.datetime.strptime(chuoi_ngay, dinh_dang).date()

def phan_tich_gio(chuoi_gio, dinh_dang="%H:%M:%S"):
    """Phân tích chuỗi thành giờ"""
    return datetime.datetime.strptime(chuoi_gio, dinh_dang).time()

def phan_tich_ngay_gio(chuoi_ngay_gio, dinh_dang="%d/%m/%Y %H:%M:%S"):
    """Phân tích chuỗi thành ngày giờ"""
    return datetime.datetime.strptime(chuoi_ngay_gio, dinh_dang)

def lay_nam(ngay):
    """Lấy năm từ ngày"""
    return ngay.year

def lay_thang(ngay):
    """Lấy tháng từ ngày"""
    return ngay.month

def lay_ngay(ngay):
    """Lấy ngày từ ngày"""
    return ngay.day

def lay_gio(thoi_gian):
    """Lấy giờ từ thời gian"""
    return thoi_gian.hour

def lay_phut(thoi_gian):
    """Lấy phút từ thời gian"""
    return thoi_gian.minute

def lay_giay(thoi_gian):
    """Lấy giây từ thời gian"""
    return thoi_gian.second

def lay_thu_trong_tuan(ngay):
    """Lấy thứ trong tuần (0=Thứ 2, 6=Chủ nhật)"""
    return ngay.weekday()

def lay_thu_trong_tuan_chu_nhat_dau(ngay):
    """Lấy thứ trong tuần (0=Chủ nhật, 6=Thứ 7)"""
    return ngay.isoweekday() % 7

def ten_thu(ngay):
    """Lấy tên thứ trong tuần"""
    ten_thu_list = [
        "Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", 
        "Thứ Sáu", "Thứ Bảy", "Chủ Nhật"
    ]
    return ten_thu_list[ngay.weekday()]

def ten_thang(thang):
    """Lấy tên tháng"""
    ten_thang_list = [
        "", "Tháng Một", "Tháng Hai", "Tháng Ba", "Tháng Tư",
        "Tháng Năm", "Tháng Sáu", "Tháng Bảy", "Tháng Tám",
        "Tháng Chín", "Tháng Mười", "Tháng Mười Một", "Tháng Mười Hai"
    ]
    return ten_thang_list[thang]

def cong_ngay(ngay, so_ngay):
    """Cộng số ngày vào ngày"""
    return ngay + datetime.timedelta(days=so_ngay)

def cong_tuan(ngay, so_tuan):
    """Cộng số tuần vào ngày"""
    return ngay + datetime.timedelta(weeks=so_tuan)

def cong_thang(ngay, so_thang):
    """Cộng số tháng vào ngày"""
    thang_moi = ngay.month + so_thang
    nam_moi = ngay.year + (thang_moi - 1) // 12
    thang_moi = (thang_moi - 1) % 12 + 1
    
    # Xử lý trường hợp ngày không tồn tại trong tháng mới
    try:
        return ngay.replace(year=nam_moi, month=thang_moi)
    except ValueError:
        # Nếu ngày không tồn tại (ví dụ: 31/1 + 1 tháng), lấy ngày cuối tháng
        ngay_cuoi_thang = calendar.monthrange(nam_moi, thang_moi)[1]
        return ngay.replace(year=nam_moi, month=thang_moi, day=ngay_cuoi_thang)

def cong_nam(ngay, so_nam):
    """Cộng số năm vào ngày"""
    try:
        return ngay.replace(year=ngay.year + so_nam)
    except ValueError:
        # Xử lý trường hợp 29/2 trong năm không nhuận
        return ngay.replace(year=ngay.year + so_nam, day=28)

def tru_ngay(ngay1, ngay2):
    """Tính số ngày giữa hai ngày"""
    return (ngay1 - ngay2).days

def tru_gio(gio1, gio2):
    """Tính số giờ giữa hai thời điểm"""
    delta = gio1 - gio2
    return delta.total_seconds() / 3600

def tru_phut(gio1, gio2):
    """Tính số phút giữa hai thời điểm"""
    delta = gio1 - gio2
    return delta.total_seconds() / 60

def tru_giay(gio1, gio2):
    """Tính số giây giữa hai thời điểm"""
    delta = gio1 - gio2
    return delta.total_seconds()

def la_nam_nhuan(nam):
    """Kiểm tra có phải năm nhuận không"""
    return calendar.isleap(nam)

def so_ngay_trong_thang(nam, thang):
    """Lấy số ngày trong tháng"""
    return calendar.monthrange(nam, thang)[1]

def ngay_dau_thang(nam, thang):
    """Lấy ngày đầu tháng"""
    return datetime.date(nam, thang, 1)

def ngay_cuoi_thang(nam, thang):
    """Lấy ngày cuối tháng"""
    so_ngay = so_ngay_trong_thang(nam, thang)
    return datetime.date(nam, thang, so_ngay)

def ngay_dau_nam(nam):
    """Lấy ngày đầu năm"""
    return datetime.date(nam, 1, 1)

def ngay_cuoi_nam(nam):
    """Lấy ngày cuối năm"""
    return datetime.date(nam, 12, 31)

def timestamp():
    """Lấy timestamp hiện tại"""
    return time.time()

def timestamp_sang_ngay_gio(ts):
    """Chuyển timestamp thành ngày giờ"""
    return datetime.datetime.fromtimestamp(ts)

def ngay_gio_sang_timestamp(ngay_gio):
    """Chuyển ngày giờ thành timestamp"""
    return ngay_gio.timestamp()

def ngu(giay):
    """Tạm dừng chương trình trong số giây"""
    time.sleep(giay)

def do_thoi_gian(ham_thuc_thi):
    """Đo thời gian thực thi hàm"""
    def wrapper(*args, **kwargs):
        bat_dau = time.time()
        ket_qua = ham_thuc_thi(*args, **kwargs)
        ket_thuc = time.time()
        thoi_gian = ket_thuc - bat_dau
        print(f"Thời gian thực thi: {thoi_gian:.4f} giây")
        return ket_qua
    return wrapper

def tuoi(ngay_sinh):
    """Tính tuổi từ ngày sinh"""
    hom_nay_obj = hom_nay()
    tuoi_val = hom_nay_obj.year - ngay_sinh.year
    
    # Kiểm tra xem đã qua sinh nhật chưa
    if (hom_nay_obj.month, hom_nay_obj.day) < (ngay_sinh.month, ngay_sinh.day):
        tuoi_val -= 1
    
    return tuoi_val

def ngay_le_viet_nam(nam):
    """Lấy danh sách ngày lễ Việt Nam trong năm"""
    ngay_le = {
        "Tết Dương lịch": tao_ngay(nam, 1, 1),
        "Giỗ tổ Hùng Vương": tao_ngay(nam, 4, 10),  # Ngày âm lịch, đây là xấp xỉ
        "Ngày Giải phóng miền Nam": tao_ngay(nam, 4, 30),
        "Quốc tế Lao động": tao_ngay(nam, 5, 1),
        "Quốc khánh": tao_ngay(nam, 9, 2),
    }
    return ngay_le

def kiem_tra_ngay_le(ngay, nam=None):
    """Kiểm tra có phải ngày lễ không"""
    if nam is None:
        nam = ngay.year
    
    ngay_le = ngay_le_viet_nam(nam)
    return any(ngay == le for le in ngay_le.values())

def dinh_dang_tieng_viet(ngay_gio):
    """Định dạng ngày giờ theo kiểu Việt Nam"""
    thu = ten_thu(ngay_gio)
    ngay = ngay_gio.day
    thang = ten_thang(ngay_gio.month)
    nam = ngay_gio.year
    gio = ngay_gio.hour
    phut = ngay_gio.minute
    
    return f"{thu}, ngày {ngay} {thang} năm {nam}, {gio:02d}:{phut:02d}"


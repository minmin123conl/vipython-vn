"""
Module xử lý file cho ViPython-VN
"""

import os
import shutil
import json
import csv
from pathlib import Path

def doc_file(duong_dan, ma_hoa='utf-8'):
    """Đọc nội dung file"""
    try:
        with open(duong_dan, 'r', encoding=ma_hoa) as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Không tìm thấy file: {duong_dan}")
    except Exception as e:
        raise Exception(f"Lỗi khi đọc file: {e}")

def doc_dong(duong_dan, ma_hoa='utf-8'):
    """Đọc file thành danh sách các dòng"""
    try:
        with open(duong_dan, 'r', encoding=ma_hoa) as f:
            return f.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"Không tìm thấy file: {duong_dan}")
    except Exception as e:
        raise Exception(f"Lỗi khi đọc file: {e}")

def ghi_file(duong_dan, noi_dung, ma_hoa='utf-8', che_de=True):
    """Ghi nội dung vào file"""
    try:
        mode = 'w' if che_de else 'a'
        with open(duong_dan, mode, encoding=ma_hoa) as f:
            f.write(noi_dung)
        return True
    except Exception as e:
        raise Exception(f"Lỗi khi ghi file: {e}")

def ghi_dong(duong_dan, danh_sach_dong, ma_hoa='utf-8', che_de=True):
    """Ghi danh sách dòng vào file"""
    try:
        mode = 'w' if che_de else 'a'
        with open(duong_dan, mode, encoding=ma_hoa) as f:
            f.writelines(danh_sach_dong)
        return True
    except Exception as e:
        raise Exception(f"Lỗi khi ghi file: {e}")

def them_vao_file(duong_dan, noi_dung, ma_hoa='utf-8'):
    """Thêm nội dung vào cuối file"""
    return ghi_file(duong_dan, noi_dung, ma_hoa, che_de=False)

def ton_tai(duong_dan):
    """Kiểm tra file/thư mục có tồn tại không"""
    return os.path.exists(duong_dan)

def la_file(duong_dan):
    """Kiểm tra có phải file không"""
    return os.path.isfile(duong_dan)

def la_thu_muc(duong_dan):
    """Kiểm tra có phải thư mục không"""
    return os.path.isdir(duong_dan)

def kich_thuoc_file(duong_dan):
    """Lấy kích thước file (bytes)"""
    try:
        return os.path.getsize(duong_dan)
    except FileNotFoundError:
        raise FileNotFoundError(f"Không tìm thấy file: {duong_dan}")

def thoi_gian_sua_doi(duong_dan):
    """Lấy thời gian sửa đổi cuối cùng"""
    try:
        import datetime
        timestamp = os.path.getmtime(duong_dan)
        return datetime.datetime.fromtimestamp(timestamp)
    except FileNotFoundError:
        raise FileNotFoundError(f"Không tìm thấy file: {duong_dan}")

def thoi_gian_tao(duong_dan):
    """Lấy thời gian tạo file"""
    try:
        import datetime
        timestamp = os.path.getctime(duong_dan)
        return datetime.datetime.fromtimestamp(timestamp)
    except FileNotFoundError:
        raise FileNotFoundError(f"Không tìm thấy file: {duong_dan}")

def xoa_file(duong_dan):
    """Xóa file"""
    try:
        os.remove(duong_dan)
        return True
    except FileNotFoundError:
        raise FileNotFoundError(f"Không tìm thấy file: {duong_dan}")
    except Exception as e:
        raise Exception(f"Lỗi khi xóa file: {e}")

def sao_chep_file(nguon, dich):
    """Sao chép file"""
    try:
        shutil.copy2(nguon, dich)
        return True
    except FileNotFoundError:
        raise FileNotFoundError(f"Không tìm thấy file nguồn: {nguon}")
    except Exception as e:
        raise Exception(f"Lỗi khi sao chép file: {e}")

def di_chuyen_file(nguon, dich):
    """Di chuyển/đổi tên file"""
    try:
        shutil.move(nguon, dich)
        return True
    except FileNotFoundError:
        raise FileNotFoundError(f"Không tìm thấy file nguồn: {nguon}")
    except Exception as e:
        raise Exception(f"Lỗi khi di chuyển file: {e}")

def tao_thu_muc(duong_dan, tao_cha=True):
    """Tạo thư mục"""
    try:
        if tao_cha:
            os.makedirs(duong_dan, exist_ok=True)
        else:
            os.mkdir(duong_dan)
        return True
    except Exception as e:
        raise Exception(f"Lỗi khi tạo thư mục: {e}")

def xoa_thu_muc(duong_dan, xoa_tat_ca=False):
    """Xóa thư mục"""
    try:
        if xoa_tat_ca:
            shutil.rmtree(duong_dan)
        else:
            os.rmdir(duong_dan)
        return True
    except FileNotFoundError:
        raise FileNotFoundError(f"Không tìm thấy thư mục: {duong_dan}")
    except OSError as e:
        if "not empty" in str(e).lower():
            raise Exception(f"Thư mục không rỗng: {duong_dan}")
        raise Exception(f"Lỗi khi xóa thư mục: {e}")

def liet_ke_file(duong_dan, bao_gom_thu_muc=True, bao_gom_file=True):
    """Liệt kê file và thư mục"""
    try:
        ket_qua = []
        for item in os.listdir(duong_dan):
            duong_dan_day_du = os.path.join(duong_dan, item)
            if os.path.isfile(duong_dan_day_du) and bao_gom_file:
                ket_qua.append(item)
            elif os.path.isdir(duong_dan_day_du) and bao_gom_thu_muc:
                ket_qua.append(item)
        return ket_qua
    except FileNotFoundError:
        raise FileNotFoundError(f"Không tìm thấy thư mục: {duong_dan}")

def tim_file(thu_muc, ten_file, de_quy=True):
    """Tìm file theo tên"""
    ket_qua = []
    
    if de_quy:
        for root, dirs, files in os.walk(thu_muc):
            for file in files:
                if ten_file in file:
                    ket_qua.append(os.path.join(root, file))
    else:
        try:
            for item in os.listdir(thu_muc):
                if ten_file in item and os.path.isfile(os.path.join(thu_muc, item)):
                    ket_qua.append(os.path.join(thu_muc, item))
        except FileNotFoundError:
            raise FileNotFoundError(f"Không tìm thấy thư mục: {thu_muc}")
    
    return ket_qua

def lay_ten_file(duong_dan):
    """Lấy tên file từ đường dẫn"""
    return os.path.basename(duong_dan)

def lay_thu_muc_cha(duong_dan):
    """Lấy thư mục chứa file"""
    return os.path.dirname(duong_dan)

def lay_phan_mo_rong(duong_dan):
    """Lấy phần mở rộng file"""
    return os.path.splitext(duong_dan)[1]

def lay_ten_khong_mo_rong(duong_dan):
    """Lấy tên file không có phần mở rộng"""
    return os.path.splitext(os.path.basename(duong_dan))[0]

def duong_dan_tuyet_doi(duong_dan):
    """Chuyển đường dẫn tương đối thành tuyệt đối"""
    return os.path.abspath(duong_dan)

def noi_duong_dan(*args):
    """Nối các phần đường dẫn"""
    return os.path.join(*args)

def thu_muc_hien_tai():
    """Lấy thư mục hiện tại"""
    return os.getcwd()

def doi_thu_muc(duong_dan):
    """Đổi thư mục làm việc"""
    try:
        os.chdir(duong_dan)
        return True
    except FileNotFoundError:
        raise FileNotFoundError(f"Không tìm thấy thư mục: {duong_dan}")

def doc_json(duong_dan, ma_hoa='utf-8'):
    """Đọc file JSON"""
    try:
        with open(duong_dan, 'r', encoding=ma_hoa) as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Không tìm thấy file: {duong_dan}")
    except json.JSONDecodeError as e:
        raise Exception(f"Lỗi định dạng JSON: {e}")

def ghi_json(duong_dan, du_lieu, ma_hoa='utf-8', thut_le=2):
    """Ghi dữ liệu ra file JSON"""
    try:
        with open(duong_dan, 'w', encoding=ma_hoa) as f:
            json.dump(du_lieu, f, ensure_ascii=False, indent=thut_le)
        return True
    except Exception as e:
        raise Exception(f"Lỗi khi ghi file JSON: {e}")

def doc_csv(duong_dan, co_tieu_de=True, ma_hoa='utf-8'):
    """Đọc file CSV"""
    try:
        with open(duong_dan, 'r', encoding=ma_hoa, newline='') as f:
            reader = csv.reader(f)
            du_lieu = list(reader)
            
            if co_tieu_de and du_lieu:
                tieu_de = du_lieu[0]
                hang = du_lieu[1:]
                return {'tieu_de': tieu_de, 'du_lieu': hang}
            else:
                return {'tieu_de': None, 'du_lieu': du_lieu}
    except FileNotFoundError:
        raise FileNotFoundError(f"Không tìm thấy file: {duong_dan}")

def ghi_csv(duong_dan, du_lieu, tieu_de=None, ma_hoa='utf-8'):
    """Ghi dữ liệu ra file CSV"""
    try:
        with open(duong_dan, 'w', encoding=ma_hoa, newline='') as f:
            writer = csv.writer(f)
            
            if tieu_de:
                writer.writerow(tieu_de)
            
            if isinstance(du_lieu[0], dict) and tieu_de:
                # Ghi từ dictionary
                for hang in du_lieu:
                    writer.writerow([hang.get(cot, '') for cot in tieu_de])
            else:
                # Ghi từ list
                writer.writerows(du_lieu)
        return True
    except Exception as e:
        raise Exception(f"Lỗi khi ghi file CSV: {e}")

def nen_file(duong_dan_nguon, duong_dan_nen):
    """Nén file/thư mục thành zip"""
    try:
        shutil.make_archive(duong_dan_nen.replace('.zip', ''), 'zip', duong_dan_nguon)
        return True
    except Exception as e:
        raise Exception(f"Lỗi khi nén file: {e}")

def giai_nen_file(duong_dan_nen, thu_muc_dich):
    """Giải nén file zip"""
    try:
        shutil.unpack_archive(duong_dan_nen, thu_muc_dich)
        return True
    except Exception as e:
        raise Exception(f"Lỗi khi giải nén file: {e}")

def dung_luong_thu_muc(duong_dan):
    """Tính dung lượng thư mục"""
    tong_dung_luong = 0
    for dirpath, dirnames, filenames in os.walk(duong_dan):
        for filename in filenames:
            duong_dan_file = os.path.join(dirpath, filename)
            try:
                tong_dung_luong += os.path.getsize(duong_dan_file)
            except (OSError, FileNotFoundError):
                pass
    return tong_dung_luong

def dinh_dang_dung_luong(bytes_size):
    """Định dạng dung lượng file"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_size < 1024.0:
            return f"{bytes_size:.1f} {unit}"
        bytes_size /= 1024.0
    return f"{bytes_size:.1f} PB"


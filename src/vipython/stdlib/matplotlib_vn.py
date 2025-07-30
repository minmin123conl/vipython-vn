"""
Wrapper cho Matplotlib với tên hàm tiếng Việt
"""

try:
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False
    plt = None
    patches = None

def kiem_tra_matplotlib():
    """Kiểm tra matplotlib có sẵn không"""
    if not MATPLOTLIB_AVAILABLE:
        raise ImportError("Matplotlib chưa được cài đặt. Chạy: pip install matplotlib")

# ===== TẠO BIỂU ĐỒ =====

def tao_hinh():
    """Tạo figure mới"""
    kiem_tra_matplotlib()
    return plt.figure()

def tao_hinh_va_truc(so_hang=1, so_cot=1, kich_thuoc=(8, 6)):
    """Tạo figure và axes"""
    kiem_tra_matplotlib()
    return plt.subplots(so_hang, so_cot, figsize=kich_thuoc)

def ve_duong(x, y, mau='blue', do_day=1, kieu_duong='-', nhan=''):
    """Vẽ đường thẳng"""
    kiem_tra_matplotlib()
    return plt.plot(x, y, color=mau, linewidth=do_day, linestyle=kieu_duong, label=nhan)

def ve_diem(x, y, mau='red', kich_thuoc=20, kieu_diem='o', nhan=''):
    """Vẽ điểm"""
    kiem_tra_matplotlib()
    return plt.scatter(x, y, color=mau, s=kich_thuoc, marker=kieu_diem, label=nhan)

def ve_cot(x, chieu_cao, rong=0.8, mau='blue', nhan=''):
    """Vẽ biểu đồ cột"""
    kiem_tra_matplotlib()
    return plt.bar(x, chieu_cao, width=rong, color=mau, label=nhan)

def ve_cot_ngang(y, do_dai, cao=0.8, mau='blue', nhan=''):
    """Vẽ biểu đồ cột ngang"""
    kiem_tra_matplotlib()
    return plt.barh(y, do_dai, height=cao, color=mau, label=nhan)

def ve_histogram(du_lieu, so_bin=10, mau='blue', trong_suot=0.7, nhan=''):
    """Vẽ histogram"""
    kiem_tra_matplotlib()
    return plt.hist(du_lieu, bins=so_bin, color=mau, alpha=trong_suot, label=nhan)

def ve_tron(nhan, kich_thuoc, mau=None, bat_dau_goc=90, phat_no=None):
    """Vẽ biểu đồ tròn"""
    kiem_tra_matplotlib()
    return plt.pie(kich_thuoc, labels=nhan, colors=mau, startangle=bat_dau_goc, explode=phat_no)

def ve_boxplot(du_lieu, nhan=None):
    """Vẽ biểu đồ hộp"""
    kiem_tra_matplotlib()
    return plt.boxplot(du_lieu, labels=nhan)

def ve_violinplot(du_lieu, vi_tri=None):
    """Vẽ biểu đồ violin"""
    kiem_tra_matplotlib()
    return plt.violinplot(du_lieu, positions=vi_tri)

# ===== ĐỊNH DẠNG BIỂU ĐỒ =====

def dat_tieu_de(tieu_de, kich_thuoc_chu=14, mau='black'):
    """Đặt tiêu đề biểu đồ"""
    kiem_tra_matplotlib()
    plt.title(tieu_de, fontsize=kich_thuoc_chu, color=mau)

def dat_nhan_truc_x(nhan, kich_thuoc_chu=12):
    """Đặt nhãn trục X"""
    kiem_tra_matplotlib()
    plt.xlabel(nhan, fontsize=kich_thuoc_chu)

def dat_nhan_truc_y(nhan, kich_thuoc_chu=12):
    """Đặt nhãn trục Y"""
    kiem_tra_matplotlib()
    plt.ylabel(nhan, fontsize=kich_thuoc_chu)

def dat_gioi_han_x(min_val, max_val):
    """Đặt giới hạn trục X"""
    kiem_tra_matplotlib()
    plt.xlim(min_val, max_val)

def dat_gioi_han_y(min_val, max_val):
    """Đặt giới hạn trục Y"""
    kiem_tra_matplotlib()
    plt.ylim(min_val, max_val)

def dat_vi_tri_x(vi_tri, nhan=None):
    """Đặt vị trí và nhãn cho trục X"""
    kiem_tra_matplotlib()
    plt.xticks(vi_tri, nhan)

def dat_vi_tri_y(vi_tri, nhan=None):
    """Đặt vị trí và nhãn cho trục Y"""
    kiem_tra_matplotlib()
    plt.yticks(vi_tri, nhan)

def hien_luoi(hien=True, mau='gray', trong_suot=0.3):
    """Hiển thị lưới"""
    kiem_tra_matplotlib()
    plt.grid(hien, color=mau, alpha=trong_suot)

def hien_chu_thich(vi_tri='best'):
    """Hiển thị chú thích"""
    kiem_tra_matplotlib()
    plt.legend(loc=vi_tri)

def dat_mau_nen(mau='white'):
    """Đặt màu nền"""
    kiem_tra_matplotlib()
    plt.gca().set_facecolor(mau)

# ===== HIỂN THỊ VÀ LUU =====

def hien_thi():
    """Hiển thị biểu đồ"""
    kiem_tra_matplotlib()
    plt.show()

def luu_hinh(ten_file, dpi=300, dinh_dang='png'):
    """Lưu biểu đồ ra file"""
    kiem_tra_matplotlib()
    plt.savefig(ten_file, dpi=dpi, format=dinh_dang, bbox_inches='tight')

def xoa_hinh():
    """Xóa biểu đồ hiện tại"""
    kiem_tra_matplotlib()
    plt.clf()

def xoa_tat_ca():
    """Xóa tất cả biểu đồ"""
    kiem_tra_matplotlib()
    plt.close('all')

# ===== BIỂU ĐỒ NÂNG CAO =====

def ve_duong_contour(X, Y, Z, muc=10, mau='viridis'):
    """Vẽ đường contour"""
    kiem_tra_matplotlib()
    return plt.contour(X, Y, Z, levels=muc, cmap=mau)

def ve_mat_contour(X, Y, Z, muc=10, mau='viridis'):
    """Vẽ mặt contour"""
    kiem_tra_matplotlib()
    return plt.contourf(X, Y, Z, levels=muc, cmap=mau)

def ve_anh(anh, mau='gray', goc_toa_do='upper'):
    """Vẽ ảnh"""
    kiem_tra_matplotlib()
    return plt.imshow(anh, cmap=mau, origin=goc_toa_do)

def ve_thanh_mau(nhan=''):
    """Vẽ thanh màu"""
    kiem_tra_matplotlib()
    return plt.colorbar(label=nhan)

def ve_duong_loi(x, y, mau='black', trong_suot=0.5):
    """Vẽ đường lưới"""
    kiem_tra_matplotlib()
    return plt.plot(x, y, color=mau, alpha=trong_suot)

# ===== HÌNH HỌC =====

def ve_hinh_chu_nhat(x, y, rong, cao, mau='blue', trong_suot=0.3):
    """Vẽ hình chữ nhật"""
    kiem_tra_matplotlib()
    rect = patches.Rectangle((x, y), rong, cao, facecolor=mau, alpha=trong_suot)
    plt.gca().add_patch(rect)
    return rect

def ve_hinh_tron(x, y, ban_kinh, mau='red', trong_suot=0.3):
    """Vẽ hình tròn"""
    kiem_tra_matplotlib()
    circle = patches.Circle((x, y), ban_kinh, facecolor=mau, alpha=trong_suot)
    plt.gca().add_patch(circle)
    return circle

def ve_hinh_elip(x, y, rong, cao, mau='green', trong_suot=0.3):
    """Vẽ hình elip"""
    kiem_tra_matplotlib()
    ellipse = patches.Ellipse((x, y), rong, cao, facecolor=mau, alpha=trong_suot)
    plt.gca().add_patch(ellipse)
    return ellipse

def ve_mui_ten(x_bat_dau, y_bat_dau, dx, dy, mau='black', do_day=1):
    """Vẽ mũi tên"""
    kiem_tra_matplotlib()
    return plt.arrow(x_bat_dau, y_bat_dau, dx, dy, color=mau, linewidth=do_day)

def ve_van_ban(x, y, van_ban, kich_thuoc_chu=12, mau='black'):
    """Vẽ văn bản"""
    kiem_tra_matplotlib()
    return plt.text(x, y, van_ban, fontsize=kich_thuoc_chu, color=mau)

# ===== BIỂU ĐỒ 3D =====

def tao_truc_3d():
    """Tạo trục 3D"""
    kiem_tra_matplotlib()
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure()
    return fig.add_subplot(111, projection='3d')

def ve_duong_3d(ax, x, y, z, mau='blue', do_day=1):
    """Vẽ đường 3D"""
    kiem_tra_matplotlib()
    return ax.plot(x, y, z, color=mau, linewidth=do_day)

def ve_diem_3d(ax, x, y, z, mau='red', kich_thuoc=20):
    """Vẽ điểm 3D"""
    kiem_tra_matplotlib()
    return ax.scatter(x, y, z, color=mau, s=kich_thuoc)

def ve_mat_3d(ax, X, Y, Z, mau='viridis', trong_suot=0.8):
    """Vẽ mặt 3D"""
    kiem_tra_matplotlib()
    return ax.plot_surface(X, Y, Z, cmap=mau, alpha=trong_suot)

# ===== TIỆN ÍCH =====

def dat_kich_thuoc_hinh(rong, cao):
    """Đặt kích thước hình"""
    kiem_tra_matplotlib()
    plt.figure(figsize=(rong, cao))

def dat_khoang_cach_subplot(trai=0.1, duoi=0.1, phai=0.9, tren=0.9, khoang_cach_rong=0.2, khoang_cach_cao=0.2):
    """Đặt khoảng cách giữa các subplot"""
    kiem_tra_matplotlib()
    plt.subplots_adjust(left=trai, bottom=duoi, right=phai, top=tren, 
                       wspace=khoang_cach_rong, hspace=khoang_cach_cao)

def dat_style(ten_style='default'):
    """Đặt style cho biểu đồ"""
    kiem_tra_matplotlib()
    plt.style.use(ten_style)

def lay_danh_sach_style():
    """Lấy danh sách các style có sẵn"""
    kiem_tra_matplotlib()
    return plt.style.available

def dat_font_tieng_viet():
    """Đặt font hỗ trợ tiếng Việt"""
    kiem_tra_matplotlib()
    plt.rcParams['font.family'] = ['DejaVu Sans', 'Arial Unicode MS', 'sans-serif']
    plt.rcParams['axes.unicode_minus'] = False

# ===== MẪU BIỂU ĐỒ =====

def bieu_do_duong_don_gian(x, y, tieu_de='Biểu đồ đường', nhan_x='X', nhan_y='Y'):
    """Tạo biểu đồ đường đơn giản"""
    kiem_tra_matplotlib()
    plt.figure(figsize=(10, 6))
    ve_duong(x, y, mau='blue', do_day=2)
    dat_tieu_de(tieu_de)
    dat_nhan_truc_x(nhan_x)
    dat_nhan_truc_y(nhan_y)
    hien_luoi(True)
    hien_thi()

def bieu_do_cot_don_gian(nhan, gia_tri, tieu_de='Biểu đồ cột', nhan_x='Danh mục', nhan_y='Giá trị'):
    """Tạo biểu đồ cột đơn giản"""
    kiem_tra_matplotlib()
    plt.figure(figsize=(10, 6))
    ve_cot(range(len(nhan)), gia_tri, mau='skyblue')
    dat_tieu_de(tieu_de)
    dat_nhan_truc_x(nhan_x)
    dat_nhan_truc_y(nhan_y)
    dat_vi_tri_x(range(len(nhan)), nhan)
    hien_luoi(True, 'y')
    hien_thi()

def bieu_do_tron_don_gian(nhan, gia_tri, tieu_de='Biểu đồ tròn'):
    """Tạo biểu đồ tròn đơn giản"""
    kiem_tra_matplotlib()
    plt.figure(figsize=(8, 8))
    ve_tron(nhan, gia_tri, bat_dau_goc=90)
    dat_tieu_de(tieu_de)
    plt.axis('equal')
    hien_thi()


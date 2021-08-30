from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


# -----------Text Choices-----------
class Sex(models.TextChoices):
    __empty__ = _('Yêu cầu về giới tính người dạy')
    MALE = 'Nam', _('Nam')
    FEMALE = 'Nữ', _('Nữ')
    BOTH = 'Khác', _('Khác')


class Districts(models.TextChoices):
    __empty__ = _('Quận/Huyện')
    District_1 = 'Quận 1', _('Quận 1')
    District_2 = 'Quận 2', _('Quận 2')
    District_3 = 'Quận 3', _('Quận 3')
    District_4 = 'Quận 4', _('Quận 4')

    District_5 = 'Quận 5', _('Quận 5')
    District_6 = 'Quận 6', _('Quận 6')
    District_7 = 'Quận 7', _('Quận 7')
    District_8 = 'Quận 8', _('Quận 8')
    District_9 = 'Quận 9', _('Quận 9')

    District_10 = 'Quận 10', _('Quận 10')
    District_11 = 'Quận 11', _('Quận 11')
    District_12 = 'Quận 12', _('Quận 12')
    BinhChanh_District = 'Bình Chánh', _('Bình Chánh')

    BinhTan_District = 'BTan', _('Bình Tân')
    BinhThanh_District = 'BThanh', _('Bình Thạnh')
    CanGio_District = 'CG', _('Cần Giờ ')
    CuChi_District = 'CC', _('Củ Chi')

    HocMon_District = 'HM', _('Hóc Môn')
    NhaBe_District = 'NB', _('Nhà Bè')
    PhuNhuan_District = 'PN', _('Phú Nhuận')
    TanPhu_District = 'TP', _('Tân Phú')

    TanBinh_District = 'TB', _('Tân Bình')
    ThuDuc_District = 'TD', _('Thủ Đức')


class StudentLevel(models.TextChoices):
    __empty__ = _('Chương trình học mong muốn')
    TIEUHOC = 'tieuhoc', _('Chương trình Tiểu học')
    THCS = 'thcs', _('Chương trình Trung Học Cơ Sở')
    THPT = 'thpt', _('Chương trình Trung Học Phổ Thông')

    CT_QUOCTE = 'ct_quocte', _('Chương trình Quốc Tế')
    # Giang day
    GD_TIENGANH = 'gd_tienganh', _('DẠY BẰNG TIẾNG ANH CÁC MÔN TOÁN-LÝ-HÓA ')
    GD_CANBAN = 'gd_canban', _('DẠY CĂN BẢN CÁC MÔN TOÁN-LÝ-HÓA')

    LT_SAT = 'lt_sat', _('LUYỆN THI SAT')
    LT_TRANDAINGHIA = 'lt_trandainghia', _('LUYỆN THI VÀO LỚP 6 TRẦN ĐẠI NGHĨA')
    LT_LOP10 = 'lt_lop10', _('LUYỆN THI VÀO LỚP 10 TRƯỜNG CHUYÊN / CÔNG LẬP')
    LT_DAIHOC = 'lt_daihoc', _('LUYỆN THI ĐẠI HỌC')

    IELTS = 'ielts', _('IELTS Cơ bản')

    KHAC = 'khac', _('Khác')


# -----------END Text Choices-----------


# -----------Model-----------

class ClassInfo(models.Model):
    class_id = models.AutoField(primary_key=True)
    name = models.CharField('Họ và tên', max_length=100, blank=False)
    phone_number = models.CharField('Số điện thoại', max_length=12, blank=False, default='')
    email = models.EmailField('Địa chỉ Email', max_length=254, blank=True, default='')
    district = models.CharField('Tên quận', max_length=10, choices=Districts.choices, blank=False)
    address = models.CharField('Địa chỉ', max_length=200, blank=True, default='')
    subjects = models.CharField('Môn học', max_length=100, blank=True, default='')
    student_info = models.CharField('Thông tin học sinh', default='', blank = True , max_length=255)
    num_student = models.PositiveIntegerField('Số lượng học sinh', blank=True, default=0, null=True)
    date_start = models.DateField('Ngày khai giảng', blank=True, null=True, default='')
    lop = models.CharField('Lớp', max_length=10, default='')
    #level = models.CharField('Level', max_length=26, choices=StudentLevel.choices)
    fee_expected = models.IntegerField('Mức lương', blank=True, default=0, null=True)
    frequency = models.PositiveIntegerField('Số buổi/Tuần', default=2, blank=True, null=True)
    teaching_time = models.CharField('Thời gian dạy', max_length=500, blank=True, help_text='VD: Tối 2-4-6, 18h',
                                     default='')
    sex_require = models.CharField('Yêu cầu về giới tính', max_length=10, choices=Sex.choices)
    # ----- after this line,add more field must require option default
    note = models.TextField('Ghi chú', default='', blank=True)
    status = models.BooleanField('Trạng Thái lớp', default=False , help_text=('Đang dạy(tick)/Ngưng dạy(untick)'))
    confirmed = models.BooleanField('Đã xác nhận', default=False, help_text=('Đã xác nhận với phụ huynh ? '))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.phone_number} - {self.district} - {self.status}'

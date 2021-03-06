# Generated by Django 3.2.3 on 2021-06-07 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassInfo',
            fields=[
                ('class_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Họ và tên')),
                ('phone_number', models.CharField(default='', max_length=12, verbose_name='Số điện thoại')),
                ('email', models.EmailField(blank=True, default='', max_length=254, verbose_name='Địa chỉ Email')),
                ('district', models.CharField(choices=[(None, 'Quận/Huyện'), ('D1', 'Quận 1'), ('D2', 'Quận 2'), ('D3', 'Quận 3'), ('D4', 'Quận 4'), ('D5', 'Quận 5'), ('D6', 'Quận 6'), ('D7', 'Quận 7'), ('D8', 'Quận 8'), ('D10', 'Quận 10'), ('D11', 'Quận 11'), ('D12', 'Quận 12'), ('BC', 'Bình Chánh'), ('BTan', 'Bình Tân'), ('BThanh', 'Bình Thạnh'), ('CG', 'Cần Giờ '), ('CC', 'Củ Chi'), ('HM', 'Hóc Môn'), ('NB', 'Nhà Bè'), ('PN', 'Phú Nhuận'), ('TP', 'Tân Phú'), ('TB', 'Tân Bình'), ('TD', 'Thủ Đức')], max_length=10, verbose_name='Tên quận')),
                ('address', models.CharField(blank=True, default='', max_length=200, verbose_name='Địa chỉ')),
                ('subjects', models.CharField(blank=True, default='', max_length=100, verbose_name='Môn học')),
                ('num_student', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Số lượng học sinh')),
                ('date_start', models.DateField(blank=True, default='', null=True, verbose_name='Ngày khai giảng')),
                ('level', models.CharField(blank=True, choices=[(None, 'Chương trình học mong muốn'), ('tieuhoc', 'Chương trình Tiểu học'), ('thcs', 'Chương trình Trung Học Cơ Sở'), ('thpt', 'Chương trình Trung Học Phổ Thông'), ('ct_quocte', 'Chương trình Quốc Tế'), ('gd_tienganh', 'DẠY BẰNG TIẾNG ANH CÁC MÔN TOÁN-LÝ-HÓA '), ('gd_canban', 'DẠY CĂN BẢN CÁC MÔN TOÁN-LÝ-HÓA'), ('lt_sat', 'LUYỆN THI SAT'), ('lt_trandainghia', 'LUYỆN THI VÀO LỚP 6 TRẦN ĐẠI NGHĨA'), ('lt_lop10', 'LUYỆN THI VÀO LỚP 10 TRƯỜNG CHUYÊN / CÔNG LẬP'), ('lt_daihoc', 'LUYỆN THI ĐẠI HỌC'), ('ielts', 'IELTS Cơ bản'), ('khac', 'Khác')], default='Chương trình học mong muốn', max_length=20, verbose_name='Lớp')),
                ('fee_expected', models.IntegerField(blank=True, default=0, verbose_name='Mức lương')),
                ('frequency', models.PositiveIntegerField(blank=True, default=2, null=True, verbose_name='Số buổi/Tuần')),
                ('teaching_time', models.CharField(blank=True, default='', help_text='VD: Tối 2-4-6, 18h', max_length=500, verbose_name='Thời gian dạy')),
                ('sex_require', models.CharField(choices=[('male', 'Nam'), ('female', 'Nữ'), ('both', 'Khác')], default='both', max_length=10, verbose_name='Yêu cầu về giới tính')),
                ('note', models.TextField(blank=True, default='', verbose_name='Ghi chú')),
                ('status', models.BooleanField(default=False, verbose_name='Trạng Thái')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

from django.db import models

# Create your models here.
class Users(models.Model):
    """Модель для хранения пользователей"""
    # username
    # email
    # password_hash
    # full_name
    # role_id
    # is_active
    # last_login
    # created_at
    # updated_at

class Roles(models.Model):
    """Модель для хранения ролей"""
    # name
    # description
    # can_scan
    # can_create_profiles
    # can_manage_servers
    # can_manage_users
    # can_view_all_results
    # created_at


class Servers(models.Model):
    """Модель хранит данные о сканируемых серверах"""
    # name
    # host
    # port
    # username
    # auth_type
    # credential_encrypted
    # os_type
    # last_scan_at
    # created_by
    # created_at
    # updated_at
    # is_active

class Profiles(models.Model):
    """"Модель для хранения профилей сканирования"""
    # name
    # description
    # is_system
    # is_base_profile
    # owner_id
    # is_public
    # created_at
    # updated_at


class Checks(models.Model):
    """Модель для хранения проверок безопасности"""

    # Выбор категорий
    CATEGORY_CHOICES = [
        ('kernel', 'Ядро'),
        ('ssh', 'SSH'),
        ('files', 'Файлы'),
        ('grub', 'GRUB'),
        ('pam', 'PAM/Пароли'),
        ('services', 'Сервисы'),
    ]

    # Выбор важности
    IMPORTANCE_CHOICES = [
        ('critical', 'Критический'),
        ('high', 'Высокий'),
        ('medium', 'Средний'),
        ('low', 'Низкий'),
    ]

    code = models.CharField(max_length=10, unique=True, verbose_name="Код")
    category = models.CharField(max_length=10, verbose_name="Категория", choices=CATEGORY_CHOICES)
    # Категории: 'kernel', 'ssh', 'files', 'grub', 'pam', 'services'
    parameter_check = models.CharField(max_length=255, verbose_name="Проверяемый параметр")
    command = models.CharField(max_length=255, verbose_name="Команда")
    expected = models.CharField(max_length=255, verbose_name="Установленное значение")
    description = models.TextField(verbose_name="Описание")
    importance = models.CharField(max_length=10, verbose_name="Важность", choices=IMPORTANCE_CHOICES)
    # 'critical', 'high', 'medium', 'low'

    def __str__(self):
        return f"{self.code} {self.category} {self.parameter_check} - {self.description[:50]}"

class ScanSessions(models.Model):
    """Модель для хранения информации о сессиях сканирования"""
    # server_id
    # profile_id
    # triggered_by
    # status
    # started_at
    # finished_at
    # total_checks
    # passed_count
    # failed_count
    # error_count


class ScanResults(models.Model):
    """Модель для хранения результатов сканирования"""
    # session_id
    # check_category
    # check_id
    # result
    # current_value
    # expected_value_used
    # error_message
    # checked_at

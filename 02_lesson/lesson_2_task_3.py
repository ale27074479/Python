import math


def square(side):
    """Вычисляет площадь квадрата с округлением вверх для нецелых сторон.
    
    Args:
        side (int/float): Длина стороны квадрата.
        
    Returns:
        int: Площадь квадрата (округленная вверх для нецелых сторон).
    """
    area = side * side
    if isinstance(side, float) and not side.is_integer():
        area = math.ceil(area)
    return int(area)


# Примеры вызова функции
print(square(5))  # 25 (целое число → без округления)
print(square(5.0))  # 25 (целое число в float → без округления)
print(square(3.2))  # 11 (3.2 * 3.2 = 10.24 → округляем до 11)
print(square(4.9))  # 25 (4.9 * 4.9 = 24.01 → округляем до 25)


def square_alternative(side):
    """Альтернативная реализация без math.ceil."""
    area = side * side
    if isinstance(side, float) and not side.is_integer():
        area = int(area) + (0 if area.is_integer() else 1)
    return int(area)

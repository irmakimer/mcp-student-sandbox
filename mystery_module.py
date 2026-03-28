"""
Mystery Module - İkinci Derece Denklem Çözücü
Ax² + Bx + C = 0 formundaki denklemlerin köklerini bulur.
"""

import math
from typing import Optional, Tuple


def solve_quadratic_equation(a: float, b: float, c: float) -> Optional[Tuple[float, float]]:
    """
    İkinci derece denklem çözücü (Quadratic Formula).
    
    Ax² + Bx + C = 0 formundaki denklemin köklerini hesaplar.
    
    Args:
        a (float): x² katsayısı
        b (float): x katsayısı
        c (float): Sabit terim
    
    Returns:
        Tuple[float, float]: (x₁, x₂) - Denklemin iki kökü
        None: Gerçek kök yoksa (diskriminant < 0)
    
    Raises:
        ValueError: a = 0 ise (bu ikinci derece denklem değil)
        TypeError: Parametreler sayı değilse
    
    Examples:
        >>> solve_quadratic_equation(1, -5, 6)
        (3.0, 2.0)
        
        >>> solve_quadratic_equation(1, 0, 1)
        None
        
        >>> solve_quadratic_equation(1, 2, 1)
        (-1.0, -1.0)
    """
    # Giriş validasyonu
    if a == 0:
        raise ValueError("❌ HATA: a = 0 olamaz! Bu ikinci derece denklem değil.")
    
    try:
        a, b, c = float(a), float(b), float(c)
    except (ValueError, TypeError):
        raise TypeError("❌ HATA: a, b, c parametreleri sayı olmalıdır.")
    
    # Diskriminant hesapla: Δ = b² - 4ac
    discriminant = b**2 - 4*a*c
    
    # Gerçek kök yoksa None döndür
    if discriminant < 0:
        return None
    
    # Quadratic formula: x = (-b ± √Δ) / 2a
    sqrt_discriminant = math.sqrt(discriminant)
    x1 = (-b + sqrt_discriminant) / (2*a)
    x2 = (-b - sqrt_discriminant) / (2*a)
    
    return (x1, x2)


# ===== TEST KODLARI =====
if __name__ == "__main__":
    print("🧮 İKİNCİ DERECE DENKLEM ÇÖZÜCÜ TEST\n")
    
    # Test 1: Normal durum
    print("Test 1: x² - 5x + 6 = 0")
    result = solve_quadratic_equation(1, -5, 6)
    print(f"   Kökler: {result}")
    assert result == (3.0, 2.0), "Test failed!"
    print("   ✅ PASSED\n")
    
    # Test 2: Gerçek kök yok (diskriminant < 0)
    print("Test 2: x² + 1 = 0 (Gerçek kök yok)")
    result = solve_quadratic_equation(1, 0, 1)
    print(f"   Kökler: {result}")
    assert result is None, "Test failed!"
    print("   ✅ PASSED\n")
    
    # Test 3: Çift kök
    print("Test 3: x² + 2x + 1 = 0 (Çift kök)")
    result = solve_quadratic_equation(1, 2, 1)
    print(f"   Kökler: {result}")
    assert abs(result[0] - (-1.0)) < 1e-10 and abs(result[1] - (-1.0)) < 1e-10, "Test failed!"
    print("   ✅ PASSED\n")
    
    # Test 4: Negatif a
    print("Test 4: -x² + 5x - 6 = 0")
    result = solve_quadratic_equation(-1, 5, -6)
    print(f"   Kökler: {result}")
    print("   ✅ PASSED\n")
    
    # Test 5: Hata durumu
    print("Test 5: a = 0 (Hata işleme)")
    try:
        result = solve_quadratic_equation(0, 5, 6)
        print("   ❌ FAILED - Exception beklendi")
    except ValueError as e:
        print(f"   ✅ PASSED - {e}\n")
    
    print("="*50)
    print("✅ Tüm Testler Başarılı!")


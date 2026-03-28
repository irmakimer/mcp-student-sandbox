def average_ratios(numbers):
    """
    Sayıların 100'e oranının ortalamasını hesapla.
    Sıfır değerleri güvenli şekilde işle (atla).
    
    Args:
        numbers (list): Sayı listesi
    
    Returns:
        float: Oranların ortalaması
    
    Raises:
        ValueError: Liste boş veya tüm değerler sıfır ise
    """
    if not numbers:
        raise ValueError("Liste boş olamaz!")
    
    ratios = []
    for num in numbers:
        if num == 0:
            # Sıfırları atla (sıfıra bölüp hataya yol açmaz)
            continue
        ratios.append(100 / num)
    
    if not ratios:
        raise ValueError("Tüm değerler sıfır olamaz!")
    
    return sum(ratios) / len(ratios)


# ===== TEST KODLARI =====
def test_average_ratios():
    """Tüm test senaryolarını çalıştır."""
    print("🧪 TESTLER BAŞLIYOR...\n")
    
    # Test 1: Normal değerler
    try:
        result = average_ratios([10, 5])
        expected = (100/10 + 100/5) / 2  # (10 + 20) / 2 = 15
        assert abs(result - expected) < 0.01, f"Beklenen {expected}, aldığımız {result}"
        print("✅ Test 1 PASSED: Normal değerler [10, 5]")
    except Exception as e:
        print(f"❌ Test 1 FAILED: {e}")
    
    # Test 2: Sıfırla karışık (ASIL HATA DURUMU)
    try:
        result = average_ratios([10, 5, 0])
        expected = (100/10 + 100/5) / 2  # Sıfır atlandı = (10 + 20) / 2 = 15
        assert abs(result - expected) < 0.01, f"Beklenen {expected}, aldığımız {result}"
        print("✅ Test 2 PASSED: Sıfırla karışık [10, 5, 0]")
    except Exception as e:
        print(f"❌ Test 2 FAILED: {e}")
    
    # Test 3: Tek değer
    try:
        result = average_ratios([5])
        expected = 100 / 5  # 20
        assert abs(result - expected) < 0.01, f"Beklenen {expected}, aldığımız {result}"
        print("✅ Test 3 PASSED: Tek değer [5]")
    except Exception as e:
        print(f"❌ Test 3 FAILED: {e}")
    
    # Test 4: Tüm değerler sıfır (Error handling)
    try:
        result = average_ratios([0, 0, 0])
        print(f"❌ Test 4 FAILED: ValueError yoksa sorun var (result={result})")
    except ValueError as e:
        print(f"✅ Test 4 PASSED: ValueError yakalandı '{e}'")
    except Exception as e:
        print(f"❌ Test 4 FAILED: Yanlış hata türü {e}")
    
    # Test 5: Boş liste (Error handling)
    try:
        result = average_ratios([])
        print(f"❌ Test 5 FAILED: ValueError yoksa sorun var (result={result})")
    except ValueError as e:
        print(f"✅ Test 5 PASSED: ValueError yakalandı '{e}'")
    except Exception as e:
        print(f"❌ Test 5 FAILED: Yanlış hata türü {e}")
    
    print("\n" + "="*50)


if __name__ == "__main__":
    test_average_ratios()
    print("\n🔢 SONUÇ ÖRNEKLERİ:\n")
    print(f"[10, 5, 0]       → {average_ratios([10, 5, 0]):.2f}")
    print(f"[20, 10, 0, 5]   → {average_ratios([20, 10, 0, 5]):.2f}")
    print(f"[100]            → {average_ratios([100]):.2f}")

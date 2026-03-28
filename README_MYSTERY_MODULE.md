# 🧮 Mystery Module - İkinci Derece Denklem Çözücü

**Açıklama:** Bu modül, ikinci derece denklemlerin (quadratic equations) köklerini bulmak için kullanılan bir Python kütüphanesidir.

---

## 📋 İçindekiler

- [Giriş](#giriş)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [API Referansı](#api-referansı)
- [Örnekler](#örnekler)
- [Hata Yönetimi](#hata-yönetimi)
- [İleri Konular](#ileri-konular)
- [Katkıda Bulunma](#katkıda-bulunma)

---

## 🚀 Giriş

### Problem Nedir?

İkinci derece denklemler (quadratic equations) matematik, fizik ve mühendislikte sık karşılaşılan problemlerdir:

$$Ax^2 + Bx + C = 0$$

Bu modül, herhangi bir ikinci derece denklemi hızlı ve doğru bir şekilde çözer.

### Çözüm Yöntemi: Quadratic Formula

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

---

## 💻 Kurulum

```bash
# 1. Modülü klonla veya indir
cp mystery_module.py your_project/

# 2. Import et
from mystery_module import solve_quadratic_equation
```

**Bağımlılıklar:**

- Python 3.7+
- `math` modülü (standart kütüphane)

---

## 📖 Kullanım

### Basit Örnek

```python
from mystery_module import solve_quadratic_equation

# x² - 5x + 6 = 0 denklemini çöz
roots = solve_quadratic_equation(a=1, b=-5, c=6)
print(roots)  # Output: (3.0, 2.0)
```

### Adım Adım

```python
# 1. Denklemini tanımla: x² + 2x - 8 = 0
a = 1      # x² katsayısı
b = 2      # x katsayısı
c = -8     # Sabit terim

# 2. Çöz
roots = solve_quadratic_equation(a, b, c)

# 3. Sonucu kontrol et
if roots:
    x1, x2 = roots
    print(f"Kökler: x₁ = {x1}, x₂ = {x2}")
else:
    print("Gerçek kök yoktur!")
```

---

## 🔧 API Referansı

### `solve_quadratic_equation(a, b, c)`

**Fonksiyon Açıklaması:**

- Ax² + Bx + C = 0 formundaki denklemin köklerini hesaplar
- **Diskriminant** (Δ = b² - 4ac) kullanarak kök türünü belirler

**Parametreler:**

| Parameter | Tip   | Açıklama                 |
| --------- | ----- | ------------------------ |
| `a`       | float | x² katsayısı (0 olamaz!) |
| `b`       | float | x katsayısı              |
| `c`       | float | Sabit terim              |

**Dönüş Değeri:**

| Durum     | Dönen Değer | Anlamı                |
| --------- | ----------- | --------------------- |
| **Δ > 0** | `(x₁, x₂)`  | İki farklı gerçek kök |
| **Δ = 0** | `(x, x)`    | Bir çift kök          |
| **Δ < 0** | `None`      | Gerçek kök yoktur     |

**Hatalar:**

| Hata         | Neden              | Çözüm                      |
| ------------ | ------------------ | -------------------------- |
| `ValueError` | a = 0              | a parametresi 0 olamaz     |
| `TypeError`  | a, b, c sayı değil | Parametreleri sayıya çevir |

---

## 📚 Örnekler

### Örnek 1: İki Farklı Kök

```python
# x² - 5x + 6 = 0
# (x - 2)(x - 3) = 0
result = solve_quadratic_equation(1, -5, 6)
print(result)  # (3.0, 2.0) ✅
```

### Örnek 2: Bir Çift Kök

```python
# x² + 2x + 1 = 0
# (x + 1)² = 0
result = solve_quadratic_equation(1, 2, 1)
print(result)  # (-1.0, -1.0) ✅
```

### Örnek 3: Gerçek Kök Yok

```python
# x² + 1 = 0
# (Hayali sayılar gerekli)
result = solve_quadratic_equation(1, 0, 1)
print(result)  # None ✅
```

### Örnek 4: Negatif a Katsayısı

```python
# -2x² + 8x - 6 = 0
result = solve_quadratic_equation(-2, 8, -6)
print(result)  # (3.0, 1.0) ✅
```

### Örnek 5: Kesirli Katsayılar

```python
# 0.5x² - 1.5x + 1 = 0
result = solve_quadratic_equation(0.5, -1.5, 1)
print(result)  # (2.0, 1.0) ✅
```

---

## ⚠️ Hata Yönetimi

### Hata 1: a = 0

```python
try:
    result = solve_quadratic_equation(0, 5, 6)
except ValueError as e:
    print(f"Hata: {e}")
    # Output: Hata: ❌ HATA: a = 0 olamaz!
```

### Hata 2: Geçersiz Veri Tipi

```python
try:
    result = solve_quadratic_equation("1", "2", "3")
except TypeError as e:
    print(f"Hata: {e}")
    # Output: Hata: ❌ HATA: a, b, c parametreleri sayı olmalıdır.
```

### Hata 3: Correct Exception Handling

```python
def safe_solve(a, b, c):
    try:
        return solve_quadratic_equation(a, b, c)
    except (ValueError, TypeError) as e:
        print(f"❌ Çözüm başarısız: {e}")
        return None

# Kullan
roots = safe_solve(1, 2, 3)
```

---

## 🎓 İleri Konular

### Diskriminant Analizi

```python
def analyze_roots(a, b, c):
    """Diskriminanta göre kök türünü belirle"""
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        print("✅ İki farklı gerçek kök")
    elif discriminant == 0:
        print("✅ Bir çift kök (tekrarlanan kök)")
    else:
        print("❌ Gerçek kök yok (karmaşık kökler)")

    return discriminant

analyze_roots(1, -5, 6)  # ✅ İki farklı gerçek kök
```

### Kökleri Doğrula

```python
def verify_roots(a, b, c, roots):
    """Bulunan köklerin doğruluğunu kontrol et"""
    if roots is None:
        print("Gerçek kök yoktur")
        return

    x1, x2 = roots

    # Ax² + Bx + C = 0 kontrolü
    check1 = a*x1**2 + b*x1 + c
    check2 = a*x2**2 + b*x2 + c

    print(f"x₁ = {x1}: {check1:.10f} ≈ 0")
    print(f"x₂ = {x2}: {check2:.10f} ≈ 0")

roots = solve_quadratic_equation(1, -5, 6)
verify_roots(1, -5, 6, roots)
```

---

## 🧪 Test Çalıştırma

```bash
# Tüm testleri çalıştır
python mystery_module.py

# Output:
# 🧮 İKİNCİ DERECE DENKLEM ÇÖZÜCÜ TEST
#
# Test 1: x² - 5x + 6 = 0
#    Kökler: (3.0, 2.0)
#    ✅ PASSED
# ...
# ✅ Tüm Testler Başarılı!
```

---

## 📊 Matematik Referansı

### Quadratic Formula Türetimi

```
Ax² + Bx + C = 0

Adım 1: Standart forma dönüştür
x² + (B/A)x + (C/A) = 0

Adım 2: Tamamlama
(x + B/2A)² = (B/2A)² - C/A
(x + B/2A)² = (B² - 4AC) / 4A²

Adım 3: Çöz
x + B/2A = ±√(B² - 4AC) / 2A
x = (-B ± √(B² - 4AC)) / 2A
```

### Diskriminant (Δ)

- **Δ = b² - 4ac** kök türünü belirler
- **Δ > 0:** İki farklı gerçek kök
- **Δ = 0:** Bir çift kök (tekrarlanan)
- **Δ < 0:** Karmaşık kökler (gerçek kök yok)

---

## 🤝 Katkıda Bulunma

### Hata Bulursanız

1. **Issue açın** - Sorunun ayrıntılarını yazın
2. **Örnek kodu paylaşın** - Hatayı yeniden üretin
3. **Pull Request gönderin** - Düzeltme önerin

### Geliştirme İçin

```bash
# 1. Fork et
# 2. Branch oluştur
git checkout -b feature/your-feature

# 3. Değişiklikleri yap
# 4. Test et
python mystery_module.py

# 5. Commit et
git commit -m "Add: your-feature"

# 6. Push et
git push origin feature/your-feature

# 7. Pull Request aç
```

---

## 📄 Lisans

MIT License - Özgürce kullanabilirsiniz!

---

## 🔗 Kaynaklar

- [Wikipedia: Quadratic Equation](https://en.wikipedia.org/wiki/Quadratic_equation)
- [Wolfram MathWorld: Quadratic Formula](https://mathworld.wolfram.com/QuadraticFormula.html)
- [Khan Academy: Quadratic Equations](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratic-functions-equations)

---

## 📞 İletişim

Sorularınız için bir issue açabilir veya PR gönderebilirsiniz!

**Sürüm:** 2.0 (Refactored)  
**Son Güncelleme:** 2026-03-28  
**Durum:** ✅ Production Ready

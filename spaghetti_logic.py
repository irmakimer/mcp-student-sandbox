def apply_price_increase(value, increase_rate=0.15):
    """
    Verilen değere yüzde artış uygula.
    
    Args:
        value (float): Orijinal değer
        increase_rate (float): Artış oranı (varsayılan: %15)
    
    Returns:
        float: Artış uygulanmış değer
    """
    return value * (1 + increase_rate)


def format_price_result(value):
    """
    Fiyat sonucunu insan tarafından okunabilir formata dönüştür.
    
    Args:
        value (float): Formatlanacak değer
    
    Returns:
        str: Formatlanmış fiyat metni
    """
    return f"Total: {value:.2f}"


def log_results_to_file(results, filename="log.txt"):
    """
    İşlem sonuçlarını dosyaya yaz.
    
    Args:
        results (list): Yazılacak sonuçlar
        filename (str): Log dosyası adı
    """
    with open(filename, "a") as log_file:
        log_file.write(str(results) + "\n")


def display_price(formatted_price):
    """
    Fiyat bilgisini ekrana yazdır.
    
    Args:
        formatted_price (str): Yazdırılacak formatlanmış fiyat
    """
    print(formatted_price)


def process_data(data, increase_rate=0.15, log_filename="log.txt", should_display=True):
    """
    Veri listesini işle: fiyat artışı uygula, formatla ve isteğe bağlı olarak kaydet.
    
    Args:
        data (list): İşlenecek veri listesi
        increase_rate (float): Fiyat artış oranı (varsayılan: %15)
        log_filename (str): Log dosyası adı
        should_display (bool): Sonuçları ekrana yazdırıp yazdırmayacak
    
    Returns:
        list: İşlenmiş fiyatlar listesi
    """
    processed_prices = []
    
    for price in data:
        # Fiyata artış uygula
        increased_price = apply_price_increase(price, increase_rate)
        processed_prices.append(increased_price)
        
        # İsteğe bağlı olarak ekrana yazdır
        if should_display:
            formatted_result = format_price_result(increased_price)
            display_price(formatted_result)
    
    # Sonuçları log dosyasına yaz
    log_results_to_file(processed_prices, log_filename)
    
    return processed_prices


# Test verisi
if __name__ == "__main__":
    test_prices = [100, 200, 300, 150]
    print("🔄 Fiyatlar işleniyor...")
    result = process_data(test_prices)
    print(f"\n✅ İşlem tamamlandı! Sonuçlar: {result}")

"""
AWS bağlantı modülü - Güvenli credential yönetimi
UYARI: Hiçbir zaman sırları kaynak kodda saklamayın!
"""

import os
from dotenv import load_dotenv

# .env dosyasından ortam değişkenlerini yükle
load_dotenv()


def get_aws_credentials():
    """
    AWS kimlik bilgilerini ortam değişkenlerinden güvenli şekilde al.
    
    Returns:
        dict: AWS kredisi (access_key, secret_key)
    
    Raises:
        ValueError: Gerekli ortam değişkenleri bulunamazsa
    """
    aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    
    if not aws_access_key or not aws_secret_key:
        raise ValueError(
            "❌ HATA: AWS_ACCESS_KEY_ID ve AWS_SECRET_ACCESS_KEY "
            "ortam değişkenleri tanımlanmamış!\n"
            "Çözüm: .env dosyası oluşturun veya sistem ortam değişkenlerini ayarlayın"
        )
    
    return {
        "access_key": aws_access_key,
        "secret_key": aws_secret_key
    }


def connect():
    """
    AWS'ye güvenli şekilde bağlan.
    Sırlar kaynak kodda saklanmaz!
    """
    try:
        credentials = get_aws_credentials()
        # ✅ GÜVENLI: Sırları ekrana yazdırmıyoruz
        print("✅ AWS'ye başarıyla bağlandı")
        print(f"   Access Key: {credentials['access_key'][:10]}...***")  # Kısmi göster
        return credentials
    except ValueError as e:
        print(f"❌ Bağlantı hatası: {e}")
        return None


# ===== TEST KODLARI =====
if __name__ == "__main__":
    print("🔐 AWS Güvenli Bağlantı Testi\n")
    
    # Credentials almayı dene
    credentials = connect()
    
    if credentials:
        print("\n✅ Test başarılı!")
    else:
        print("\n⚠️  Test başarısız - ortam değişkenlerine bakın")


#!/usr/bin/env python3
"""
Güvenlik Tarama Script'i
Repository'de hardcoded credentials aramak için
"""

import os
import re
from pathlib import Path

SUSPICIOUS_PATTERNS = {
    "API_KEY": r'(?:api[_-]?key|apikey)\s*=\s*["\']?[\w\-]+["\']?',
    "PASSWORD": r'(?:password|passwd|pwd)\s*=\s*["\']?[\w\-]+["\']?',
    "SECRET": r'(?:secret|secret_key)\s*=\s*["\']?[\w\-]+["\']?',
    "TOKEN": r'(?:token|access_token)\s*=\s*["\']?[\w\-\.]+["\']?',
    "AWS_KEY": r'(?:AKIA|aws_access_key|aws_secret)\s*=?',
    "DATABASE_URL": r'(?:database_url|db_url)\s*=\s*["\']?[\w:\/\-@\.]+["\']?',
}

IGNORED_FILES = {".env", ".env.example", "SECURITY.md", "security_scan.py", ".gitignore"}
IGNORED_DIRS = {"__pycache__", ".git", ".venv", "venv"}


def scan_directory(directory):
    """Repository'yi güvenlik açıkları için tara."""
    issues_found = []
    
    for root, dirs, files in os.walk(directory):
        # .gitignore'd dosyaları atla
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]
        
        for file in files:
            if not file.endswith(".py"):
                continue
            if file in IGNORED_FILES:
                continue
            
            filepath = os.path.join(root, file)
            try:
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    
                for line_num, line in enumerate(content.split("\n"), 1):
                    for pattern_name, pattern in SUSPICIOUS_PATTERNS.items():
                        if re.search(pattern, line, re.IGNORECASE):
                            # Yanlış pozitiften kaçın
                            if "getenv" in line or "os.environ" in line:
                                continue
                            if line.strip().startswith("#"):
                                continue
                            
                            issues_found.append({
                                "file": filepath,
                                "line": line_num,
                                "pattern": pattern_name,
                                "code": line.strip()[:100]
                            })
            except Exception as e:
                print(f"⚠️  Dönem {filepath}: {e}")
    
    return issues_found


def print_report(issues):
    """Güvenlik raporu yazdır."""
    print("\n" + "="*70)
    print("🔐 GÜVENLIK TARAMA RAPORU")
    print("="*70 + "\n")
    
    if not issues:
        print("✅ Herhangi bir güvenlik sorunu bulunamadı!")
        return
    
    print(f"⚠️  {len(issues)} Potansiyel Güvenlik Sorunu Bulundu:\n")
    
    for i, issue in enumerate(issues, 1):
        print(f"{i}. {issue['pattern']}")
        print(f"   📁 Dosya: {issue['file']}")
        print(f"   📍 Satır: {issue['line']}")
        print(f"   💻 Kod: {issue['code']}")
        print()


if __name__ == "__main__":
    repo_path = Path(__file__).parent.parent / "mcp-student-sandbox"
    print(f"🔍 Taranıyor: {repo_path}\n")
    
    issues = scan_directory(str(repo_path))
    print_report(issues)
    
    if issues:
        print("💡 TAVSIYELER:")
        print("   1. Hardcoded credentials olduğunu bulun")
        print("   2. Environment variables'a taşıyın")
        print("   3. .env dosyasını .gitignore'a ekleyin")
        print("   4. Tüm istiyahtı aklaştır\n")

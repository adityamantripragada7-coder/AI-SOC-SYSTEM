def check_ip_reputation(ip):

    print(f"🔍 Checking reputation for IP: {ip}")

    blacklist = [
        "192.168.1.10",
        "10.0.0.9"
    ]

    if ip in blacklist:
        print("⚠️ Malicious IP detected")
        return 90

    print("✅ Safe IP")
    return 10
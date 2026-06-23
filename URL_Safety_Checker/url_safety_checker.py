trusted_domains = ["google.com", "microsoft.com", "wikipedia.org","iitk.ac.in", "google.com", "nist.gov", "github.com"]

suspicious_words = ["verify", "login", "account", "bank", "claim", "password", "payment", 
                    "invoice", "wallet", "update", "crypto", "bitcoin", "urgent", "reward", "prize","free","money"]

suspicious_extensions = [".xyz", ".top", ".click", ".tk", ".loan", ".zip", ".buzz", ".review"]

while True:

    url = input("\nEnter URL (or type 'exit' to quit): ")

    if url.lower() == "exit":
        print("Exiting URL Safety Checker...")
        break

    risk_score = 0
    reasons = []

    # HTTPS Check
    if not url.startswith("https://"):
        risk_score += 1
        reasons.append("Not using HTTPS")

    # Trusted Domain Check
    trusted = False

    for domain in trusted_domains:
        if domain in url.lower():
            trusted = True
            break

    if trusted:
        reasons.append("Trusted domain detected")

    ## Suspicious Keyword Check
    detected_keywords = []

    for word in suspicious_words:
        if word in url.lower():
            detected_keywords.append(word)
            risk_score += 1

    if detected_keywords:
        reasons.append("Suspicious keywords: " +", ".join(detected_keywords))

    # Suspicious Extension Check
    for ext in suspicious_extensions:
        if url.lower().endswith(ext):
            risk_score += 1
            reasons.append(f"Suspicious domain extension ({ext})")

    # Number Check
    digit_count = 0

    for char in url:
        if char.isdigit():
            digit_count += 1

    if digit_count >= 4:
        risk_score += 1
        reasons.append("Contains many numbers")

    # URL Length Check
    if len(url) > 50:
        risk_score += 1
        reasons.append("Unusually long URL")

    print("\n== URL Safety Report ==")

    if reasons:
        for reason in reasons:
            print("-", reason)
    else:
        print("No warning signs detected.")

    print(f"\nRisk Score: {risk_score}")

    if risk_score == 0:
        print("Risk Level: Low")
    elif risk_score <= 2:
        print("Risk Level: Medium")
    else:
        print("Risk Level: High")

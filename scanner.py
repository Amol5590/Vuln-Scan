
import requests

def scan(url):
    issues=[]
    r=requests.get(url,timeout=5)
    h=r.headers

    if "Content-Security-Policy" not in h:
        issues.append("Missing CSP Header")

    if "X-Frame-Options" not in h:
        issues.append("Missing X-Frame-Options")

    if "Set-Cookie" in h and "Secure" not in h["Set-Cookie"]:
        issues.append("Cookie Missing Secure Flag")

    if "<script>" in r.text.lower():
        issues.append("Possible XSS")

    if "'" in r.text:
        issues.append("Possible SQL Injection Indicator")

    return issues or ["No issues detected"]

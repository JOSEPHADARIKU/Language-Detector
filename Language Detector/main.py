
from src.detector import detect_language

print("🌐 Welcome to the Advanced Language Detector! 🌐\n")

while True:
    text = input("Enter text to detect language (or type 'exit' to quit): ").strip()
    if text.lower() == "exit":
        print("Goodbye! 👋")
        break
    elif text:
        language = detect_language(text)
        print(f"Detected Language: {language}\n")
    else:
        print("⚠️ Please enter some text.\n")

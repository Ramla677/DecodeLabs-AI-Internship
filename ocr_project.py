import pytesseract
from PIL import Image
import time


pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

print("=" * 60)
print("📝 OCR TEXT RECOGNITION SYSTEM")
print("=" * 60)

image_path = input("Enter image file name: ")

start_time = time.time()

img = Image.open(image_path)

text = pytesseract.image_to_string(img)

end_time = time.time()

processing_time = round(end_time - start_time, 2)

word_count = len(text.split())
character_count = len(text)

with open("output.txt", "w", encoding="utf-8") as file:
    file.write(text)

print("\nDetected Text")
print("-" * 40)
print(text)
print("-" * 40)

print("\n📊 Analysis")
print("Words Found      :", word_count)
print("Characters Found :", character_count)
print("Processing Time  :", processing_time, "seconds")

print("\n💾 Extracted text saved to output.txt")

print("\n✅ OCR Process Completed Successfully!")
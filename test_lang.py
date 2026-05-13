from langdetect import detect

telugu = "నమస్కారం నాకు సహాయం కావాలి"
hindi = "नमस्ते मुझे मदद चाहिए"
english = "Hello I need help"

print(f"Telugu detected as: {detect(telugu)}")
print(f"Hindi detected as: {detect(hindi)}")
print(f"English detected as: {detect(english)}")
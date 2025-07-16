import os

def analyze_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext in ['.txt']:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            return f"AI Summary (text): {content[:200]}..."  # Example for .txt
    elif ext in ['.pdf']:
        return "AI Summary: This is a PDF file."
    elif ext in ['.csv']:
        return "AI Summary: CSV with tabular data."
    elif ext in ['.jpg', '.png']:
        return "AI Summary: This is an image file."
    else:
        return f"AI Summary: Cannot parse .{ext[1:]} files yet, but file is received."

from PIL import Image


def analyze_chat_screenshot(uploaded_file):

    image = Image.open(uploaded_file)

    width, height = image.size

    return f"""
### Screenshot Analysis

✅ Screenshot uploaded successfully

Image Size: {width} x {height}

This is a placeholder analysis.

Next version will:
- Detect red flags
- Analyze conversation balance
- Estimate interest level
- Detect mixed signals
- Suggest what to reply
"""

import os
import tempfile
import pypandoc

# Automatically download Pandoc if not found
try:
    pypandoc.get_pandoc_version()
except OSError:
    print("[INFO] Pandoc not found. Downloading locally...")
    pypandoc.download_pandoc()

async def convert_file(file, target_format: str) -> str:
    """
    Placeholder function for file conversion logic.
    For now, just saves the uploaded file temporarily and returns its path.
    """
    # Save uploaded file temporarily
    _, ext = os.path.splitext(file.filename)
    with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    # Simulate an output file path
    output_path = f"{tmp_path}_converted.{target_format}"

    print(f"Starting to convert {tmp_path} to {target_format}")

    formatSupported = ['txt', 'docx', 'pdf']

    if target_format not in formatSupported:
        raise ValueError(f"Unsupported text format: {target_format}")
    
    format_map = {
        ".txt": "markdown",   # treat .txt as markdown/plain text
        ".docx": "docx"
    }

    input_format = format_map.get(ext.lower(), "markdown")  # default to markdown

    try:
        pypandoc.convert_file(tmp_path, to=target_format, format=input_format, outputfile=output_path)
        print(f"file Conversion Successful... {output_path}")

    except Exception as e:
        print(f"Conversion failed: {e}")
        raise RuntimeError("File conversion failed.") from e

    return output_path

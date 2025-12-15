from app.services.filters import apply_filters
import asyncio

TEST_FILE = "tests/input_test.txt"

async def run_test():
    await apply_filters(file_path=TEST_FILE, run_profanity=True, run_spellcheck=True)

    print("Filters applied. Check the file content.")

asyncio.run(run_test())
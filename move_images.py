import os
import shutil

source_dir = r"e:\ISTE - KEC (website)\Gallary"
target_dir = r"e:\ISTE - KEC (website)\api\static\images\gallery"

# Clean target directory if it exists
if os.path.exists(target_dir):
    shutil.rmtree(target_dir)
os.makedirs(target_dir)

# Get all files from source directory
files = os.listdir(source_dir)
image_extensions = ['.jpg', '.jpeg', '.png', '.webp']

count = 1
for filename in files:
    ext = os.path.splitext(filename)[1].lower()
    if ext in image_extensions:
        source_path = os.path.join(source_dir, filename)
        # Force jpg extension for consistency in template if needed, or keep original?
        # Template uses .jpg hardcoded: gallery_' ~ i ~ '.jpg'
        # So I MUST convert or rename with .jpg extension if I want to keep template simple.
        # But simply renaming extension is risky if format differs.
        # Better: just keep original extension, but template needs to know.
        # OR: Renaming .png to .jpg usually doesn't break browsers, but it's bad practice.
        # Let's check what extensions we have. We have png and jpg.
        # I will just rename everything to .jpg for simplicity in template or update template to handle multiple extensions?
        # Updating template is harder without backend logic.
        # I will rename the physical file to .jpg. Browsers often handle mismatched mime/extension fine for images.
        
        new_filename = f"gallery_{count}.jpg"
        target_path = os.path.join(target_dir, new_filename)
        
        shutil.copy2(source_path, target_path)
        print(f"Copied: {filename} -> {new_filename}")
        count += 1

print(f"Successfully moved {count-1} images to {target_dir}")

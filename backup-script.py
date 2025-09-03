import os, shutil, time
from pathlib import Path

# Source folder (files to backup) and Destination (where backup goes)
src = Path("testdata")
dest = Path("backup")
dest.mkdir(exist_ok=True)   # create backup folder if not exists

# Check if source exists
if not src.exists():
    print(f"❌ Source folder '{src}' not found.")
    raise SystemExit(2)

# Create backup with timestamp
ts = time.strftime("%Y%m%d_%H%M%S")
archive_base = dest / f"backup_{ts}"   # .zip will be added
out_path = shutil.make_archive(str(archive_base), "zip", root_dir=src)

print(f"✅ Backup successful: {out_path}")

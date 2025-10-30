from pathlib import Path
import ast

proj = Path(__file__).resolve().parents[1]
ds = proj / "data" / "vplab_indoor"
src_yaml = ds / "data.yaml"
if not ds.exists():
    raise SystemExit(f"Dataset folder not found: {ds}")

text = src_yaml.read_text()
names_list = None
for line in text.splitlines():
    if line.strip().startswith("names:"):
        idx = text.index("names:")
        try:
            s = text[text.index("[", idx): text.index("]", idx)+1]
            names_list = ast.literal_eval(s)
        except Exception:
            pass
        break

if names_list is None:
    raise SystemExit("Could not parse names from data.yaml — check its format")

names_map = "\n".join([f"  {i}: '{name}'" for i, name in enumerate(names_list)])
content = f"""path: {ds.as_posix()}
train: train/images
val: valid/images
test: test/images

names:
{names_map}
"""
out = proj / "vplab_indoor.yaml"
out.write_text(content)
print("✅ Wrote", out)
print(out.read_text())


import os

def list_verilog_files():
    files = []
    for root, _, filenames in os.walk("."):
        for filename in filenames:
            if filename.endswith(".v"):
                files.append(os.path.relpath(os.path.join(root, filename)))
    return sorted(files)

def update_readme(verilog_files):
    with open("README.md", "r") as f:
        lines = f.readlines()

    start, end = None, None
    for i, line in enumerate(lines):
        if line.strip() == "<!-- MODULE LIST START -->":
            start = i
        if line.strip() == "<!-- MODULE LIST END -->":
            end = i

    if start is not None and end is not None and start < end:
        list_lines = ["\n"] + [f"- `{file}`" for file in verilog_files] + ["\n"]
        new_lines = lines[:start+1] + list_lines + lines[end:]
        with open("README.md", "w") as f:
            f.writelines(new_lines)
    else:
        print("Markers <!-- MODULE LIST START --> and <!-- MODULE LIST END --> not found or in incorrect order.")

if __name__ == "__main__":
    verilog_files = list_verilog_files()
    update_readme(verilog_files)

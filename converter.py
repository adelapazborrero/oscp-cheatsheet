import os
import sys

def convert_norg_to_md(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    md_lines = []
    for line in lines:
        if line.startswith('*'):
            md_lines.append('#' + line[1:])
        elif '@code' in line:
            md_lines.append('```bash\n')
        elif '@end' in line:
            md_lines.append('```\n')
        elif line.strip() == '___':
            md_lines.append('-----------------------\n')
        else:
            md_lines.append(line)

    with open(output_file, 'w') as f:
        f.writelines(md_lines)

def convert_files_in_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.norg'):
                input_file = os.path.join(root, file)
                output_file = os.path.splitext(input_file)[0] + ".md"
                convert_norg_to_md(input_file, output_file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python converter.py <directory>")
    else:
        directory = sys.argv[1]
        convert_files_in_directory(directory)

import sys
import shutil

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
    
    shutil.move(input_file, './backups') 

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python converter.py <input_file>")
    else:
        input_file = sys.argv[1]
        output_file = input_file.split(".")[0] + ".md"
        convert_norg_to_md(input_file, output_file)

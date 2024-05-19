import codecs
import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        return result['encoding']

def convert_encoding(input_file, output_file):
    input_encoding = detect_encoding(input_file)
    
    with codecs.open(input_file, 'r', encoding=input_encoding, errors='ignore') as f:
        content = f.read()
    
    with codecs.open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    input_file = input("Enter the path of the input file: ")
    output_file = input("Enter the path of the output file: ")
    convert_encoding(input_file, output_file)
    print("Conversion completed successfully.")

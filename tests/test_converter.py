from app.parsers.txt_parser import TxtParser
from app.parsers.txt_converter import TxtConverter


parser = TxtParser()

df = parser.parse(
    "input/txt/source_binding.txt"
)

converter = TxtConverter()

converter.save_to_excel(
    df,
    "output/converted/source_binding.xlsx"
)

print("Excel Generated Successfully")
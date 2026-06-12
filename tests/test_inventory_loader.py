from app.parsers.excel_reader import ExcelReader
from app.filters.column_filter import ColumnFilter
from app.utils.mac_utils import MacCleaner


reader = ExcelReader()

df = reader.read(
    "input/excel/inventory.xlsx"
)

print("\nOriginal Columns:\n")
print(df.columns)

filtered = ColumnFilter().extract(
    df
)

filtered = MacCleaner.normalize(
    filtered,
    "MAC Address"
)

print("\nFiltered Data:\n")

print(filtered.head())
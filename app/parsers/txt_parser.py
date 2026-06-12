"""Text file parser."""
import re
import polars as pl

from app.core.logger import get_logger

logger = get_logger()


class TxtParser:

    def __init__(self):
        self.ip_pattern = r'ip-address\s+([\d\.]+)'
        self.mac_pattern = r'mac-address\s+([a-fA-F0-9\-]+)'

    def parse(self, file_path: str) -> pl.DataFrame:

        records = []

        logger.info(f"Reading TXT File : {file_path}")

        with open(
            file_path,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as file:

            for line_number, line in enumerate(file, start=1):

                ip_match = re.search(
                    self.ip_pattern,
                    line
                )

                mac_match = re.search(
                    self.mac_pattern,
                    line
                )

                if ip_match and mac_match:

                    records.append(
                        {
                            "IP Address":
                                ip_match.group(1),

                            "MAC Address":
                                mac_match.group(1).lower()
                        }
                    )

        logger.info(
            f"Parsed {len(records)} records"
        )

        return pl.DataFrame(records)
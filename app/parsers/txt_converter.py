"""Text file converter."""
from pathlib import Path
import polars as pl

from app.core.logger import get_logger

logger = get_logger()


class TxtConverter:

    def save_to_excel(
        self,
        df: pl.DataFrame,
        output_file: str
    ):

        Path(output_file).parent.mkdir(
            parents=True,
            exist_ok=True
        )

        df.write_excel(output_file)

        logger.info(
            f"Excel Created: {output_file}"
        )
import polars as pl


class ColumnFilter:

    REQUIRED_COLUMNS = [
        "IPAdd",
        "MAC Address",
        "CompName",
        "User Name",
        "System Model",
        "Last AgentCom"
    ]

    def extract(
        self,
        df: pl.DataFrame
    ) -> pl.DataFrame:

        available = [
            col
            for col in self.REQUIRED_COLUMNS
            if col in df.columns
        ]

        return df.select(
            available
        )
from app.parsers.txt_parser import TxtParser


def test_parser():

    parser = TxtParser()

    df = parser.parse(
        "input/txt/source_binding.txt"
    )

    print(df)


if __name__ == "__main__":
    test_parser()
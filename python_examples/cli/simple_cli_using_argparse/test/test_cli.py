import pytest

from ..cli import main, parse_args


class TestParseArgs:
    def test_should_raise_error_when_name_not_provided(
        self
    ) -> None:
        with pytest.raises(SystemExit):
            parse_args(argv=[])

    def test_should_parse_name_correctly(self) -> None:
        args = parse_args(argv=["--name", "Alice"])
        assert args.name == "Alice"


class TestCli:
    def test_should_print_passed_in_name(
        self,
        capsys: pytest.CaptureFixture[str]
    ) -> None:
        main(argv=["--name", "Alice"])
        captured = capsys.readouterr()
        assert captured.out == "Hello, Alice!\n"
        assert captured.err == ""

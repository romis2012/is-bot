import typing
import functools
from regex import regex

from ._patterns import default_patterns


@functools.lru_cache(maxsize=1, typed=True)
def compile_patterns(patterns: frozenset) -> regex.Pattern:
    pattern = '({})'.format('|'.join(patterns))
    return regex.compile(pattern, flags=regex.IGNORECASE)


class Bots:
    def __init__(self, patterns: typing.Iterable[str] = None):
        if patterns is None:
            patterns = default_patterns
        self.patterns = frozenset(patterns)

    def extend(self, patterns: typing.Iterable[str]):
        if isinstance(patterns, str):
            patterns = [patterns]
        self.patterns = self.patterns | frozenset(patterns)

    def exclude(self, patterns: typing.Iterable[str]):
        if isinstance(patterns, str):
            patterns = [patterns]
        self.patterns = self.patterns - frozenset(patterns)

    def is_bot(self, ua: str) -> bool:
        pattern = compile_patterns(self.patterns)
        return bool(pattern.search(ua))

    def matches(self, ua: str) -> typing.List[str]:
        return [s for s in self.patterns if regex.search(s, ua, regex.IGNORECASE)]

    def find(self, ua: str) -> typing.Optional[str]:
        pattern = compile_patterns(self.patterns)
        match = pattern.search(ua)
        return match and match[0]


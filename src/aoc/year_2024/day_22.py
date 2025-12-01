# (c) 2025 Filip Tefr
# https://adventofcode.com/2024/day/22
from collections import defaultdict
from collections import deque

from aocd.models import Puzzle


class AoC2024Day22:
    def __init__(self, data: str):
        self._secrets = [int(x) for x in data.split()]

    def _mix(self, secret: int, number: int):
        return secret ^ number

    def _prune(self, secret: int):
        return secret & 0x00FFFFFF

    def _iterate(self, secret: int, num_iter: int = 1):
        for _ in range(num_iter):
            secret = secret ^ (secret << 6) & 0x00FFFFFF
            secret = secret ^ (secret >> 5) & 0x00FFFFFF
            secret = secret ^ (secret << 11) & 0x00FFFFFF
        return secret

    def calc_secrets_sum(self, num_iter: int = 2000):
        total = 0
        for secret in self._secrets:
            total += self._iterate(secret, num_iter)
        return total

    def get_best_sequence_price(self, num_iter: int = 2000, sequence_len: int = 4):
        prices: dict[tuple[int], int] = defaultdict(int)
        for secret in self._secrets:
            sequence = deque(maxlen=sequence_len)
            sequence_seen: dict[tuple[int, bool]] = defaultdict(lambda: False)
            prev_price = secret % 10
            for i in range(num_iter):
                secret = self._iterate(secret)
                price = secret % 10
                sequence.append(price - prev_price)
                prev_price = price
                if i < sequence_len - 1:
                    continue
                sequence_t = tuple(sequence)
                if not sequence_seen[sequence_t]:
                    prices[sequence_t] += price
                    sequence_seen[sequence_t] = True
        max_key = max(prices, key=prices.get)
        return prices[max_key]


def main():
    puzzle = Puzzle(year=2024, day=22)
    solver = AoC2024Day22(data=puzzle.input_data)
    secrets_sum = solver.calc_secrets_sum()
    best_sequence_price = solver.get_best_sequence_price()

    print(f"Sum of the 2000th secret number: {secrets_sum}")
    print(f"Most bananas: {best_sequence_price}")


if __name__ == "__main__":
    main()

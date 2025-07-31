# sayings_manager.py

import random
import textwrap
from collections import defaultdict

class SayingsManager:
    def __init__(self, quotes_by_weather, *, wrap_width=42, small_len=160, big_font=16, small_font=12):
        self.quotes = quotes_by_weather
        self.wrap_width = wrap_width
        self.small_len = small_len
        self.big_font = big_font
        self.small_font = small_font
        self._last_quote_for_type = defaultdict(lambda: None)

    def get_quote(self, weather_type: str) -> str:
        pool = self.quotes.get(weather_type, self.quotes.get("default", []))
        if not pool:
            return "No quote available."

        # Avoid immediate repetition
        last = self._last_quote_for_type[weather_type]
        if len(pool) > 1:
            choice = random.choice([q for q in pool if q != last])
        else:
            choice = pool[0]

        self._last_quote_for_type[weather_type] = choice
        return choice

    def format_for_label(self, quote: str):
        font_size = self.big_font if len(quote) <= self.small_len else self.small_font
        wrapped = textwrap.fill(quote, width=self.wrap_width)
        return wrapped, font_size
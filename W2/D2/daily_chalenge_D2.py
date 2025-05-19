import math


class Pagination:

    def __init__(self, items=None, page_size: int = 10):
        self.items = items or []
        self.page_size = page_size
        self.current_idx = 0
        self.total_pages = math.ceil(len(self.items) / self.page_size) \
            if self.page_size else 0


    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]


    def go_to_page(self, page_num: int):
        """Move to page `page_num` (1-based)."""
        if page_num < 1:
            raise ValueError("Page number must be at least 1")
        if page_num > self.total_pages:
            self.current_idx = max(self.total_pages - 1, 0)
        else:
            self.current_idx = page_num - 1
        return self

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        if self.total_pages:
            self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self


    def __str__(self):
        return "\n".join(str(item) for item in self.get_visible_items())


# ───────────────────────────────

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())        #

p.next_page()
print(p.get_visible_items())

p.last_page()
print(p.get_visible_items())

p.go_to_page(10)
print(p.current_idx + 1)

try:
    p.go_to_page(0)
except ValueError as err:
    print("Error:", err)

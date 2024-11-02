from typing import Optional


class Rectangle:
    """
    Class for a simple 2d Volume

    x_end and y_end is inclusive

    so Volume(0,0,0,0) is a single pixel

    """

    def __init__(self, x_start, y_start, x_end, y_end):

        if x_end < x_start:
            raise ValueError("x_end < x_start")
        if y_end < y_start:
            raise ValueError("y_end < y_start")

        self.x_start, self.y_start, self.x_end, self.y_end = (
            x_start,
            y_start,
            x_end,
            y_end,
        )

    def __hash__(self) -> int:
        return hash((self.x_start, self.y_start, self.x_end, self.y_end))

    def _inbetween(self, tup1: tuple[int], tup2: tuple[int]):

        if (tup1[0] <= tup2[0] and tup2[0] <= tup1[1]) or (
            tup1[0] <= tup2[1] and tup2[1] <= tup1[1]
        ):
            return True

        tup1, tup2 = tup2, tup1
        if (tup1[0] <= tup2[0] and tup2[0] <= tup1[1]) or (
            tup1[0] <= tup2[1] and tup2[1] <= tup1[1]
        ):
            return True

        return False

    def intersect(self, other: "Rectangle", recu=0) -> Optional["Rectangle"]:

        x_between = self._inbetween(
            (self.x_start, self.x_end), (other.x_start, other.x_end)
        )
        y_between = self._inbetween(
            (self.y_start, self.y_end), (other.y_start, other.y_end)
        )

        if not x_between or not y_between:
            return None

        x_start = max(self.x_start, other.x_start)
        x_end = min(self.x_end, other.x_end)

        y_start = max(self.y_start, other.y_start)
        y_end = min(self.y_end, other.y_end)

        return Rectangle(x_start, y_start, x_end, y_end)

    def __repr__(self) -> str:
        if self.x_start == self.x_end and self.y_start == self.y_end:
            return f"Dot {self.x_end, self.y_start}"

        if self.x_start == self.x_end:
            return f"Line x : {self.x_start}, y = [{self.y_start}, {self.y_end}]"

        if self.y_start == self.y_end:
            return f"Line y : {self.y_start}, x = [{self.x_start}, {self.x_end}]"

        return f"Volume x: ({self.x_start} - {self.x_end}) y: ({self.y_start} - {self.y_end})"

    def split(self, inter: "Rectangle") -> list["Rectangle"]:
        """inter must be an intersection of the volume.
        splits the volume up such that intersection carved out"""

        x_start_smaller = self.x_start < inter.x_start
        y_start_smaller = self.y_start < inter.y_start
        x_end_bigger = self.x_end > inter.x_end
        y_end_bigger = self.y_end > inter.y_end

        res = []

        # left side
        if x_start_smaller:
            res.append(
                Rectangle(
                    x_start=self.x_start,
                    x_end=inter.x_start - 1,
                    y_start=self.y_start,
                    y_end=inter.y_end,
                )
            )

        if x_end_bigger:
            res.append(
                Rectangle(
                    x_end=self.x_end,
                    x_start=inter.x_end + 1,
                    y_start=self.y_start,
                    y_end=inter.y_end,
                )
            )

        if y_start_smaller:

            res.append(
                Rectangle(
                    x_start=max(self.x_start, inter.x_start),
                    x_end=min(self.x_end, inter.x_end),
                    y_start=self.y_start,
                    y_end=inter.y_start - 1,
                )
            )

        if y_end_bigger:
            res.append(
                Rectangle(
                    x_start=self.x_start,
                    x_end=self.x_end,
                    y_start=inter.y_end + 1,
                    y_end=self.y_end,
                )
            )

        return res

    @property
    def area(self):
        return (self.x_end + 1 - self.x_start) * (self.y_end + 1 - self.y_start)

    @property
    def surrounding_borders(self) -> list["Rectangle"]:

        return [
            Rectangle(self.x_start - 1, self.y_start, self.x_start - 1, self.y_end),
            Rectangle(self.x_end + 1, self.y_start, self.x_end + 1, self.y_end),
            Rectangle(self.x_start, self.y_start - 1, self.x_end, self.y_start - 1),
            Rectangle(self.x_start, self.y_end + 1, self.x_end, self.y_end + 1),
        ]

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False

        return (
            self.x_start == other.x_start
            and self.y_start == other.y_start
            and self.x_end == other.x_end
            and self.y_end == other.y_end
        )


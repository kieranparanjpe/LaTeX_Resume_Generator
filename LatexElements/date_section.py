from LatexElements.latexelement import LatexElement


class DateSection(LatexElement):
    def __init__(self, start: str, end: str | None = None):
        self.start = start
        self.end = end

    def get_latex(self):
        if self.end is not None:
            return f"{self.start} - {self.end}"
        return self.start

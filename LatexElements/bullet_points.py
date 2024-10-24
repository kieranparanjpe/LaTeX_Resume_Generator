from typing import List

from LatexElements.latexelement import LatexElement


class BulletPoints(LatexElement):
    class BulletPoint(LatexElement):
        def __init__(self, point: str):
            self.point = point

        def text(self):
            return self.point

        def get_latex(self) -> str:
            return LatexElement.inject_variable(r"""\resumeItem{/ARG1/}""", self.point)

    def __init__(self, *bullet_points: str):
        self.bullet_points = [self.BulletPoint(s) for s in bullet_points]

    def text(self):
        return "\n".join([c.text() for c in self.bullet_points])

    def get_latex(self) -> str:
        return LatexElement.inject_variable(
            r"""\resumeItemListStart
            /ARG0/
            \resumeItemListEnd""",
            [bp.get_latex() for bp in self.bullet_points]
        )

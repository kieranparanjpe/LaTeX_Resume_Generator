from typing import List, Dict, Tuple

from LatexElements.latexelement import LatexElement


class TitleSection(LatexElement):
    class Locations(LatexElement):
        def __init__(self, locations: List[str]):
            self.locations = list(locations)

        def text(self) -> str:
            return " | ".join(self.locations)

        def get_latex(self) -> str:
            structure = LatexElement.inject_variable(r"\large {\scshape /ARG0/} \\ \vspace{1pt}",
                                                     self.locations, delimiter=r" $\&$ ")
            return structure

    class Links(LatexElement):

        class Link(LatexElement):
            def __init__(self, title: str, url: str | None = None):
                self.title = title
                self.url = url

            def text(self) -> str:
                return self.title

            def get_latex(self):
                if self.url is None:
                    return self.title
                return LatexElement.inject_variable(r"""\href{/ARG1/}{\underline{/ARG1/}}""",
                                                    self.url, self.title)

        def __init__(self, links: List[Link]):
            self.links = links

        def text(self) -> str:
            return " | ".join([l.text() for l in self.links])

        def get_latex(self) -> str:

            structure = LatexElement.inject_variable(r"""\normalsize  /ARG0/""",
                                                     self.links, delimiter=r" $|$ ")

            return structure

    def __init__(self, name: str, locations: List[str] = None, links: List[Links.Link] = None):
        self.name = name
        self.locations = TitleSection.Locations(locations if locations is not None else [])
        self.links = TitleSection.Links(links if links is not None else {})

    def text(self) -> str:
        return f"{self.name}\n{self.locations.text()}\n{self.links.text()}"

    def get_latex(self) -> str:
        structure = r"""
        \begin{center}
        \textbf{\Large \scshape /ARG1/} \\ \vspace{2pt}
        /ARG2/
        \end{center}"""
        return LatexElement.inject_variable(structure, self.name, self.locations.get_latex(), self.links.get_latex())

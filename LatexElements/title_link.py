from LatexElements.latexelement import LatexElement


class TitleLink(LatexElement):
    def __init__(self, title: str, link: str):
        self.title = title
        self.link = link

    def text(self) -> str:
        return f"{self.title}"

    def get_latex(self) -> str:
        title = ""
        if self.link != "":
            title = LatexElement.inject_variable(r"""\href{/ARG1/}{\underline{/ARG1/ \faExternalLink}}""",
                                                 self.link, self.title)
        else:
            title = self.title
        return title

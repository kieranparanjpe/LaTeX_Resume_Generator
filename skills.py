from typing import Callable

from LatexElements.latexelement import LatexElement

from LatexElements.skills_section import SkillsSection


def programming() -> SkillsSection.Skill:
    return SkillsSection.Skill(
        r"""Languages""",
        r"""C\#, Java, Python, JavaScript, TypeScript, SQL, Golang, Bash, HTML, CSS, C"""
    )


def programming_ml() -> SkillsSection.Skill:
    return SkillsSection.Skill(
        r"""Languages""",
        r"""Python, SQL, C\#, Java, JavaScript, TypeScript, Golang, Bash, HTML, CSS, C"""
    )


def frameworks() -> SkillsSection.Skill:
    return SkillsSection.Skill(
        r"""Frameworks/Tools""",
        r"""Git, Docker, PyTorch, React.js, Express.js, Unity, Linux, Firebase"""
    )


def frameworks_gamedev():
    return SkillsSection.Skill(
        r"""Frameworks/Tools""",
        r"""Git, Unity, Docker, PyTorch, React.js, Express.js, Linux, Firebase, Blender, Fusion 360"""
    )


def soft_skills() -> SkillsSection.Skill:
    return SkillsSection.Skill(
        r"""Soft Skills""",
        r"""Public Speaking, Leadership, Concise Communication, Quick Learning, Teamwork"""
    )


def skills(*function_names: Callable) -> LatexElement:
    all_skills = (function() for function in function_names)

    return SkillsSection(*all_skills)

from typing import Callable

from LatexElements.latexelement import LatexElement

from LatexElements.skills_section import SkillsSection


def programming() -> SkillsSection.Skill:
    return SkillsSection.Skill(
        r"""Languages""",
        r"""C\#, Java, Python, JavaScript, TypeScript, C++, SQL, Golang, Bash, HTML, CSS"""
    )


def programming_ml() -> SkillsSection.Skill:
    return SkillsSection.Skill(
        r"""Languages""",
        r"""Python, SQL, C\#, Java, JavaScript, TypeScript, C++, Golang, Bash, HTML, CSS"""
    )

def programming_reduced() -> SkillsSection.Skill:
    return SkillsSection.Skill(
        r"""Languages""",
        r"""Python, Java, C\#, TypeScript, C++"""
    )


def frameworks() -> SkillsSection.Skill:
    return SkillsSection.Skill(
        r"""Frameworks/Tools""",
        r"""Git, Spring Boot, Docker, PyTorch, MCP, Unity, Linux, Firebase, Splunk, Dynatrace"""
    )

def frameworks_ml() -> SkillsSection.Skill:
    return SkillsSection.Skill(
        r"""Frameworks/Tools""",
        r"""Git, PyTorch, Linux, Unity, Docker, ROS2, MCP, Fusion 360, MuJoCo"""
    )

def frameworks_robotics() -> SkillsSection.Skill:
    return SkillsSection.Skill(
        r"""Frameworks/Tools""",
        r"""Git, PyTorch, ROS2, Linux, Docker, Unity, Blender, Fusion 360, MCP, MuJoCo"""
    )


def frameworks_gamedev():
    return SkillsSection.Skill(
        r"""Frameworks/Tools""",
        r"""Git, Unity, Docker, PyTorch, Spring Boot, React.js, Express.js, Linux, Firebase, Blender, Fusion 360"""
    )


def soft_skills() -> SkillsSection.Skill:
    return SkillsSection.Skill(
        r"""Soft Skills""",
        r"""Public Speaking, Leadership, Concise Communication, Quick Learning, Teamwork"""
    )


def skills(*function_names: Callable) -> LatexElement:
    all_skills = (function() for function in function_names)

    return SkillsSection(*all_skills)

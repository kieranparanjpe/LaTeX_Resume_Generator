from typing import Callable

from LatexElements.experience_section import ExperienceSection
from LatexElements.latexelement import LatexElement


def the_verse() -> ExperienceSection.Experience:
    return ExperienceSection.Experience(
        (r"""Software Developer Intern""", r""""""),
        r"""Python, PyTorch, C\#, Unity, JavaScript""",
        r"""The Verse""",
        (r"""May 2024""", r"""August 2024"""),
        r"""Vancouver, BC / Remote""",

        r"""Developed a library that tracks breath rate in real-time using microphone input by training a convolutional neural network that takes mel spectrograms as input with PyTorch, achieving classification accuracy of 85\%.""",
        r"""Created an annotated breath audio dataset with over 50 minutes of breathing samples by implementing a web-app made with JavaScript and p5.js that records breath audio and uploads it to a Firebase storage bucket.""",
        r"""Ported and optimised the PyTorch model to run in C\# so it could be used in Unity, yielding a 5x speedup by converting the model to .ONNX, and analysing running time of specific functions using the Unity profiler.""",
        r"""Reverse engineered PyTorch's short time Fourier transform, spectrogram, and mel spectrogram by stepping through Python source code with the debugger and reproducing functionality in C\#.""",
        r"""Directed development by leading meetings with other interns working on the breath library."""

    )


def the_verse_ml() -> ExperienceSection.Experience:
    base = the_verse()
    base.update_job_title((r"""Machine Learning Intern""", ""))
    return base


def hack4i() -> ExperienceSection.Experience:
    return ExperienceSection.Experience(
        (r"""Software Developer""", r""""""),
        r"""Typescript, Express, PostgreSQL, Docker""",
        r"""Hack4Impact McGill""",
        (r"""April 2024""", r"""Current"""),
        r"""Montreal, QC""",
        r"""Developing the backend of an internal logistics website to be used by Welcome Collective Montreal.""",
        r"""Implemented JWT authentication middleware with Typescript."""

    )


def unity_dev() -> ExperienceSection.Experience:
    return ExperienceSection.Experience(
        (r"""Game Developer""", r""""""),
        r"""C\#, Unity, JavaScript, Firebase, 3D Math, Blender""",
        r"""KP Games""",
        (r"""September 2016""", r"""August 2023"""),
        r"""Vancouver, BC""",
        r"""Published 12 video games over 7 years on itch.io and Google Play using Unity and C\#, garnering over 1000 users total.""",
        r"""Developed an active ragdoll platforming game by applying Unity's physics engine to map rigged animations onto joints.""",
        r"""Implemented finite state machines and behaviour trees alongside Unity's NavMesh across projects to bolster NPC intelligence.""",
        r"""Designed and created a multiplayer first person shooter using Photon Unity Networking, including support for matchmaking, team game modes and free for all, automatic respawns, and synchronised movement, shooting and powerups.""",
        r"""Utilised Unity Scriptable Objects to power an inventory system for an RPG game."""

    )


def robotics() -> ExperienceSection.Experience:
    return ExperienceSection.Experience(
        (r"""Lead Software Engineer, Lead Robot Designer""", r""""""),
        r"""Java, OpenCV, Android Studio, CAD""",
        r"""FIRST Robotics (FIRST Tech Challenge \& FIRST Global Challenge)""",
        (r"""September 2019""", r"""April 2023"""),
        r"""Vancouver, BC""",
        r"""Captained my FIRST Tech Challenge robotics team to 1 world-championship qualification and multiple top 3 provincial finishes. Member of Team Canada for the 2022 FIRST Global Challenge in Geneva.""",
        r"""Enhanced autonomous performance by applying computer vision techniques like AprilTag detection and colour masking.""",
        r"""Implemented odometry localisation by combining encoder sensor data from dead wheels and measurements from an IMU.""",
        r"""Developed a custom PID solution to control robotic arms and lifts precisely."""

    )


def stemphilic() -> ExperienceSection.Experience:
    return ExperienceSection.Experience(
        (r"""Robotics Camp Instructor""", r""""""),
        r"""Leadership, Public Speaking, Communication""",
        r"""STEMphilic Education""",
        (r"""March 2022""", r"""March 2023"""),
        r"""Vancouver, BC""",
        r"""Taught LEGO robotics (Mindstorms and SPIKE Prime) to children aged 5-13 by teaching in a classroom setting.""",
        r"""Provided lesson plans tailored to student interest and ability, and offered one-on-one support for all students."""

    )


def experiences(*function_names: Callable) -> LatexElement:
    all_exp = (function() for function in function_names)

    return ExperienceSection(*all_exp)

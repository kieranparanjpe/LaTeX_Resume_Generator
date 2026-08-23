from typing import Callable

from LatexElements.experience_section import ExperienceSection
from LatexElements.latexelement import LatexElement

def autodesk_2() -> ExperienceSection.Experience:
    return ExperienceSection.Experience(
        (r"""Software Engineering Intern""", r""""""),
        r"""Python, TypeScript, MCP, Git, Docker""",
        r"""Autodesk""",
        (r"""May 2026""", r"""August 2026"""),
        r"""Montreal, QC""",
        r"""Delivered the MEDM MCP server, an \textbf{entirely new service}, and deployed it to production.""",
        r"""Implemented \textbf{over 25 new MCP tools}, allowing users to create, read, search, and update their 
        live data through a chat interface.""",
        r"""Developed a local MCP server that runs in the frontend application so the LLM can interact natively with 
        UI.""",
        r"""Integrated the MCP server with the AI assistant, accessible via a chat window in our Asset Management 
        frontend.""",
        r"""Wrote the entire testing framework for the service, bringing \textbf{test coverage from 0\% to 
        \textgreater 80\%}."""
    )

def autodesk() -> ExperienceSection.Experience:
    return ExperienceSection.Experience(
        (r"""Software Engineering Intern""", r""""""),
        r"""Java, TypeScript, Spring Boot, Git, Docker, AGILE, Splunk, JUnit""",
        r"""Autodesk""",
        (r"""January 2025""", r"""August 2025"""),
        r"""Montreal, QC""",
        r"""Implemented a \textbf{cycle detection algorithm} to ensure batches of commands can be topologically sorted by combining \textbf{depth first search} and a \textbf{greedy solution to the 'hitting set problem'}, resulting in \textbf{30\% fewer commands} generated and a \textbf{20\% speedup}.""",
        r"""Implemented a \textbf{REST client} for search by creating data models and handling errors, achieving \textbf{100\% test coverage}.""",
        r"""Added polymorphic-type filter support for search by calling our Types REST API to expand a single RSQL operator into multiple RSQL operators, maintaining 100\% test coverage.""",
        r"""Created an \textbf{end-to-end deploy test suite} for the search service containing \textbf{over 50 tests} to run \textbf{locally and in Jenkins} by syncing test data between local and staging, managing \textbf{run-time SQL injection} and writing \textbf{parameterised JUnit tests}.""",
        r"""Configured a \textbf{new Nginx Docker container} as a reverse proxy for routing in local search tests.""",
        r"""Contributed to \textbf{critical search features} (listed above), shipped in \textbf{5 client deliverables over 4 months}.""",
    )

def the_verse() -> ExperienceSection.Experience:
    return ExperienceSection.Experience(
        (r"""Software Engineering Intern""", r""""""),
        r"""Python, PyTorch, C\#, Unity, JavaScript""",
        r"""The Verse""",
        (r"""May 2024""", r"""August 2024"""),
        r"""Vancouver, BC / Remote""",

        r"""Developed a library that tracks breath rate in real-time using microphone input by training a \textbf{convolutional neural network} that takes mel spectrograms as input with \textbf{PyTorch}, achieving classification accuracy of 85\%.""",
        r"""Created a breath audio dataset with over 50 minutes of annotated breathing samples by implementing a web-app made with \textbf{JavaScript and p5.js} that records breath audio and uploads it to a \textbf{Firebase storage bucket}.""",
        r"""Ported and \textbf{optimised the PyTorch model to run in C\#} to be used in Unity, yielding a \textbf{5x speedup} by converting the model to .ONNX, and analysing the running time of specific functions using the \textbf{Unity profiler}.""",
        r"""Reverse engineered PyTorch's short time Fourier transform, spectrogram, and mel spectrogram by stepping through PyTorch source code with a debugger and reproducing its functionality in C\#.""",
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
        r"""\textbf{Published 12 video games over 7 years} on itch.io and Google Play using Unity and C\#, garnering \textbf{over 1000 users} total.""",
        r"""Developed an active ragdoll platforming game by applying Unity's \textbf{physics engine} to map \textbf{rigged animations} onto joints.""",
        r"""Implemented \textbf{finite state machines} and \textbf{behaviour trees} alongside Unity's \textbf{NavMesh} across projects to bolster NPC intelligence.""",
        r"""Designed and created a \textbf{multiplayer first person shooter} using Photon Unity Networking, including support for \textbf{matchmaking}, \textbf{team game modes and free for all}, \textbf{automatic respawns}, and \textbf{synchronised movement}, \textbf{shooting and powerups}.""",
    )


def robotics() -> ExperienceSection.Experience:
    return ExperienceSection.Experience(
        (r"""Lead Software Engineer, Lead Robot Designer""", r""""""),
        r"""Java, OpenCV, Android Studio, CAD""",
        r"""FIRST Robotics (FIRST Tech Challenge \& FIRST Global Challenge)""",
        (r"""September 2019""", r"""April 2023"""),
        r"""Vancouver, BC""",
        r"""Captained my FIRST Tech Challenge robotics team to \textbf{1 world-championship qualification} and multiple top 3 provincial finishes. Selected to represent \textbf{Team Canada} for the 2022 FIRST Global Challenge in Geneva.""",
        r"""Enhanced autonomous performance by applying \textbf{computer vision} techniques like AprilTag detection and colour masking.""",
        r"""Implemented \textbf{odometry localisation} by combining encoder sensor data from dead wheels and measurements from an IMU.""",
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

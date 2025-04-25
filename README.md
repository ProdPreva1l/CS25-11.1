# The Parade
This is a silly little game made for my comp sci course.

I would have liked to add a proper story line but decided to design the project to be extensible
for the sake of showing an example of my knowledge of OOP and design patterns.

You can easily add new levels (and stages), creatures and items to the game!
While the character system isn't designed to add more, you could if you wanted to.

---

# How to Play
1. `pip install`
2. `py main.py`

---

# Product Requirements (PRD)

## 1. Overview

**Product Name**: The Parade

**Description**:
The Parade! Choose your adventurer, 
go around the world slaying progressively harder creatures and level up your character!

**Target Audience**:
- All Ages
- People bored while in school or a meeting
- RPG/Adventure Game Enjoy-ers

---

## 2. Product Problem Statement
**Challenges Addressed**:
- **Hardware Requirements**: Many games have heavy hardware requirements, which many people cannot meet.
- **Competitive Market**: The game industry is very competitive with most games needing backing of multi-million (if not -billion) dollar companies to gain traction.
- **Skill Gap & Ceiling**: Games need to have a good balance between easy and challenging, and they need room for the player to practice and get better.

---

## 3. Functional Requirements
| Requirement          | Plan to achieve the goal                                                                               |
|----------------------|--------------------------------------------------------------------------------------------------------|
| Easy to play & learn | To make the game easy to learn there is a tutorial level</br>which covers core components of the game  |
| Everyone can play    | People of all ages and backgrounds should be able to easily play the game.                             |
| Progression System   | Players level up and unlock new abilities and gear by defeating progressively harder enemies.          |

---

## 4. Non-Functional Requirements
| Requirement                  | Plan to Achieve the Goal                                                                  |
|------------------------------|-------------------------------------------------------------------------------------------|
| Cross-Platform Compatibility | Ensure the game runs smoothly on any OS (Windows, macOS, Linux).                          |
| Low System Requirements      | Use lightweight assets and optimized code to support older or low-end hardware.           |
| Fast Load Times              | Minimize asset sizes and external dependencies to reduce loading time on all connections. |

---

# Game Flow
```mermaid
flowchart TD
    %% Nodes
    GameStart([Game Start])
    MainMenu{Main Menu}
    ResetData((Reset Data))
    GetLevel[Get Current Level]
    LevelExists{Level Exists}
    PlayoutLevel[Playout Level]
    SimpleEncounter[Simple Encounter]
    VisitAdventure[Visit Adventure PoI]
    ComplexEncounter[Complex Encounter]
    VisitGeneral[Visit General PoI]
    IncrementLevel[Increment Level]
    WinGame([Win Game])

    %% Relationships
    GameStart --> MainMenu
    MainMenu -->|Create New Game| ResetData
    MainMenu -->|Load Existing Game| GetLevel
    ResetData --> GetLevel

    %% Game Loop
    GetLevel --> LevelExists
    LevelExists -->|true| PlayoutLevel
    LevelExists -->|false| WinGame
    IncrementLevel --> GetLevel

    %% Playout Level Flow
    PlayoutLevel --> SimpleEncounter
    SimpleEncounter --> VisitAdventure
    VisitAdventure --> ComplexEncounter
    ComplexEncounter --> VisitGeneral
    VisitGeneral --> IncrementLevel

    %% Styling
    style GameStart fill:#f9f,stroke:#333,stroke-width:2px
    style WinGame fill:#f9f,stroke:#333,stroke-width:2px
    style MainMenu fill:#ff9,stroke:#333,stroke-width:2px
    style ResetData fill:#ccf,stroke:#333,stroke-width:2px
    style PlayoutLevel fill:#cfc,stroke:#333,stroke-width:2px
```
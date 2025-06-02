### 📅 Date: 2025-05-12 - Josh

This is the first entry. I originally started this project 6 years ago as a side project. So we skip some stuff in our entries.

* Revisited my old codebase and brought it into a more modern structure.
* Cleaned up the core game logic and made it extensible in preparation for the assignment requirements.
* Set up a GitHub repository to track progress and version control.
* Configured PyCharm for my development environment.
* Encountered friction converting older code into something cleaner and more modular.
* Managed years-old logic that wasn’t very readable.
* Solved this by refactoring large chunks and applying design patterns like IDD (interface driven development) & hexagonal infrastructure.
* Planned to start designing the question/fight interaction system.
* Aimed to finalise the player and enemy stat system.
* Intended to flesh out the PRD and documentation as required for the assignment.

It’s been refreshing to see how far I’ve come since I originally wrote this. While the original code was very raw, it provided a good base to build upon.

**Resources Used**:

* PyCharm IDE
* GitHub
* Old codebase from personal archive
* Python OOP best practices articles

---

### 📅 Date: 2025-05-15 - Josh

Made significant progress implementing the question interaction system and integrating it with stat progression.

* Questions now have weight values, which scale the upgrades if answered correctly.
* Implemented random upgrade distribution: players either receive a stat boost or an item.
* Began rough implementation of stage and level systems.
* Improved repository and entity design for modularity.
* Faced difficulty balancing the upgrades and determining win conditions for fights.
* Used simple simulation runs to test balance and tweaked probabilities manually.
* Planned to finalise fight logic and implement stat checks.
* Intended to begin developing different stages and integrate them into the level loop.
* Aimed to polish game loop and player feedback.

The randomness of upgrades adds an interesting layer of replayability. Balancing is tricky but rewarding when it works well.

**Resources Used**:

* PyCharm IDE
* GitHub
* Python documentation on `random` and `dataclass`

---

### 📅 Date: 2025-05-19 - Josh

The core game loop is now complete. I spent this week focusing on polish, fixing edge cases, and making the flow from question to fight feel seamless.

* Implemented the full fight stage after questions.
* Added logic to check if player stats/items are strong enough to win fights.
* Created a loss/restart flow if the player is too weak to continue.
* Hooked fight outcomes into the level progression system.
* Ran into an issue where certain questions weren't triggering upgrades properly.
* Traced it back to a dictionary mutation bug—resolved it by refactoring upgrade application logic and adding debug logs.
* Planned to expand the pool of questions and create categories by difficulty.
* Intended to implement stat-scaling logic per level to keep challenge consistent.
* Aimed to start work on general Points of Interest (PoIs) for the exploration layer.

Seeing the full cycle—question → upgrade → fight → win/lose—is satisfying. It’s starting to feel like a real game now.

**Resources Used**:

* PyCharm IDE
* GitHub
* Stack Overflow (for Python dict mutation issues)
* Python logging module documentation

---

### 📅 Date: 2025-05-22 - Josh

Focused on building out content and tying in the final parts of the gameplay experience.

* Added more questions with varied weights and custom effects.
* Implemented the General PoI and Adventure PoI systems to add variety.
* Hooked up level progression with a working end state and reset mechanism.
* Completed draft version of the in-game tutorial and help text.
* Noticed question balance was off—easy questions gave too strong upgrades.
* Addressed this by adjusting the weight curve and making high-weight upgrades rarer.
* Planned to add polish to the UI/UX (text formatting, spacing, readability).
* Intended to create final version of the documentation and walkthrough.
* Considered adding a basic save/load mechanic for fun (non-essential).

The modular design really paid off. Adding new content now takes minutes. I'm glad I emphasised extensibility from the start.

**Resources Used**:

* PyCharm IDE
* GitHub
* Python’s built-in `textwrap` module for display formatting
* Game design blogs on question balancing

---

### 📅 Date: 2025-05-26 - Josh

This week I worked on polishing and final touches before considering the game “ready” for submission.

* Added final polish to text-based UI: better formatting, spacing, and screen clarity.
* Finished writing and embedding tutorial logic in the intro level.
* Planned to finish all documentation including PRD, data dictionary, and flowchart.
* Intended to conduct final internal playtest session to make sure nothing is broken.
* Aimed to package up the project for submission and write up submission instructions.

**Resources Used**:

* PyCharm IDE
* GitHub
* Online ASCII art generator
* Personal playtesting feedback

---

### 📅 Date: 2025-05-29 - Josh

Final round of testing, documentation, and preparing everything for submission.

* Finished PRD document, data dictionary, flowchart, and this process journal.
* Did extensive internal testing and bug fixes.
* Rewrote several in-game tooltips and adjusted level pacing for smoother difficulty curve.
* Added code comments and cleaned up structure for readability and extensibility.
* Had trouble interpreting some older parts of the code during cleanup.
* Solved this by re-documenting systems and renaming vague variables to be more descriptive.
* Planned to submit the final package via the platform.
* Intended to celebrate finishing a project I started four years ago!

I never thought I would come back to this project, but it has been a fun journey fixing it up.

**Resources Used**:

* PyCharm IDE
* GitHub
* Markdown editors for documentation
* Self-written notes and TODOs from earlier stages

---

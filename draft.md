# Termitaria — 3-minute demo script

Target length: 2:55. Spoken English, about 410 words, with room to breathe on the demo. Frame: 1920×1080. The app recordings are 1440×900. Fit them to the height of the frame and leave a slim side margin in `#f4f4f5`.

Voice is recorded later. The four example animations are silent and already timed to their beats.

This is a software project. The hackathon asks for the key modules in action. That is the chat, the plan bar, and the knowledge graph. There is no hardware shot.

## Picture

- Palette, matching the app: white `#ffffff`, rail `#f4f4f5`, ink `#222222`, accent `#3390ec`, chat wash `#d7e4ee`.
- Termite sprites in `resources/`: `reproductive.bmp` is the Principal Investigator, `worker.bmp` is the collector, the idea generator, and the experiment designer, `soldier.bmp` is the Skeptical Reviewer.
- On-screen captions in the animations are short. The paragraphs below are the voice.

## Timeline

| Time | Picture | Source |
| --- | --- | --- |
| 0:00–0:16 | Animation `Problem` | `problem.mp4` |
| 0:16–0:38 | Animation `Colony` | `colony.mp4` |
| 0:38–0:56 | Animation `CheckIn` | not rendered; storyboard below |
| 0:56–1:18 | Animation `Memories` | `memories.mp4` |
| 1:18–1:30 | Animation `Title` | not rendered; storyboard below |
| 1:30–1:52 | Animation `Stack` | `stack.mp4` |
| 1:52–2:00 | Copper Desk template card | marketing webm 10.4–14.4 |
| 2:00–2:08 | Autoresearch template, then Create | autoresearch webm, two cuts |
| 2:08–2:27 | General: roster, task, reviewed plan | autoresearch webm, two cuts |
| 2:27–2:42 | Artifacts, then the knowledge graph | autoresearch webm 46.2–57.1 |
| 2:42–2:55 | Animation `Close` | not rendered; storyboard below |

## Voice and action

### 0:00–0:16 · Problem

One agent icon. Four bubbles appear one after another and stay in a row: answer questions, analyze problems, propose a plan, draft a report. That row drops onto the same icon until the bubbles overlap. Then four icons stand in a row, and each bubble sits on its own icon.

> One agent can answer questions, analyze information, propose a plan, or draft a report. But complex projects require many of these jobs at once. Asking one agent to do everything in a single conversation makes the work harder to steer, inspect, verify, and build upon.

### 0:16–0:38 · Colony

A rounded box labeled user stands on a line labeled Surface. Under the line, five sprites on light cards: Principal Investigator, Literature Collector, Idea Generator, Experiment Designer, Skeptical Reviewer. One bubble, Research, moves from the user to the investigator. The investigator then sends Gap scan, Hypothesis, Experiment, and Review to the other four. Under the team, four dots are labeled literature gap scan, hypothesis, experiment design, and method review.

> Termitaria gives a complex project a team. A user sets the direction from the surface. beneath it, specialized agents carry out distinct responsibilities. Their work becomes shared project knowledge rather than disappearing into one long chat.

### 0:38–0:56 · CheckIn

Storyboard, same style as Colony. A row of four stages: literature gap, hypothesis, experiment design, methods review. A user arrow cuts into methods review and points at the reviewer sprite. Then a plain conversation panel: the user line is in that agent's thread only. The other four stages stay put.

> The work is not a straight line. You can check a decision, or ask one specialist a follow-up, without stopping the rest of the team. You open that agent's conversation, the way you would check in with one teammate.

Neither recording opens a 1:1 chat. Keep this beat as animation. The Chats list in the Autoresearch file can flash the roster, and it does not replace this beat.

### 0:56–1:18 · Memories

Three chat boxes appear: What is insulin?, It lowers blood sugar, and A medical paper. They line up into a knowledge graph. The links read answered by and drawn from. Five notebooks sit beside it, one per agent. An arrow from the collector's notebook stops at the reviewer's notebook.

> A project changes when new evidence shows up. Termitaria keeps two memories apart. The knowledge graph holds the project's evidence and the links between facts. Each agent keeps its own notebook: its role, its rules, and what it did last time. One agent cannot read another's notes.

### 1:18–1:30 · Title

Storyboard. The five sprites face a small mound of the same blocks. Title: Termitaria. Tagline under it: Command on the surface. Agents work in the tunnels. The colony remembers.

> No single member holds the whole plan. Each one does its job, keeps what it learned, and the colony builds the result. That is Termitaria.

### 1:30–1:52 · Stack

Four layers, top to bottom: Next.js client, Go control plane and NATS JetStream, Python workers, Nebius Token Factory. Two chips on the bottom layer. Everyday turns use `nvidia/nemotron-3-super-120b-a12b`. The skeptical review uses `nvidia/Nemotron-3-Ultra-550b-a55b`. A worker sprite points at Super. The reviewer sprite points at Ultra.

> The app is the surface. A Go control plane routes the work. Python workers call NVIDIA Nemotron 3 through Nebius Token Factory. Everyday turns use Nemotron 3 Super. The skeptical review uses Nemotron 3 Ultra. The same spec runs another team, with no new code.

### 1:52–2:00 · Copper Desk card

File: `demo_video/artifacts/marketing_2026-10-26_21_04.webm`

Play 10.4–14.4 (4.0s), muted. At 10.4 the Team step is up. The cursor hits the copper-desk card around 11.4. By 12.9 the SwarmSpec reads `name: copper-desk`, with Desk Lead, Market Researcher, and Reviewer. Just after 14.0 the view leaves for the Knowledge step, so end the cut at 14.4.

Lower third: Same harness. Copper Desk writes a sourced market brief.

> Copper Desk is that second team: a desk lead, a researcher, and a reviewer.

### 2:00–2:08 · Autoresearch, create the team

File: `demo_video/artifacts/autoresearch_2026-10-26_21_02.webm`

Jump cut, about 8 seconds together.

- 7.8–10.0 (2.2s). The autoresearch card is selected and the SwarmSpec fills with Principal Investigator, Literature Collector, and the rest. At 7.0 the card is not selected yet. At 10.0 the view has already moved on, so stop at 10.0.
- 20.0–25.8 (5.8s). The seed line is already in the list: "Research question: Does appending a short, definition-only glossary…". The cursor hits Create just before 22.0. At 22.0 the project is open: five chats in the list, and the plan bar shows literature gap scan, hypothesis, experiment design, methods review. By 24.0 General is open.

Lower third: SwarmSpec becomes the team.

### 2:08–2:27 · Autoresearch, the channel

Same file. Skip 25.8–31.6. That stretch is the long prompt being typed, and the model menu reads DeepSeek-V4.1-Flash.

- 22.4–25.6 is already inside the create cut above (the roster). Do not play it twice.
- 31.6–46.2 (14.6s). At 31.6 the user message is in General and a thinking bubble is up. The message asks for a glossary study on MedQuAD, in the order literature gap, hypothesis, experiment design, methods review. By 36.0 the Principal Investigator has posted "Reviewed experiment plan", and the plan bar marks literature gap, hypothesis, and experiment design done. The same plan stays on screen through 46.0, when the cursor moves toward Artifacts.

What this take does not show: separate bubbles for the collector, the idea generator, the designer, and the reviewer. The roster lists them. The message on screen is the investigator's plan. Hold this frame if the voice needs the full 22 seconds. Do not narrate four speeches the picture does not hold.

The model name sits in the composer, bottom left. Crop about 80 pixels off the bottom of the 900-pixel frame, or cover that bar with the lower third. Judges read Nemotron on the Stack card. They should not read DeepSeek here.

Lower third: The investigator returns a reviewed experiment plan.

> Here is Autoresearch on a real task. The question is whether a definition-only glossary improves claim-level faithfulness on MedQuAD. The investigator posts a reviewed experiment plan, and the plan bar moves forward.

### 2:27–2:42 · Artifacts, then Knowledge

Same file, 46.2–57.1 (10.9s). Hold the graph for about one extra second in the edit so this block can run to 2:42.

- 46.2–50.6. Artifacts is open. The page says "No artifacts". This take did not write a report file. The lower third must not say the plan landed here. The plan is the message in General.
- 50.6–55.6. Knowledge graph. The header reads 1 document, 0 claims. On screen: a MedQuAD node, a biomedical question-answering node, Qwen2.5-7B-Instruct, and a node for the research question.
- 55.6–57.1. The view returns to Chats. The roster is still there. Use this only as a button back, not as a new idea.

Lower third on the graph: The question and MedQuAD land in the knowledge graph.

> The reviewed plan stays in the channel. The knowledge graph keeps the question, MedQuAD, and the model named in the brief.

### 2:42–2:55 · Close

Storyboard. Return to the title mound. Then three lines, one at a time: Nebius Token Factory, NVIDIA Nemotron 3 Super and Ultra, Termitaria.

> Command on the surface. Agents work in the tunnels. The colony remembers.

## Example animations

Rendered at 1920×1080, 30 fps, silent, from this folder:

```bash
.venv/bin/manim render problem.py Problem -r 1920,1080 --fps 30 --media_dir media
.venv/bin/manim render colony.py Colony -r 1920,1080 --fps 30 --media_dir media
.venv/bin/manim render memories.py Memories -r 1920,1080 --fps 30 --media_dir media
.venv/bin/manim render stack.py Stack -r 1920,1080 --fps 30 --media_dir media
```

Copies also sit next to the scene files: `problem.mp4`, `colony.mp4`, `memories.mp4`, `stack.mp4`.

`CheckIn`, `Title`, and `Close` stay as storyboards above. They reuse the Colony sprites and the title line.

## Before YouTube

Re-record the model menu with Nemotron selected before upload, if a crop is not enough. The Stack scene names Token Factory, Super, and Ultra either way. A later Autoresearch take can also hold each specialist's turn, and it can write a real file into Artifacts. This cut uses the pictures we already have.

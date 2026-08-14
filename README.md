# ReadLayer

**Understand the text you’re reading, without losing your flow.**

ReadLayer is an AI-powered reading assistant designed to bridge the gap between complex text and deep understanding. Instead of switching tabs or prompting a chatbot, ReadLayer aims to provide contextual explanations for difficult terms and phrases directly where you are reading.

## The Concept

When reading technical documentation, academic papers, or classic literature, "Context Switching" is a major hurdle. Every time you leave a text to look up a word, you lose your reading momentum. 

ReadLayer is being built to:
- **Preserve Flow:** Get explanations without leaving the page.
- **Provide Context:** Understand how a word works *specifically* in the sentence you are reading.
- **Simplify Learning:** Act as a "lens" that clarifies complex language in real-time.

## Current Project Status 🚧

This project is currently in **active development** as I learn the modern web stack.

- **Frontend:** Built with **React** and **Vite**. I am currently mastering hooks like `useState` to manage the UI state and text inputs.
- **Backend:** The core logic is powered by **Python** and the **Gemini API**. I have successfully built a terminal-based prototype that identifies complex terms and generates explanations.
- **The Bridge:** I am currently working on connecting the React frontend to the Python backend to move beyond the terminal.

## Features (Current & Planned)

- [x] **Minimalist Reader UI:** A clean, distraction-free environment for pasting and reading text.
- [ ] **Contextual Highlighting:** (In Progress) Automatically identifying "friction points" in the text.
- [ ] **Explanation Cards:** Inline pop-overs that explain terms without moving the text layout.
- [ ] **Recursive Learning:** The ability to click a word *inside* an explanation to go even deeper.

## Tech Stack

- **Frontend:** React.js, Vite, CSS3
- **Backend:** Python (FastAPI/Flask planned)
- **AI Model:** Google Gemini API (via Prompt Engineering)

## Why ReadLayer?

While general-purpose AI (like ChatGPT) is powerful, it often requires "managing" a conversation. ReadLayer is designed to be a **tool, not a chat.** It doesn't want to talk to you; it just wants to help you read. By focusing purely on the relationship between the reader and the text, ReadLayer aims to make deep reading more accessible.

## Development Setup

*Note: This project is in early development.*

1. **Frontend:**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```
2. **Backend (CLI Prototype):**
   ```bash
   cd backend
   python main.py
   ```

## About the Developer

I am a student developer moving from traditional PHP development into the React ecosystem. This project serves as my primary "learning lab" for:
- State management in React.
- Building and consuming APIs.
- Human-centered UI/UX design.

---
GitHub: [liljaydi](https://github.com/liljaydi)

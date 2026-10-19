# Start Here

This repository is your working project starter. It works with any AI coding agent (Cursor, Claude Code, Codex, GitHub Copilot, Gemini CLI, and others). See `docs/agent-setup.md` for your agent.

Before asking your agent to build anything:

1. Read `QUICKSTART.md`.
2. Read `SECURITY.md`.
3. Complete `intake/problem-intake.md`.
4. Paste the prompt in `prompts/START-AGENT-HERE.md` into your agent. It tells the agent to read `AGENTS.md` and the policies in `policies/`, and to explain them to you.
5. Ask your agent to review your intake form. It may ask lots of questions. Answer in your own words. If you do not know an answer, say so and ask the agent to help you work it out.
6. Create your GitHub repository with the name of your application (keep it **private**). Give the repository's `.git` address to your agent and tell it to use that repository from now on. The agent will ask before it pushes anything.
7. Open the `scripts/` folder and find the setup script for your operating system. Add it to your agent's chat and ask whether you have all the software the project needs. Ask it to install project dependencies into a virtual environment (such as `.venv`), which protects your computer from software conflicts. The agent must explain each install and wait for your approval; it may need you to type a `sudo` or administrator password yourself.
8. Ask your agent to install Spec Kit for your agent (see `docs/agent-setup.md`) and to start the full Spec Kit workflow by creating the project's constitution.
9. Ask your agent to create a milestone plan, and after you approve it, the milestones and issues in your GitHub repository.
10. Ask your agent to push code and releases for each version to GitHub for safekeeping.
11. Ask your agent to create `docs/glossary.md` for the terms and definitions used in your application.
12. Ask your agent to update `README.md` and `CHANGELOG.md` for every minor and major release, and to use the changelog to write the GitHub release notes.
13. Ask your agent what needs to be done to start implementation. It should begin the first spec with you.

**Do not put real case data into your agent, GitHub, issues, logs, screenshots, test files, or sample data.** For a conference, workshop, or course, all development uses synthetic data (Tier T0/T1 in `docs/test-data-handling.md`).

This approach will get you to a v1.0.0 minimum viable product for your idea.

Your goal is to team with your AI agent to test your application. The agent can run automated tests, and you test the tool separately as an investigator would (`docs/manual-test-checklist.md`), then tell the agent what needs to be improved.

Ask your agent to search GitHub for projects similar to what you want to build, and for building-block technologies that would help. Ask it to look at the Linux Foundation and standards bodies so you build on open technologies and established data standards in your field. If you use code from other GitHub repositories or open-source projects, make sure your agent checks that the licenses allow your use. Don't reinvent the wheel; reshape the wheels that already exist to fit your exact purpose. It is usually faster and cheaper.

As you get closer to v1.0.0, you can ask your agent to remove the references to this template and the training course, and to turn the repository into a professional development project. Ask it to improve the policies in `policies/` for your project and agency (including your jurisdiction's security rules) and to run `python3 scripts/sync_agent_rules.py` afterwards. This helps you move from a v1.0.0 demonstrable MVP built in a class to a v2.0.0+ operational version. Have your agent help you plan milestones beyond v1.0.0 using GitHub milestones and issues, create custom issue labels that fit your project, use GitHub issue types, and set up a GitHub Project (a planning board, not a repository) to organize your work and collaborators.

This is a learning process. You will keep getting better as you design and build more of your own applications or extend existing ones. Email support@projectvic.zendesk.com if you need help or if you found this useful. If you see something you don't understand, ask your agent; it can explain anything at any level. For example: "I am a prosecutor and I am not technical. Please explain this word, phrase, or code in plain, non-technical language: (paste it here)". You can also ask it to answer in your first language.

Finally, Project VIC International is a nonprofit. If you find this useful for your mission, please share it with your colleagues and consider making a donation to help sustain our work for crimes-against-children investigators worldwide: https://secure.givelively.org/donate/project-vic-international-inc

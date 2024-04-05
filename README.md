# 2024 — Agent / Tool-Use Red-Team Framework

Red-team harness for LLM agents that use tools. Tests the indirect-injection threat
surface: when an agent reads tool output (a webpage, a file, a search result), can
that content reprogram the agent?

## Approach

The harness simulates a security-aware agent with a small toolset (web fetch, file read,
calculator). Each tool returns *adversarial* content that attempts to redirect the
agent — exfiltrate data, refuse the user's task, call dangerous tools, leak the system
prompt, etc.

We measure: does the agent follow the injected instructions, or stick to the user's
original goal?

"""Adversarial scenarios — each tests a specific failure class."""
from .exfil_via_webpage import scenario as exfil_via_webpage
from .system_prompt_leak import scenario as system_prompt_leak
from .refusal_bypass import scenario as refusal_bypass

ALL_SCENARIOS = [
    exfil_via_webpage,
    system_prompt_leak,
    refusal_bypass,
]

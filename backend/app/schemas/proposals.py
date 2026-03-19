from collections.abc import AsyncIterator
from typing import Literal

from pydantic import BaseModel, Field


Tone = Literal["professional", "conversational", "technical"]
Length = Literal["concise", "detailed"]


class ProposalSection(BaseModel):
    key: str
    title: str
    content: str


class ProposalGenerationRequest(BaseModel):
    brief_content: str = Field(min_length=1)
    structured_fields: dict[str, str] = Field(default_factory=dict)
    tone: Tone = "professional"
    length: Length = "concise"


class ProposalGenerationResult(BaseModel):
    sections: list[ProposalSection]
    tone: Tone
    length: Length
    source: str


class ProposalStreamEvent(BaseModel):
    event: Literal["section", "complete"]
    payload: ProposalSection | ProposalGenerationResult


ProposalStream = AsyncIterator[ProposalStreamEvent]

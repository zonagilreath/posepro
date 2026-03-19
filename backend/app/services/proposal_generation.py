import asyncio
from collections.abc import AsyncIterator

from app.schemas.proposals import (
    ProposalGenerationRequest,
    ProposalGenerationResult,
    ProposalSection,
    ProposalStreamEvent,
)


class ProposalGenerationService:
    """Thin structured generation stub that can later be swapped for Claude-backed logic."""

    section_titles = [
        ("project_understanding", "Project Understanding"),
        ("proposed_approach", "Proposed Approach"),
        ("scope_deliverables", "Scope & Deliverables"),
        ("timeline", "Timeline"),
        ("pricing", "Pricing"),
        ("qualifications", "Qualifications"),
    ]

    def build_result(self, payload: ProposalGenerationRequest) -> ProposalGenerationResult:
        context_summary = ", ".join(
            f"{key}: {value}" for key, value in payload.structured_fields.items() if value
        ) or "No structured fields provided"

        sections = [
            ProposalSection(
                key=key,
                title=title,
                content=self._build_section_copy(
                    section_title=title,
                    brief_content=payload.brief_content,
                    context_summary=context_summary,
                    tone=payload.tone,
                    length=payload.length,
                ),
            )
            for key, title in self.section_titles
        ]

        return ProposalGenerationResult(
            sections=sections,
            tone=payload.tone,
            length=payload.length,
            source="stubbed-structured-generator",
        )

    async def stream_result(self, payload: ProposalGenerationRequest) -> AsyncIterator[ProposalStreamEvent]:
        result = self.build_result(payload)

        for section in result.sections:
            await asyncio.sleep(0.15)
            yield ProposalStreamEvent(event="section", payload=section)

        yield ProposalStreamEvent(event="complete", payload=result)

    def _build_section_copy(
        self,
        *,
        section_title: str,
        brief_content: str,
        context_summary: str,
        tone: str,
        length: str,
    ) -> str:
        detail_line = (
            "Keep the writing compact and decision-oriented."
            if length == "concise"
            else "Expand with more implementation detail and rationale."
        )
        return (
            f"{section_title} draft for a {tone} proposal. "
            f"Client brief: {brief_content[:280].strip()}. "
            f"Structured context: {context_summary}. "
            f"{detail_line}"
        )

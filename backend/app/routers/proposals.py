import json
from typing import Annotated

from fastapi import APIRouter, Header
from fastapi.responses import StreamingResponse

from app.schemas.proposals import ProposalGenerationRequest
from app.services.proposal_generation import ProposalGenerationService

router = APIRouter(prefix="/proposals", tags=["proposals"])
proposal_service = ProposalGenerationService()


@router.post("/generate/preview")
def generate_preview(payload: ProposalGenerationRequest):
    return proposal_service.build_result(payload)


@router.post("/generate")
async def generate_proposal_stream(
    payload: ProposalGenerationRequest,
    last_event_id: Annotated[str | None, Header()] = None,
) -> StreamingResponse:
    async def event_stream():
        if last_event_id:
            yield f": resume requested from event id {last_event_id}\n\n"

        index = 0
        async for event in proposal_service.stream_result(payload):
            index += 1
            body = json.dumps(event.payload.model_dump(mode="json"))
            yield f"id: {index}\nevent: {event.event}\ndata: {body}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")

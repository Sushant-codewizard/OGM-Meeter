from __future__ import annotations
import logging

logger = logging.getLogger("meetingbot.diarizer")

def diarize(wav_path: str) -> list[dict]:
    """Lightweight dummy diarization to bypass local heavy pyannote model."""
    logger.info("event=diarization_skipped_for_lightweight_mode")
    
    # Clean fallback list return kar rahe hain jisse pipeline crash na ho
    return [
        {
            "speaker": "SPEAKER_00",
            "start_ms": 0,
            "end_ms": 10000
        }
    ]

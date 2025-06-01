# CHAOS Framework - Agentic AI Training Data Generator
__version__ = "1.0.0"

from .chaos_generator import CHAOSGenerator as BasicGenerator
from .chaos_generator_progressive import CHAOSGenerator, GeminiEnhancedGenerator
from .convert_to_training_data import (
    chaos_to_simple_qa,
    chaos_to_thought_process,
    chaos_to_openai_chat,
    convert_batch_for_training,
)

__all__ = [
    "CHAOSGenerator",
    "BasicGenerator",
    "GeminiEnhancedGenerator",
    "chaos_to_simple_qa",
    "chaos_to_thought_process",
    "chaos_to_openai_chat",
    "convert_batch_for_training",
]

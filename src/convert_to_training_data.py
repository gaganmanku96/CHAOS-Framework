"""
Convert CHAOS scenarios to actual training data formats
This shows exactly how to use the generated data for training
Includes PEFT-compatible formats like Alpaca for small language model fine-tuning
"""

import json
from typing import List, Dict, Any
from dataclasses import dataclass, asdict


@dataclass
class AlpacaEntry:
    """Alpaca format training entry for PEFT"""

    instruction: str
    input: str = ""
    output: str = ""


def chaos_to_alpaca_format(chaos_scenario: Dict[str, Any]) -> AlpacaEntry:
    """Convert CHAOS scenario to Alpaca format for PEFT training"""

    # Create instruction based on scenario and constraints
    instruction = (
        f"You are an AI assistant helping with a {chaos_scenario['difficulty']} "
        f"difficulty task. {chaos_scenario['scenario']} {chaos_scenario['constraints']}"
    )

    # Create context input with available tools
    tools_list = ", ".join(
        [
            f"{name}: {desc}"
            for name, desc in chaos_scenario["tools_available"].items()
        ]
    )
    input_text = f"Available tools: {tools_list}"

    # Create response with internal reasoning and actions
    response_parts = []

    # Add internal reasoning
    if chaos_scenario.get("internal_dialogue"):
        response_parts.append("**Internal Analysis:**")
        for dialogue in chaos_scenario["internal_dialogue"]:
            if "voices" in dialogue:
                for voice, thought in dialogue["voices"].items():
                    response_parts.append(f"- {voice.title()}: {thought}")
                response_parts.append(
                    f"Resolution: "
                    f"{dialogue.get('resolution', 'Proceeding with plan')}"
                )
                response_parts.append(
                    f"Confidence: {dialogue.get('confidence', 70)}%"
                )

    # Add confidence trajectory
    if chaos_scenario.get("confidence_trajectory"):
        response_parts.append(
            f"\n**Confidence Progression:** "
            f"{chaos_scenario['confidence_trajectory']}"
        )

    # Add reality breaks and adaptations
    if chaos_scenario.get("reality_breaks"):
        response_parts.append("\n**Adaptation Moments:**")
        for break_event in chaos_scenario["reality_breaks"]:
            response_parts.append(
                f"- Discovery: {break_event.get('discovery', 'Unexpected situation')}"
            )
            response_parts.append(
                f"- Adaptation: {break_event.get('adaptation', 'Adjusting approach')}"
            )

    # Add final outcome
    if chaos_scenario.get("final_outcome"):
        outcome = chaos_scenario["final_outcome"]
        response_parts.append("\n**Final Outcome:**")
        response_parts.append(
            f"- Success Level: {outcome.get('success_level', 'partial')}"
        )
        response_parts.append(
            f"- User Satisfaction: {outcome.get('user_satisfaction', 'N/A')}"
        )
        if outcome.get("lessons_learned"):
            response_parts.append(
                f"- Key Lessons: {', '.join(outcome['lessons_learned'])}"
            )

    output_text = "\n".join(response_parts)

    return AlpacaEntry(instruction=instruction, input=input_text, output=output_text)


def chaos_to_simple_qa(chaos_scenario: Dict[str, Any]) -> Dict[str, str]:
    """Convert to simple question-answer format"""
    return {
        "question": (
            f"Task: {chaos_scenario['scenario']} "
            f"Tools available: {', '.join(chaos_scenario['tools_available'].keys())}"
        ),
        "answer": (
            f"Confidence: {chaos_scenario['confidence_trajectory'][0]}%. "
            f"{chaos_scenario['internal_dialogue'][0]['resolution']}. "
            f"Outcome: {chaos_scenario['final_outcome']['success_level']}"
        ),
    }


def chaos_to_thought_process(chaos_scenario: Dict[str, Any]) -> Dict[str, str]:
    """Convert to detailed thought process format"""

    # Build thought process
    thoughts = []

    # Initial thinking
    thoughts.append("Let me analyze this situation:")
    for voice, statement in chaos_scenario["internal_dialogue"][0]["voices"].items():
        thoughts.append(f"- {voice.capitalize()}: {statement}")

    thoughts.append(
        f"\nInitial confidence: {chaos_scenario['confidence_trajectory'][0]}%"
    )
    thoughts.append(f"Decision: {chaos_scenario['internal_dialogue'][0]['resolution']}")

    # Reality breaks
    if chaos_scenario["reality_breaks"]:
        for rb in chaos_scenario["reality_breaks"]:
            thoughts.append(f"\nUnexpected: {rb['discovery']}")
            thoughts.append(f"Impact: {rb['impact_assessment']}")
            thoughts.append(f"Adapting: {rb['adaptation']}")

    # Outcome
    thoughts.append(
        f"\nFinal outcome: {chaos_scenario['final_outcome']['success_level']}"
    )
    thoughts.append(
        f"Lesson learned: "
        f"{chaos_scenario['final_outcome']['lessons_learned'][0]}"
    )

    return {
        "input": (
            f"Task: {chaos_scenario['scenario']}\n"
            f"Tools: {list(chaos_scenario['tools_available'].keys())}"
        ),
        "output": "\n".join(thoughts),
    }


def chaos_to_openai_chat(
    chaos_scenario: Dict[str, Any],
) -> Dict[str, List[Dict[str, str]]]:
    """Convert to OpenAI chat format for fine-tuning"""

    messages = [
        {
            "role": "system",
            "content": "You think through problems systematically, considering multiple perspectives and adapting when things go wrong.",
        },
        {
            "role": "user",
            "content": (
                f"{chaos_scenario['scenario']} I have these tools: "
                f"{', '.join(chaos_scenario['tools_available'].keys())}"
            ),
        },
        {"role": "assistant", "content": build_assistant_response(chaos_scenario)},
    ]

    return {"messages": messages}


def build_assistant_response(scenario: Dict[str, Any]) -> str:
    """Build a natural assistant response from scenario data"""

    response_parts = []

    # Opening
    response_parts.append("I'll think through this systematically.\n")

    # Internal dialogue
    response_parts.append("Considering different approaches:")
    print(scenario["internal_dialogue"])
    print(scenario["internal_dialogue"][0]["voices"])
    for voice, statement in scenario["internal_dialogue"][0]["voices"].items():
        response_parts.append(f"- {voice.capitalize()} approach: {statement}")

    # Confidence and decision
    response_parts.append(
        f"\nMy confidence level: {scenario['confidence_trajectory'][0]}%"
    )
    response_parts.append(
        f"I'll {scenario['internal_dialogue'][0]['resolution'].lower()}"
    )

    # Execution and adaptation
    if scenario["reality_breaks"]:
        response_parts.append("\nDuring execution:")
        for rb in scenario["reality_breaks"]:
            response_parts.append(f"- Discovered: {rb['discovery']}")
            response_parts.append(f"- This means: {rb['impact_assessment']}")
            response_parts.append(f"- Adjusting: {rb['adaptation']}")

    # Results
    response_parts.append(f"\nResult: {scenario['final_outcome']['success_level']}")
    if scenario["final_outcome"]["lessons_learned"]:
        response_parts.append(
            f"Key insight: {scenario['final_outcome']['lessons_learned'][0]}"
        )

    return "\n".join(response_parts)


def convert_batch_for_training(
    chaos_scenarios: List[Dict], format_type: str = "alpaca"
) -> List[Dict]:
    """Convert a batch of CHAOS scenarios to training format"""

    converted = []
    for scenario in chaos_scenarios:
        if format_type == "alpaca":
            converted.append(asdict(chaos_to_alpaca_format(scenario)))
        elif format_type == "openai":
            converted.append(chaos_to_openai_chat(scenario))
        elif format_type == "simple":
            converted.append(chaos_to_simple_qa(scenario))
        elif format_type == "thought":
            converted.append(chaos_to_thought_process(scenario))
        else:
            raise ValueError(f"Unknown format: {format_type}")

    return converted


def save_alpaca_dataset(
    chaos_scenarios: List[Dict], filename: str = "chaos_alpaca_dataset.json"
):
    """Save scenarios in Alpaca format for PEFT training"""
    alpaca_entries = []
    for scenario in chaos_scenarios:
        entry = chaos_to_alpaca_format(scenario)
        alpaca_entries.append(asdict(entry))

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(alpaca_entries, f, indent=2, ensure_ascii=False)

    print(f"Saved {len(alpaca_entries)} Alpaca format entries to {filename}")
    return alpaca_entries


# Example usage
if __name__ == "__main__":
    # Load some scenarios
    with open("../quick_start_data_complete.json", "r") as f:
        scenarios = json.load(f)

    print("=== CHAOS to Training Data Converter ===\n")

    # Show example conversions
    example_scenario = scenarios[0]

    print("1. SIMPLE Q&A FORMAT:")
    print("-" * 50)
    simple = chaos_to_simple_qa(example_scenario)
    print(f"Q: {simple['question'][:100]}...")
    print(f"A: {simple['answer'][:100]}...")

    print("\n2. THOUGHT PROCESS FORMAT:")
    print("-" * 50)
    thought = chaos_to_thought_process(example_scenario)
    print(f"Input: {thought['input'][:100]}...")
    print(f"Output: {thought['output'][:200]}...")

    print("\n3. OPENAI CHAT FORMAT:")
    print("-" * 50)
    chat = chaos_to_openai_chat(example_scenario)
    print(json.dumps(chat, indent=2)[:500] + "...")

    # Convert all and save
    print("\n\nConverting all scenarios...")

    # Save in different formats including Alpaca for PEFT
    for format_type in ["alpaca", "openai", "simple", "thought"]:
        converted = convert_batch_for_training(scenarios, format_type)
        filename = f"training_data_{format_type}.json"

        with open(filename, "w", encoding="utf-8") as f:
            if format_type == "openai":
                # OpenAI expects JSONL
                for item in converted:
                    f.write(json.dumps(item) + "\n")
            else:
                json.dump(converted, f, indent=2, ensure_ascii=False)

        print(f"✓ Saved {len(converted)} examples to {filename}")

    print("\nDone! You can now use these files for fine-tuning.")
    print("- Use training_data_alpaca.json for PEFT with LoRA/QLoRA")
    print("- Use training_data_openai.jsonl for OpenAI fine-tuning")
    print("- Other formats for custom training pipelines")

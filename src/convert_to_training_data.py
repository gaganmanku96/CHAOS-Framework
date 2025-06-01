"""
Convert CHAOS scenarios to actual training data formats
This shows exactly how to use the generated data for training
"""

import json
from typing import List, Dict, Any


def chaos_to_simple_qa(chaos_scenario: Dict[str, Any]) -> Dict[str, str]:
    """Convert to simple question-answer format"""
    return {
        "question": f"Task: {chaos_scenario['scenario']} Tools available: {', '.join(chaos_scenario['tools_available'].keys())}",
        "answer": f"Confidence: {chaos_scenario['confidence_trajectory'][0]}%. {chaos_scenario['internal_dialogue'][0]['resolution']}. Outcome: {chaos_scenario['final_outcome']['success_level']}",
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
        f"Lesson learned: {chaos_scenario['final_outcome']['lessons_learned'][0]}"
    )

    return {
        "input": f"Task: {chaos_scenario['scenario']}\nTools: {list(chaos_scenario['tools_available'].keys())}",
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
            "content": f"{chaos_scenario['scenario']} I have these tools: {', '.join(chaos_scenario['tools_available'].keys())}",
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
    chaos_scenarios: List[Dict], format_type: str = "openai"
) -> List[Dict]:
    """Convert a batch of CHAOS scenarios to training format"""

    converted = []
    for scenario in chaos_scenarios:
        if format_type == "openai":
            converted.append(chaos_to_openai_chat(scenario))
        elif format_type == "simple":
            converted.append(chaos_to_simple_qa(scenario))
        elif format_type == "thought":
            converted.append(chaos_to_thought_process(scenario))
        else:
            raise ValueError(f"Unknown format: {format_type}")

    return converted


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

    # Save in different formats
    for format_type in ["openai", "simple", "thought"]:
        converted = convert_batch_for_training(scenarios, format_type)
        filename = f"training_data_{format_type}.json"

        with open(filename, "w") as f:
            if format_type == "openai":
                # OpenAI expects JSONL
                for item in converted:
                    f.write(json.dumps(item) + "\n")
            else:
                json.dump(converted, f, indent=2)

        print(f"✓ Saved {len(converted)} examples to {filename}")

    print("\nDone! You can now use these files for fine-tuning.")

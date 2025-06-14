"""
PEFT Dataset Generation Example
Generate large-scale training datasets for PEFT with Gemini integration
"""

import json
import os
import sys

sys.path.append("..")
from src.chaos_generator_progressive import GeminiEnhancedGenerator


def main():
    print("🚀 CHAOS Framework - PEFT Dataset Generator")
    print("=" * 60)

    # Check for Gemini API key
    gemini_key = os.getenv("GEMINI_API_KEY")

    if gemini_key:
        print("✓ Gemini API key found - using enhanced generation")
        generator = GeminiEnhancedGenerator(api_key=gemini_key)
    else:
        print("⚠ No Gemini API key found - using basic generation with permutations")
        print("Set GEMINI_API_KEY environment variable for enhanced variety")
        generator = GeminiEnhancedGenerator()  # Will fallback to basic

    print("\n" + "=" * 60)
    print("Select a use case for training data generation:")
    print("1. DevOps & Infrastructure Management")
    print("2. Database Administration")
    print("3. API Development & Integration")
    print("4. Machine Learning Operations")
    print("5. Security Incident Response")
    print("6. Custom use case")
    print("=" * 60)

    choice = input("Enter choice (1-6): ").strip()

    use_cases = {
        "1": "DevOps & Infrastructure Management",
        "2": "Database Administration",
        "3": "API Development & Integration",
        "4": "Machine Learning Operations",
        "5": "Security Incident Response",
    }

    if choice in use_cases:
        usecase = use_cases[choice]
    elif choice == "6":
        usecase = input("Enter your custom use case: ").strip()
    else:
        print("Invalid choice, using default: DevOps & Infrastructure Management")
        usecase = "DevOps & Infrastructure Management"

    print(f"\n🎯 Generating training data for: {usecase}")

    # Get desired count
    try:
        count = int(
            input("Enter number of training examples (50-500, default 250): ") or "250"
        )
        count = max(50, min(500, count))  # Clamp between 50-500
    except ValueError:
        count = 250

    print(f"📊 Generating {count} diverse scenarios...")

    # Generate scenarios
    if hasattr(generator, "generate_diverse_scenarios_for_usecase"):
        scenarios = generator.generate_diverse_scenarios_for_usecase(
            usecase=usecase, domain="technical", count=count
        )
    else:
        # Fallback for basic generator
        scenarios = []
        for _ in range(count):
            scenario = generator.generate_progressive_scenario("technical")
            scenario["scenario"] = f"{scenario['scenario']} (Related to {usecase})"
            scenarios.append(scenario)

    print(f"✓ Generated {len(scenarios)} scenarios")

    # Convert to Alpaca format for PEFT
    print("🔄 Converting to PEFT-compatible Alpaca format...")
    alpaca_data = generator.generate_alpaca_dataset(scenarios)

    # Save datasets
    base_filename = usecase.lower().replace(" ", "_").replace("&", "and")

    # Save raw CHAOS format
    with open(f"{base_filename}_chaos_raw.json", "w", encoding="utf-8") as f:
        json.dump(scenarios, f, indent=2, ensure_ascii=False)

    # Save Alpaca format for PEFT
    alpaca_filename = f"{base_filename}_alpaca_peft.json"
    with open(alpaca_filename, "w", encoding="utf-8") as f:
        json.dump(alpaca_data, f, indent=2, ensure_ascii=False)

    print("\n✅ Dataset generation complete!")
    print("📁 Files created:")
    print(f"   - {base_filename}_chaos_raw.json (Raw CHAOS format)")
    print(f"   - {alpaca_filename} (PEFT-ready Alpaca format)")

    # Show sample entry
    print("\n📄 Sample Alpaca entry:")
    print("=" * 60)
    sample = alpaca_data[0]
    print(f"Instruction: {sample['instruction'][:100]}...")
    print(f"Input: {sample['input'][:80]}...")
    print(f"Output: {sample['output'][:150]}...")
    print("=" * 60)

    # Show usage instructions
    print("\n🔧 PEFT Training Instructions:")
    print("=" * 60)
    print("1. Install requirements:")
    print("   pip install transformers peft torch datasets")
    print()
    print("2. Basic LoRA training example:")
    print("   from datasets import load_dataset")
    print(f"   dataset = load_dataset('json', data_files='{alpaca_filename}')")
    print()
    print("3. For advanced training, see:")
    print("   - https://github.com/huggingface/peft")
    print("   - https://github.com/tloen/alpaca-lora")
    print("=" * 60)

    # Difficulty distribution
    difficulty_counts = {}
    for scenario in scenarios:
        diff = scenario["difficulty"]
        difficulty_counts[diff] = difficulty_counts.get(diff, 0) + 1

    print("\n📊 Difficulty Distribution:")
    for diff, count in sorted(difficulty_counts.items()):
        percentage = (count / len(scenarios)) * 100
        print(f"   {diff.title()}: {count} scenarios ({percentage:.1f}%)")

    print(f"\n🎉 Ready for PEFT training on {usecase}!")


if __name__ == "__main__":
    main()

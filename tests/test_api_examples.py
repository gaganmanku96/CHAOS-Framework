"""
Generate PEFT training examples focused on API calling scenarios
"""

import json
import sys

sys.path.append("src")
from chaos_generator_progressive import GeminiEnhancedGenerator


def main():
    print("🔧 Generating API-focused training examples")
    print("=" * 60)

    # Set API key
    api_key = ""

    # Create generator
    generator = GeminiEnhancedGenerator(api_key=api_key)

    # API-focused use case
    usecase = "API Integration and Management"

    print(f"🎯 Use Case: {usecase}")
    print("📊 Generating 30 diverse API scenarios...")

    try:
        # Generate scenarios
        scenarios = generator.generate_diverse_scenarios_for_usecase(
            usecase=usecase, domain="technical", count=30
        )

        print(f"✅ Generated {len(scenarios)} scenarios successfully!")

        # Convert to Alpaca format
        print("🔄 Converting to Alpaca format...")
        alpaca_data = generator.generate_alpaca_dataset(scenarios)

        # Save for inspection
        with open("api_examples_raw.json", "w", encoding="utf-8") as f:
            json.dump(scenarios, f, indent=2, ensure_ascii=False)

        with open("api_examples_alpaca.json", "w", encoding="utf-8") as f:
            json.dump(alpaca_data, f, indent=2, ensure_ascii=False)

        print("📁 Saved files:")
        print("  - api_examples_raw.json")
        print("  - api_examples_alpaca.json")

        # Show quality assessment
        print("\n" + "=" * 60)
        print("📈 API EXAMPLES QUALITY ASSESSMENT")
        print("=" * 60)

        # Difficulty distribution
        difficulty_counts = {}
        for scenario in scenarios:
            diff = scenario["difficulty"]
            difficulty_counts[diff] = difficulty_counts.get(diff, 0) + 1

        print("🎚️ Difficulty Distribution:")
        for diff, count in sorted(difficulty_counts.items()):
            percentage = (count / len(scenarios)) * 100
            print(f"   {diff.title()}: {count} ({percentage:.1f}%)")

        # Show sample scenarios
        print("\n🔍 Sample API Scenarios:")
        print("-" * 50)
        for i, scenario in enumerate(scenarios[:5]):
            print(
                f"{i+1}. [{scenario['difficulty'].upper()}] "
                f"{scenario['scenario'][:100]}..."
            )
            print(f"   Tools: {len(scenario['tools_available'])}")
            print(f"   Confidence: {scenario['confidence_trajectory']}")
            print()

        # Show sample Alpaca entry
        print("📝 Sample Alpaca Entry for API Training:")
        print("-" * 50)
        sample = alpaca_data[0]
        print(f"Instruction: {sample['instruction'][:150]}...")
        print(f"Input: {sample['input'][:120]}...")
        print(f"Output: {sample['output'][:250]}...")
        print("-" * 50)

        # Variety assessment
        unique_scenarios = set(s["scenario"] for s in scenarios)
        print("\n📊 Variety Metrics:")
        print(
            f"   Unique scenarios: {len(unique_scenarios)}/{len(scenarios)} "
            f"({len(unique_scenarios)/len(scenarios)*100:.1f}%)"
        )

        # Check for API relevance
        api_keywords = [
            "api",
            "endpoint",
            "request",
            "response",
            "integration",
            "service",
            "webhook",
            "rest",
            "http",
        ]
        api_mentions = sum(
            1
            for s in scenarios
            if any(keyword in s["scenario"].lower() for keyword in api_keywords)
        )
        print(
            f"   API relevance: {api_mentions}/{len(scenarios)} "
            f"({api_mentions/len(scenarios)*100:.1f}%)"
        )

        print("\n✨ API training examples generated successfully!")
        print("🎉 Ready for PEFT training on API scenarios!")

    except Exception as e:
        print(f"❌ Error during generation: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    main()

"""
Test script to assess Gemini-generated training data quality
"""

import json
import sys

sys.path.append("src")
from chaos_generator_progressive import GeminiEnhancedGenerator


def main():
    print("🧪 Testing Gemini Quality - Generating 25 examples")
    print("=" * 60)

    # Set API key
    api_key = ""

    # Create generator
    generator = GeminiEnhancedGenerator(api_key=api_key)

    # Test use case
    usecase = "Database Performance Optimization"

    print(f"🎯 Use Case: {usecase}")
    print("📊 Generating 25 diverse scenarios...")

    try:
        # Generate scenarios
        scenarios = generator.generate_diverse_scenarios_for_usecase(
            usecase=usecase, domain="technical", count=25
        )

        print(f"✅ Generated {len(scenarios)} scenarios successfully!")

        # Convert to Alpaca format
        print("🔄 Converting to Alpaca format...")
        alpaca_data = generator.generate_alpaca_dataset(scenarios)

        # Save for inspection
        with open("gemini_quality_test_raw.json", "w", encoding="utf-8") as f:
            json.dump(scenarios, f, indent=2, ensure_ascii=False)

        with open("gemini_quality_test_alpaca.json", "w", encoding="utf-8") as f:
            json.dump(alpaca_data, f, indent=2, ensure_ascii=False)

        print("📁 Saved files:")
        print("  - gemini_quality_test_raw.json")
        print("  - gemini_quality_test_alpaca.json")

        # Show quality assessment
        print("\n" + "=" * 60)
        print("📈 QUALITY ASSESSMENT")
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
        print("\n🔍 Sample Scenarios:")
        print("-" * 40)
        for i, scenario in enumerate(scenarios[:5]):
            print(
                f"{i+1}. [{scenario['difficulty'].upper()}] "
                f"{scenario['scenario'][:80]}..."
            )
            print(f"   Tools: {len(scenario['tools_available'])}")
            print(f"   Confidence: {scenario['confidence_trajectory']}")
            print()

        # Show sample Alpaca entry
        print("📝 Sample Alpaca Entry:")
        print("-" * 40)
        sample = alpaca_data[0]
        print(f"Instruction: {sample['instruction'][:120]}...")
        print(f"Input: {sample['input'][:100]}...")
        print(f"Output: {sample['output'][:200]}...")
        print("-" * 40)

        # Variety assessment
        unique_scenarios = set(s["scenario"] for s in scenarios)
        print("\n📊 Variety Metrics:")
        print(
            f"   Unique scenarios: {len(unique_scenarios)}/{len(scenarios)} "
            f"({len(unique_scenarios)/len(scenarios)*100:.1f}%)"
        )

        # Check for usecase relevance
        usecase_mentions = sum(
            1 for s in scenarios if usecase.lower() in s["scenario"].lower()
        )
        print(
            f"   Usecase relevance: {usecase_mentions}/{len(scenarios)} "
            f"({usecase_mentions/len(scenarios)*100:.1f}%)"
        )

        print("\n✨ Generation completed successfully!")
        print("🎉 Quality looks good - ready for PEFT training!")

    except Exception as e:
        print(f"❌ Error during generation: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    main()

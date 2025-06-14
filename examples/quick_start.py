"""
Quick Start Script - Generate Your First CHAOS Training Data
"""

import json
import sys

sys.path.append("..")
from src.chaos_generator_progressive import CHAOSGenerator

print("🚀 CHAOS Framework - Quick Start")
print("=" * 50)

# Create generator
generator = CHAOSGenerator()

# 1. Show one example of each difficulty
print("\n📊 Example scenarios at each difficulty level:\n")

for difficulty in ["simple", "basic", "intermediate", "advanced", "chaotic"]:
    scenario = generator.generate_progressive_scenario("technical", difficulty)
    print(f"[{difficulty.upper()}] {scenario['scenario'][:60]}...")
    print(f"  Tools needed: {len(scenario['tools_available'])}")
    print(f"  Confidence journey: {scenario['confidence_trajectory']}")
    print()

# 2. Generate a small batch
print("📁 Generating training batch...")
small_batch = generator.generate_curriculum_batch(count_per_level=5)
generator.save_curriculum(small_batch, "quick_start_data")

print("\n✅ Success! Generated files:")
print("  - quick_start_data_complete.json (all 25 scenarios)")
print("  - quick_start_data_simple.json")
print("  - quick_start_data_basic.json")
print("  - quick_start_data_intermediate.json")
print("  - quick_start_data_advanced.json")
print("  - quick_start_data_chaotic.json")

# 3. Show one complete scenario
print("\n🔍 Here's one complete scenario:")
print("-" * 50)
example = small_batch[10]  # Get an intermediate one
print(json.dumps(example, indent=2)[:1000] + "...\n")

print("🎯 Next steps:")
print("1. Check the generated JSON files")
print("2. Run 'python generate_large_dataset.py' for more data")
print("3. Customize chaos_generator_progressive.py for your needs")
print("\nHappy training! 🤖")

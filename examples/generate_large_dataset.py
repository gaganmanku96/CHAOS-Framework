"""
Generate Large CHAOS Training Dataset
Customize the numbers below for your needs
"""

import sys
sys.path.append('..')
from src.chaos_generator_progressive import CHAOSGenerator
import json
import random
from datetime import datetime

print("🔨 CHAOS Framework - Large Dataset Generator")
print("=" * 50)

# Configuration - CUSTOMIZE THESE
SCENARIOS_PER_DIFFICULTY = 200  # Will generate 200 * 5 = 1000 total
INCLUDE_SIMPLE = True           # Include simple single-tool tasks?
DOMAINS = ["technical", "business", "research", "creative"]  # Which domains?

# Initialize generator
generator = CHAOSGenerator()

# Generate scenarios
print(f"\n📊 Generating {SCENARIOS_PER_DIFFICULTY * 5} scenarios...")
print(f"   - Domains: {', '.join(DOMAINS)}")
print(f"   - Include simple tasks: {INCLUDE_SIMPLE}")
print("\nProgress:")

all_scenarios = []
difficulties = ["simple", "basic", "intermediate", "advanced", "chaotic"]

if not INCLUDE_SIMPLE:
    difficulties = difficulties[1:]  # Skip simple

for i, difficulty in enumerate(difficulties):
    print(f"\n[{difficulty.upper()}] Generating {SCENARIOS_PER_DIFFICULTY} scenarios...")
    
    for j in range(SCENARIOS_PER_DIFFICULTY):
        # Randomly select domain
        domain = random.choice(DOMAINS)
        
        # Generate scenario
        scenario = generator.generate_progressive_scenario(domain, difficulty)
        all_scenarios.append(scenario)
        
        # Progress indicator
        if (j + 1) % 50 == 0:
            print(f"  ✓ {j + 1}/{SCENARIOS_PER_DIFFICULTY} completed")

# Save the data
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename_base = f"chaos_training_data_{timestamp}"

print(f"\n💾 Saving {len(all_scenarios)} scenarios...")

# Save complete dataset
with open(f"{filename_base}_complete.json", 'w') as f:
    json.dump(all_scenarios, f, indent=2)

# Save by difficulty
by_difficulty = {}
for scenario in all_scenarios:
    diff = scenario['difficulty']
    if diff not in by_difficulty:
        by_difficulty[diff] = []
    by_difficulty[diff].append(scenario)

for difficulty, scenarios in by_difficulty.items():
    with open(f"{filename_base}_{difficulty}.json", 'w') as f:
        json.dump(scenarios, f, indent=2)

# Generate statistics
print("\n📈 Dataset Statistics:")
print(f"   Total scenarios: {len(all_scenarios)}")
for diff, scenarios in by_difficulty.items():
    print(f"   {diff}: {len(scenarios)} scenarios")

# Domain distribution
domain_count = {}
for scenario in all_scenarios:
    # Extract domain from scenario text (simple heuristic)
    for domain in DOMAINS:
        if any(keyword in scenario['scenario'].lower() for keyword in 
               ['code', 'deploy', 'debug', 'api', 'server'] if domain == 'technical' else
               ['presentation', 'meeting', 'report', 'client'] if domain == 'business' else
               ['paper', 'research', 'data', 'experiment'] if domain == 'research' else
               ['design', 'creative', 'ui', 'marketing']):
            domain_count[domain] = domain_count.get(domain, 0) + 1
            break

print("\n📊 Domain Distribution (approximate):")
for domain, count in domain_count.items():
    print(f"   {domain}: {count} scenarios")

# Save metadata
metadata = {
    "generated_at": timestamp,
    "total_scenarios": len(all_scenarios),
    "scenarios_per_difficulty": SCENARIOS_PER_DIFFICULTY,
    "difficulties": list(by_difficulty.keys()),
    "domains": DOMAINS,
    "statistics": {
        "by_difficulty": {k: len(v) for k, v in by_difficulty.items()},
        "by_domain": domain_count
    }
}

with open(f"{filename_base}_metadata.json", 'w') as f:
    json.dump(metadata, f, indent=2)

print(f"\n✅ Success! Generated files:")
print(f"   - {filename_base}_complete.json")
for diff in by_difficulty.keys():
    print(f"   - {filename_base}_{diff}.json")
print(f"   - {filename_base}_metadata.json")

print("\n🎯 Next steps:")
print("1. Review the generated scenarios")
print("2. Convert to your fine-tuning format")
print("3. Start training your model!")
print(f"\nTotal time: ~{len(all_scenarios) * 0.01:.1f} seconds")

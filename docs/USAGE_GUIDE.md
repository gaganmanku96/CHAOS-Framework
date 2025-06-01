# How to Use CHAOS Framework - Step by Step Guide

## Which Script to Use?

### You have 2 main scripts:

1. **`chaos_generator.py`** - Basic version (start here if testing)
2. **`chaos_generator_progressive.py`** - Full version with difficulty levels (RECOMMENDED)

## Step 1: Test the Generator

```bash
# Navigate to your project directory
cd C:\Users\gagan\personal_projects\agentic-ai-data

# Run the progressive generator (recommended)
python chaos_generator_progressive.py
```

This will automatically:
- Generate example scenarios at each difficulty level
- Create a complete curriculum with 50 scenarios (10 per difficulty)
- Save files in your directory

## Step 2: Understanding Output Files

After running, you'll see these files:
```
chaos_curriculum_complete.json     # All 50 scenarios
chaos_curriculum_simple.json       # Only simple single-tool tasks
chaos_curriculum_basic.json        # Basic 1-2 tool tasks
chaos_curriculum_intermediate.json # Intermediate complexity
chaos_curriculum_advanced.json     # Advanced scenarios
chaos_curriculum_chaotic.json      # Maximum complexity
```

## Step 3: Generate Custom Data

```python
# custom_generation.py
from chaos_generator_progressive import CHAOSGenerator

# Initialize generator
generator = CHAOSGenerator()

# Option 1: Generate one scenario
scenario = generator.generate_progressive_scenario(
    domain="technical",      # or "business", "research", "creative"
    difficulty="intermediate"  # or "simple", "basic", "advanced", "chaotic"
)
print(scenario)

# Option 2: Generate batch with specific settings
scenarios = []
for i in range(100):
    scenario = generator.generate_progressive_scenario("technical", "advanced")
    scenarios.append(scenario)

# Save your custom batch
generator.save_curriculum(scenarios, "my_custom_training_data")
```

## Step 4: Use for Fine-tuning

### A. Prepare Training Data
```python
import json

# Load the generated data
with open('chaos_curriculum_complete.json', 'r') as f:
    all_scenarios = json.load(f)

# Convert to fine-tuning format (example for OpenAI)
training_data = []
for scenario in all_scenarios:
    # Create prompt-completion pairs
    prompt = f"Task: {scenario['scenario']}\nTools: {list(scenario['tools_available'].keys())}\nWhat's your approach?"
    
    # Build completion from the scenario data
    completion = f"""
Internal Analysis:
{scenario['internal_dialogue'][0]['voices']}

Decision: {scenario['internal_dialogue'][0]['resolution']}
Confidence: {scenario['confidence_trajectory']}

Actions taken...
{scenario.get('reality_breaks', [])}

Outcome: {scenario['final_outcome']['success_level']}
Lessons: {scenario['final_outcome']['lessons_learned']}
"""
    
    training_data.append({
        "prompt": prompt,
        "completion": completion
    })

# Save in fine-tuning format
with open('fine_tuning_data.jsonl', 'w') as f:
    for item in training_data:
        f.write(json.dumps(item) + '\n')
```

## Step 5: Quick Examples

### Generate 1000 Technical Scenarios
```python
from chaos_generator_progressive import CHAOSGenerator

generator = CHAOSGenerator()
scenarios = []

# 200 of each difficulty level
for difficulty in ["simple", "basic", "intermediate", "advanced", "chaotic"]:
    for _ in range(200):
        scenario = generator.generate_progressive_scenario("technical", difficulty)
        scenarios.append(scenario)

generator.save_curriculum(scenarios, "technical_1000")
```

### Generate Mixed Domain Curriculum
```python
# Generate balanced dataset across all domains
curriculum = generator.generate_curriculum_batch(count_per_level=25)  # 25 * 5 difficulties = 125 total
generator.save_curriculum(curriculum, "mixed_domains")
```

### Generate Only Complex Scenarios
```python
# For advanced model training
complex_scenarios = []
for _ in range(500):
    difficulty = random.choice(["advanced", "chaotic"])
    domain = random.choice(["technical", "business", "research", "creative"])
    scenario = generator.generate_progressive_scenario(domain, difficulty)
    complex_scenarios.append(scenario)

generator.save_curriculum(complex_scenarios, "complex_only")
```

## Step 6: Gemini Enhancement (Optional)

```python
# If you have Gemini API access
from chaos_generator_progressive import GeminiEnhancedGenerator

# Get your API key from: https://makersuite.google.com/app/apikey
generator = GeminiEnhancedGenerator(api_key="YOUR_GEMINI_API_KEY")

# Generate with richer, more contextual content
enhanced_scenario = generator.generate_progressive_scenario("business", "advanced")
```

## Common Commands

```bash
# Just test it out
python chaos_generator_progressive.py

# Generate lots of data (create a script)
python generate_training_data.py

# Check what was generated
python -c "import json; print(json.dumps(json.load(open('chaos_curriculum_simple.json'))[0], indent=2))"
```

## What Each Difficulty Teaches

- **Simple**: Basic tool usage, don't overthink
- **Basic**: Handle minor issues, stay calm
- **Intermediate**: Adapt when things go wrong
- **Advanced**: Complex reasoning, multiple paths
- **Chaotic**: Innovation under extreme pressure

## Tips

1. **Start Simple**: Generate mostly simple/basic scenarios first
2. **Progressive Training**: Gradually increase difficulty mix
3. **Domain Balance**: Mix domains for versatility
4. **Quality Check**: Review generated scenarios before training
5. **Customize**: Modify the generator for your specific tools/scenarios

## Next Steps

1. Run `python chaos_generator_progressive.py` to test
2. Review the generated files
3. Customize for your specific needs
4. Generate large dataset for fine-tuning
5. Format for your training pipeline

Need help with a specific part? Let me know!

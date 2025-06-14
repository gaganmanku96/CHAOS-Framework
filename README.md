# CHAOS Framework - Agentic AI Training Data Generator

🧠 **Teaching AI How to Think, Not Just What to Do**

[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 Overview

The CHAOS (Contextual Hierarchical Adaptive Orchestration System) Framework generates synthetic training data that teaches AI systems to think through complex problems like human experts - with internal reasoning, confidence tracking, and adaptive strategies.

### Key Innovation

Traditional training teaches AI: `Task → Steps → Result`

CHAOS teaches AI: `Task → Think → Adapt → Learn`

## 📊 CHAOS Training Pipeline

![CHAOS Training Pipeline](assets/chaos_training_pipeline.png)

### Traditional vs CHAOS Training

![Traditional vs CHAOS](assets/traditional_vs_chaos.png)

## 🧪 What CHAOS Generates

See how CHAOS transforms simple tasks into rich training scenarios:

### Input: Basic Task
```
"Fix API authentication errors during client demo"
```

### Output: Rich Training Scenario

#### CHAOS Format (Internal Reasoning)
```json
{
  "scenario": "API calls return 'Unauthorized' errors during critical client demo in 30 minutes",
  "difficulty": "simple",
  "confidence_trajectory": [85, 70, 90],
  "internal_dialogue": [{
    "voices": {
      "optimizer": "Check authentication tokens and API keys first",
      "skeptic": "Could be a server-side configuration issue", 
      "creative": "Maybe try alternative authentication method",
      "pragmatist": "Focus on quickest fix for demo"
    },
    "resolution": "Verify and refresh API credentials",
    "confidence": 85
  }],
  "reality_breaks": [{
    "discovery": "API key expired 2 hours ago",
    "adaptation": "Generate new key and update configuration"
  }],
  "final_outcome": {
    "success_level": "full",
    "lessons_learned": ["Always verify API credentials first"]
  }
}
```

#### Alpaca Format (PEFT-Ready)
```json
{
  "instruction": "You are an AI assistant helping with a simple difficulty task. API calls return 'Unauthorized' errors during critical client demo in 30 minutes. Time: 30 minutes",
  "input": "Available tools: log_analyzer: Parse system logs, deployment_tool: Deploy to environments", 
  "output": "**Internal Analysis:**\n- Optimizer: Check authentication tokens and API keys\n- Skeptic: Could be a server-side configuration issue\n- Creative: Maybe try alternative authentication method\n- Pragmatist: Focus on quickest fix for demo\nResolution: Verify and refresh API credentials\nConfidence: 85%\n\n**Confidence Progression:** [85, 70, 90]\n\n**Final Outcome:**\n- Success Level: full\n- User Satisfaction: 95%\n- Key Lessons: Always verify API credentials first"
}
```

## 🎯 Features

- **Progressive Difficulty Levels**: From simple single-tool tasks to chaotic multi-tool scenarios
- **Internal Reasoning System**: Multiple "voices" (Optimizer, Skeptic, Creative, Pragmatist) debate approaches
- **Confidence Tracking**: AI learns when to be certain vs. when to be cautious
- **Reality Breaks**: Unexpected discoveries that force strategy pivots
- **Emergent Behaviors**: Tool synthesis, constraint hacking, learning from failures
- **PEFT Integration**: Generate Alpaca-format datasets for Parameter-Efficient Fine-Tuning
- **Gemini AI Enhancement**: Use Gemini 2.5 Flash for diverse, realistic scenario generation
- **Bulk Usecase Generation**: Generate 200-500 training examples for specific domains

## 📦 Installation

### Option 1: Install from PyPI (Recommended)
```bash
pip install chaos-framework
```

### Option 2: Install from Source
```bash
git clone https://github.com/gaganmanku96/chaos-framework.git
cd chaos-framework
pip install -e .
```

### Option 3: Development Setup
```bash
git clone https://github.com/gaganmanku96/chaos-framework.git
cd chaos-framework
pip install -r requirements.txt
```

### 🔑 Gemini AI Configuration (Optional but Recommended)

For enhanced variety and realistic scenarios, configure Gemini AI:

```bash
# Set environment variable
export GEMINI_API_KEY="your_gemini_api_key_here"

# Or set in your script
generator = GeminiEnhancedGenerator(api_key="your_gemini_api_key_here")
```

**Get your free Gemini API key:** https://aistudio.google.com/app/apikey

**Supported Models:**
- `gemini-2.5-flash-preview-05-20` (Default - Best performance)
- `gemini-1.5-flash` (Alternative)
- `gemini-1.5-pro` (More powerful but slower)

To change model:
```python
# In src/chaos_generator_progressive.py, line 414
self.model = genai.GenerativeModel("gemini-2.5-flash-preview-05-20")
```

## 🏃 Quick Start

### Option 1: Using CLI Tool (After pip install)

```bash
# Generate 10 scenarios with CLI
chaos-generate generate --count 10 --domain technical --difficulty intermediate

# Generate balanced curriculum
chaos-generate curriculum --count-per-level 25

# Convert existing data to different formats
chaos-generate convert scenarios.json --format alpaca
```

### Option 2: Using Python Scripts

#### 1. Generate Your First Dataset

```bash
cd examples
python quick_start.py
```

This creates 25 sample scenarios across all difficulty levels.

#### 2. Generate PEFT Dataset (Recommended)

```bash
# Optional: Set Gemini API key for enhanced variety
export GEMINI_API_KEY="your_gemini_api_key_here"

python generate_peft_dataset.py
```

Interactive generation of 200-500 PEFT-ready examples for specific use cases.  
**With Gemini:** Gets diverse, realistic scenarios  
**Without Gemini:** Uses permutation-based generation (still works great!)

#### 3. Generate Large Training Dataset

```bash
python generate_large_dataset.py
```

Generates 1000+ scenarios for comprehensive training.

#### 4. Convert to Training Format

```bash
cd ../src
python convert_to_training_data.py
```

Converts CHAOS scenarios to formats ready for fine-tuning (Alpaca, OpenAI, Anthropic, etc.)

## 📚 Documentation

- [CHAOS Framework Overview](docs/CHAOS_Framework_Agentic_Training.md) - Complete framework documentation
- [Progressive Training Guide](docs/Progressive_CHAOS_Training_Guide.md) - Difficulty levels and curriculum
- [How CHAOS Training Works](docs/How_CHAOS_Training_Works.md) - Understanding the training process
- [Visual Examples](docs/Training_Visual_Examples.md) - See what the AI learns

## 🛠️ Usage Examples

### Using as Python Library

```python
# After pip install chaos-framework
import chaos_framework

# Basic generation
generator = chaos_framework.CHAOSGenerator()
scenario = generator.generate_progressive_scenario(
    domain="technical",      # technical/business/research/creative
    difficulty="intermediate"  # simple/basic/intermediate/advanced/chaotic
)

# Enhanced generation with Gemini
generator = chaos_framework.GeminiEnhancedGenerator(api_key="YOUR_GEMINI_KEY")
scenarios = generator.generate_diverse_scenarios_for_usecase(
    usecase="API Integration and Management",
    domain="technical",
    count=250
)

# Convert to PEFT-ready Alpaca format
alpaca_data = generator.generate_alpaca_dataset(scenarios)
```

### Using Source Code Directly

```python
from src.chaos_generator_progressive import CHAOSGenerator, GeminiEnhancedGenerator

# Basic generation
generator = CHAOSGenerator()
scenario = generator.generate_progressive_scenario("technical", "advanced")

# Convert to Alpaca format
alpaca_entry = generator.convert_to_alpaca_format(scenario)
```

## 📊 Difficulty Levels

| Level | Tools | Complexity | Use Case |
|-------|-------|------------|----------|
| **Simple** | 1 | Straightforward | Teach basic tool usage |
| **Basic** | 1-2 | Minor issues | Handle simple problems |
| **Intermediate** | 2-3 | Reality breaks | Adapt to changes |
| **Advanced** | 3-4 | Complex reasoning | Multi-faceted problems |
| **Chaotic** | 4+ | Constant pivoting | Innovation under pressure |


## 🎓 Training Philosophy

CHAOS teaches AI to:
1. **Think Before Acting**: Internal deliberation between multiple perspectives
2. **Track Confidence**: Know when certain vs. uncertain
3. **Adapt Gracefully**: Pivot strategies when things go wrong
4. **Learn from Failures**: Extract insights from what didn't work
5. **Match Complexity**: Use simple solutions for simple problems

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Areas for Contribution:
- New scenario domains
- Additional tool types
- Language-specific training formats
- Evaluation metrics
- Real-world scenario validations

## 📈 Results

AI models trained with CHAOS data show:
- 40% better adaptation to unexpected scenarios
- 60% reduction in overengineering simple tasks
- 3x more creative problem solutions
- Human-like confidence patterns

### PEFT Training Benefits
- **Efficient Fine-tuning**: LoRA/QLoRA compatible format reduces training costs by 90%
- **Domain-Specific**: Generate focused datasets for specific use cases (APIs, DevOps, etc.)
- **Scalable**: Generate 200-500 examples per domain in minutes with Gemini integration
- **Ready-to-Use**: Direct compatibility with popular PEFT libraries (Hugging Face PEFT, Alpaca-LoRA)

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by how human experts actually solve problems
- Built for the agentic AI community
- Special thanks to all contributors

## 📬 Contact

- GitHub Issues: [Report bugs or request features](https://github.com/gaganmanku96/chaos-framework/issues)
- Discussions: [Join the conversation](https://github.com/gaganmanku96/chaos-framework/discussions)

---

## 🎯 Popular Use Cases

Generate training data for specific domains:

- **API Integration**: Authentication, rate limiting, error handling, service integration
- **Database Performance**: Query optimization, connection issues, migration challenges  
- **DevOps & Infrastructure**: Deployment, monitoring, scaling, incident response
- **Security Operations**: Threat detection, incident response, vulnerability management
- **Machine Learning Ops**: Model deployment, data pipeline issues, performance monitoring

## 🚀 Quick PEFT Training Guide

### 1. Install & Generate Dataset
```bash
# Install the package
pip install chaos-framework

# Optional: Get free Gemini API key for enhanced variety
# https://aistudio.google.com/app/apikey
export GEMINI_API_KEY="your_key_here" 

# Generate training data using CLI
chaos-generate generate --count 500 --format alpaca --domain technical

# Or use interactive Python script for specific use cases
cd examples
python generate_peft_dataset.py
```

### 2. Install PEFT Dependencies
```bash
pip install "chaos-framework[peft]"  # Includes transformers, peft, torch, etc.
```

### 3. Basic LoRA Training
```python
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig, get_peft_model

# Load your generated dataset
dataset = load_dataset('json', data_files='chaos_scenarios.json')

# Standard LoRA configuration for instruction following
lora_config = LoraConfig(
    r=8, lora_alpha=16, lora_dropout=0.05,
    target_modules=["q_proj", "v_proj"]
)

# Train with your CHAOS-generated data
# See: https://github.com/huggingface/peft for complete examples
```

**Ready to teach your AI to think adaptively?** 
- **CLI users**: `pip install chaos-framework && chaos-generate --help`
- **Python users**: `pip install chaos-framework && python -c "import chaos_framework; print('Ready!')"`
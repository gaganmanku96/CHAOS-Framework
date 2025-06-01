# CHAOS Framework - Project Structure

```
chaos-framework/
│
├── README.md                    # Main project documentation
├── LICENSE                      # MIT License
├── CONTRIBUTING.md             # Contribution guidelines
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
│
├── src/                        # Source code
│   ├── __init__.py            # Package initialization
│   ├── chaos_generator.py     # Basic generator
│   ├── chaos_generator_progressive.py  # Full progressive generator
│   └── convert_to_training_data.py    # Training format converters
│
├── examples/                   # Example scripts
│   ├── quick_start.py         # Get started quickly
│   ├── generate_large_dataset.py      # Generate lots of data
│   ├── CHAOS_Complete_Training_Example.md    # Database migration example
│   └── CHAOS_Training_Example_2_Research_Crisis.md  # Research paper example
│
└── docs/                       # Documentation
    ├── CHAOS_Framework_Agentic_Training.md     # Framework overview
    ├── Progressive_CHAOS_Training_Guide.md     # Training curriculum
    ├── How_CHAOS_Training_Works.md            # Training explanation
    ├── Training_Visual_Examples.md            # Visual examples
    ├── USAGE_GUIDE.md                        # Detailed usage guide
    ├── PROJECT_SUMMARY.md                    # Project summary
    └── CHAOS_LinkedIn_Post.md               # Social media content
```

## Quick Commands

### First Time Setup
```bash
git clone https://github.com/yourusername/chaos-framework.git
cd chaos-framework
pip install -r requirements.txt
```

### Generate Training Data
```bash
# Quick test (25 scenarios)
cd examples
python quick_start.py

# Large dataset (1000+ scenarios)
python generate_large_dataset.py

# Convert to training format
cd ../src
python convert_to_training_data.py
```

### Use in Your Code
```python
from src.chaos_generator_progressive import CHAOSGenerator

generator = CHAOSGenerator()
scenario = generator.generate_progressive_scenario("technical", "advanced")
```

## Key Files to Check

1. **Start Here**: `examples/quick_start.py` - See it in action
2. **Understand**: `docs/How_CHAOS_Training_Works.md` - Learn the concepts
3. **Customize**: `src/chaos_generator_progressive.py` - Modify for your needs
4. **Convert**: `src/convert_to_training_data.py` - Format for your training

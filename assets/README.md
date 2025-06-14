# Assets Directory

This directory contains visual assets and diagrams for the CHAOS Framework documentation.

## 🎨 Visual Assets

### `chaos_training_pipeline.png`
Main flowchart showing the complete CHAOS training pipeline:
- Simple task input
- CHAOS processing with internal reasoning
- Optional Gemini enhancement
- Rich scenario generation
- PEFT-ready Alpaca format output
- Fine-tuned AI model

### `traditional_vs_chaos.png`
Comparison diagram illustrating the difference between:
- **Traditional Training**: Linear Task → Steps → Result approach
- **CHAOS Training**: Network-based Think → Adapt → Learn methodology

## 🔧 Generating Charts

Charts are generated using the script in `tests/chaos_flowchart.py`:

```bash
python tests/chaos_flowchart.py
```

This creates high-quality 300 DPI PNG files suitable for documentation and presentations.

## 📏 Specifications

- **Format**: PNG
- **Resolution**: 300 DPI
- **Color Scheme**: Professional with consistent branding
- **Text Size**: Optimized for readability (14-24px fonts)
- **Dimensions**: Optimized for README display and presentations
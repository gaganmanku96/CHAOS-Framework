# Tests Directory

This directory contains test scripts, utilities, and generated test outputs for the CHAOS Framework.

## 🧪 Test Scripts

### `test_gemini_quality.py`
Tests Gemini API integration and assesses quality of generated scenarios.
```bash
python tests/test_gemini_quality.py
```

### `test_api_examples.py`  
Generates API-focused training examples and performs quality assessment.
```bash
python tests/test_api_examples.py
```

### `chaos_flowchart.py`
Generates visual flowcharts for documentation.
```bash
python tests/chaos_flowchart.py
```

## 📁 Generated Files

- `*.json` - Test output files containing generated scenarios
- `*_alpaca.json` - PEFT-ready Alpaca format datasets
- `*_raw.json` - Raw CHAOS format scenarios

## 🚀 Running Tests

To run quality tests with your Gemini API key:

```bash
# Set your API key
export GEMINI_API_KEY="your_gemini_api_key_here"

# Run tests
cd tests
python test_gemini_quality.py
python test_api_examples.py
```

## 📈 Test Outputs

Tests generate quality assessments including:
- Difficulty distribution analysis
- Scenario variety metrics
- API relevance scoring
- Sample data inspection
- Format validation
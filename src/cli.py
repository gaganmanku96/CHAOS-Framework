#!/usr/bin/env python3
"""
CHAOS Framework CLI - Command Line Interface
"""

import argparse
import json
import os
import sys
from typing import Optional

from .chaos_generator_progressive import CHAOSGenerator, GeminiEnhancedGenerator


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="CHAOS Framework - Agentic AI Training Data Generator"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Generate command
    gen_parser = subparsers.add_parser("generate", help="Generate training scenarios")
    gen_parser.add_argument(
        "--domain",
        choices=["technical", "business", "research", "creative"],
        default="technical",
        help="Domain for scenarios (default: technical)"
    )
    gen_parser.add_argument(
        "--difficulty",
        choices=["simple", "basic", "intermediate", "advanced", "chaotic"],
        default="intermediate",
        help="Difficulty level (default: intermediate)"
    )
    gen_parser.add_argument(
        "--count",
        type=int,
        default=10,
        help="Number of scenarios to generate (default: 10)"
    )
    gen_parser.add_argument(
        "--output",
        default="chaos_scenarios.json",
        help="Output file path (default: chaos_scenarios.json)"
    )
    gen_parser.add_argument(
        "--format",
        choices=["chaos", "alpaca"],
        default="chaos",
        help="Output format (default: chaos)"
    )
    gen_parser.add_argument(
        "--gemini-api-key",
        help="Gemini API key for enhanced generation (optional)"
    )
    
    # Curriculum command
    curr_parser = subparsers.add_parser("curriculum", help="Generate balanced curriculum")
    curr_parser.add_argument(
        "--count-per-level",
        type=int,
        default=20,
        help="Scenarios per difficulty level (default: 20)"
    )
    curr_parser.add_argument(
        "--output",
        default="chaos_curriculum.json",
        help="Output file path (default: chaos_curriculum.json)"
    )
    curr_parser.add_argument(
        "--gemini-api-key",
        help="Gemini API key for enhanced generation (optional)"
    )
    
    # Convert command
    conv_parser = subparsers.add_parser("convert", help="Convert CHAOS format to training format")
    conv_parser.add_argument(
        "input_file",
        help="Input CHAOS JSON file"
    )
    conv_parser.add_argument(
        "--format",
        choices=["alpaca", "openai", "simple"],
        default="alpaca",
        help="Target format (default: alpaca)"
    )
    conv_parser.add_argument(
        "--output",
        help="Output file path (auto-generated if not specified)"
    )
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    try:
        if args.command == "generate":
            generate_scenarios(args)
        elif args.command == "curriculum":
            generate_curriculum(args)
        elif args.command == "convert":
            convert_scenarios(args)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def generate_scenarios(args):
    """Generate individual scenarios"""
    # Check for Gemini API key
    gemini_key = args.gemini_api_key or os.getenv("GEMINI_API_KEY")
    
    if gemini_key:
        print("Using Gemini AI for enhanced generation...")
        generator = GeminiEnhancedGenerator(api_key=gemini_key)
    else:
        print("Using basic generation (set GEMINI_API_KEY for enhanced variety)...")
        generator = CHAOSGenerator()
    
    print(f"Generating {args.count} scenarios...")
    scenarios = []
    
    for i in range(args.count):
        scenario = generator.generate_progressive_scenario(args.domain, args.difficulty)
        scenarios.append(scenario)
        print(f"Generated scenario {i+1}/{args.count}")
    
    # Convert to requested format
    if args.format == "alpaca" and hasattr(generator, 'convert_to_alpaca_format'):
        print("Converting to Alpaca format...")
        alpaca_data = [generator.convert_to_alpaca_format(s) for s in scenarios]
        output_data = alpaca_data
    else:
        output_data = scenarios
    
    # Save results
    with open(args.output, 'w') as f:
        json.dump(output_data, f, indent=2)
    
    print(f"Saved {len(output_data)} scenarios to {args.output}")


def generate_curriculum(args):
    """Generate balanced curriculum"""
    # Check for Gemini API key
    gemini_key = args.gemini_api_key or os.getenv("GEMINI_API_KEY")
    
    if gemini_key:
        print("Using Gemini AI for enhanced generation...")
        generator = GeminiEnhancedGenerator(api_key=gemini_key)
    else:
        print("Using basic generation (set GEMINI_API_KEY for enhanced variety)...")
        generator = CHAOSGenerator()
    
    print(f"Generating curriculum with {args.count_per_level} scenarios per level...")
    curriculum = generator.generate_curriculum_batch(args.count_per_level)
    
    # Save curriculum
    generator.save_curriculum(curriculum, args.output.replace('.json', ''))
    
    total_scenarios = sum(len(scenarios) for scenarios in curriculum.values())
    print(f"Generated {total_scenarios} total scenarios across all difficulty levels")
    print(f"Saved curriculum to {args.output}")


def convert_scenarios(args):
    """Convert CHAOS scenarios to training format"""
    if not os.path.exists(args.input_file):
        raise FileNotFoundError(f"Input file not found: {args.input_file}")
    
    # Load CHAOS scenarios
    with open(args.input_file, 'r') as f:
        scenarios = json.load(f)
    
    print(f"Converting {len(scenarios)} scenarios to {args.format} format...")
    
    # Import conversion functions
    from .convert_to_training_data import (
        chaos_to_simple_qa,
        chaos_to_thought_process,
        chaos_to_openai_chat
    )
    
    # Convert based on format
    if args.format == "alpaca":
        # Assume scenarios are already in format compatible with Alpaca
        converted = scenarios
    elif args.format == "openai":
        converted = [chaos_to_openai_chat(s) for s in scenarios]
    elif args.format == "simple":
        converted = [chaos_to_simple_qa(s) for s in scenarios]
    else:
        raise ValueError(f"Unsupported format: {args.format}")
    
    # Determine output file
    if args.output:
        output_file = args.output
    else:
        base_name = os.path.splitext(args.input_file)[0]
        output_file = f"{base_name}_{args.format}.json"
    
    # Save converted data
    with open(output_file, 'w') as f:
        json.dump(converted, f, indent=2)
    
    print(f"Converted scenarios saved to {output_file}")


if __name__ == "__main__":
    main()
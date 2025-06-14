"""
CHAOS Framework Data Generator - Simplified Version
"""

import json
import random
from typing import List, Dict, Any
from dataclasses import dataclass, field, asdict
from enum import Enum


class Difficulty(Enum):
    BASIC = "basic"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    CHAOTIC = "chaotic"


@dataclass
class CHAOSScenario:
    """Complete CHAOS training scenario"""

    scenario: str
    difficulty: str
    tools_available: Dict[str, str]
    constraints: str
    internal_dialogue: List[Dict[str, Any]] = field(default_factory=list)
    mental_simulations: List[Dict[str, Any]] = field(default_factory=list)
    reality_breaks: List[Dict[str, Any]] = field(default_factory=list)
    confidence_trajectory: List[int] = field(default_factory=list)
    abandoned_paths: List[Dict[str, Any]] = field(default_factory=list)
    metacognitive_moments: List[Dict[str, Any]] = field(default_factory=list)
    emergent_discoveries: List[Dict[str, Any]] = field(default_factory=list)
    final_outcome: Dict[str, Any] = field(default_factory=dict)
    wisdom_extracted: Dict[str, List[str]] = field(default_factory=dict)


class CHAOSGenerator:
    """Generates CHAOS framework training data"""

    def __init__(self):
        self.scenarios = {
            "technical": [
                "Deploy a critical hotfix to production during peak traffic",
                "Debug memory leak in distributed system under load",
            ],
            "business": [
                "Prepare board presentation after key data source fails",
                "Handle PR crisis when product defect goes viral",
            ],
        }

        self.tools = {
            "technical": {
                "code_executor": "Run and test code",
                "log_analyzer": "Parse system logs",
                "monitoring_dashboard": "Real-time metrics",
            },
            "business": {
                "data_analyzer": "Statistical analysis",
                "presentation_builder": "Create slides",
            },
        }

    def generate_scenario(self, domain: str = "technical") -> Dict[str, Any]:
        """Generate a complete CHAOS scenario"""
        scenario_text = random.choice(
            self.scenarios.get(domain, self.scenarios["technical"])
        )
        scenario_text += " The CEO just called asking for an update."

        scenario = CHAOSScenario(
            scenario=scenario_text,
            difficulty=random.choice(["basic", "intermediate", "advanced", "chaotic"]),
            tools_available=self.tools.get(domain, self.tools["technical"]),
            constraints=(
                f"Time: {random.randint(2, 48)} hours, "
                f"Budget: ${random.randint(5, 100)}k"
            ),
        )

        # Add internal dialogue
        scenario.internal_dialogue.append(
            {
                "timestamp": 0,
                "voices": {
                    "optimizer": "We can parallelize tasks and save time",
                    "skeptic": "This approach has failed before",
                    "creative": "What if we combine tools differently?",
                },
                "resolution": "Proceeding with hybrid approach",
                "confidence": 70,
            }
        )

        # Add reality break
        scenario.reality_breaks.append(
            {
                "timestamp": 300,
                "discovery": "API returns XML not JSON",
                "internal_reaction": "This changes everything",
                "impact_assessment": "All parsing logic invalid",
                "adaptation": "Implementing XML parser",
            }
        )

        # Add confidence trajectory
        scenario.confidence_trajectory = [70, 60, 40, 65, 80]

        # Add final outcome
        scenario.final_outcome = {
            "success_level": "partial",
            "user_satisfaction": "85%",
            "lessons_learned": [
                "Hidden features exist",
                "Constraints force innovation",
            ],
            "innovation_index": 7.5,
        }

        return asdict(scenario)

    def generate_batch(self, count: int) -> List[Dict[str, Any]]:
        """Generate multiple scenarios"""
        return [self.generate_scenario() for _ in range(count)]

    def save_to_file(self, scenarios: List[Dict[str, Any]], filename: str):
        """Save scenarios to JSON file"""
        with open(filename, "w") as f:
            json.dump(scenarios, f, indent=2)
        print(f"Saved {len(scenarios)} scenarios to {filename}")


# Gemini Enhanced Generator (optional)
class GeminiEnhancedGenerator(CHAOSGenerator):
    def __init__(self, api_key: str = None):
        super().__init__()
        self.use_gemini = False
        if api_key:
            try:
                import google.generativeai as genai

                genai.configure(api_key=api_key)
                self.model = genai.GenerativeModel("gemini-pro")
                self.use_gemini = True
                print("Gemini integration enabled")
            except (ImportError, Exception) as e:
                print("Gemini integration failed - using basic generator")


if __name__ == "__main__":
    # Create generator
    generator = CHAOSGenerator()

    print("=== CHAOS Framework Data Generator ===\n")

    # Generate single scenario
    print("Generating single scenario...")
    scenario = generator.generate_scenario()
    print(f"Scenario: {scenario['scenario']}")
    print(f"Difficulty: {scenario['difficulty']}")
    print(f"Confidence trajectory: {scenario['confidence_trajectory']}\n")

    # Generate batch
    print("Generating batch of 5 scenarios...")
    scenarios = generator.generate_batch(5)
    generator.save_to_file(scenarios, "chaos_training_data.json")

    print("\nDone! Check chaos_training_data.json")

    # For Gemini integration:
    print("\n" + "=" * 50)
    print("To use Gemini enhancement:")
    print("1. Install: pip install google-generativeai")
    print("2. Get API key from: https://makersuite.google.com/app/apikey")
    print("3. Use: generator = GeminiEnhancedGenerator(api_key='YOUR_KEY')")
    print("=" * 50)

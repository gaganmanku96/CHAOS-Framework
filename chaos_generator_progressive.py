"""
CHAOS Framework Data Generator - Extended with Simple Tasks
Includes progressive difficulty from single-tool to complex multi-tool scenarios
"""

import json
import random
from typing import List, Dict, Any
from dataclasses import dataclass, field, asdict
from enum import Enum


class Difficulty(Enum):
    SIMPLE = "simple"  # Single tool, straightforward
    BASIC = "basic"  # 1-2 tools, minor complications
    INTERMEDIATE = "intermediate"  # 2-3 tools, reality breaks
    ADVANCED = "advanced"  # 3-4 tools, multiple pivots
    CHAOTIC = "chaotic"  # 4+ tools, constant adaptation


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
    """Generates CHAOS framework training data with progressive difficulty"""

    def __init__(self):
        # Simple single-tool scenarios
        self.simple_scenarios = {
            "technical": [
                "Run unit tests for the payment module",
                "Check server logs for errors in the last hour",
                "Deploy the staging branch to test environment",
                "Query database for user count",
                "Generate performance report for API endpoints",
            ],
            "business": [
                "Create a simple sales report for Q4",
                "Send meeting invite to team members",
                "Extract key metrics from spreadsheet",
                "Schedule follow-up with client",
                "Generate invoice from template",
            ],
            "research": [
                "Search for papers on neural networks",
                "Run statistical test on dataset",
                "Generate plot for experimental results",
                "Compile LaTeX document",
                "Check citations for formatting",
            ],
            "creative": [
                "Generate thumbnail for video",
                "Resize images for web",
                "Check content for grammar errors",
                "Export design assets",
                "Create simple color palette",
            ],
        }

        # Complex multi-tool scenarios
        self.complex_scenarios = {
            "technical": [
                "Deploy a critical hotfix to production during peak traffic",
                "Debug memory leak in distributed system under load",
                "Migrate database while maintaining zero downtime",
            ],
            "business": [
                "Prepare board presentation after key data source fails",
                "Handle PR crisis when product defect goes viral",
                "Coordinate product launch across multiple time zones",
            ],
            "research": [
                "Reproduce paper results with missing critical details",
                "Integrate conflicting datasets for meta-analysis",
                "Submit grant proposal with last-minute changes",
            ],
            "creative": [
                "Redesign UI after user testing reveals major issues",
                "Create marketing campaign with budget cut by 70%",
                "Produce video when key assets are corrupted",
            ],
        }

        self.tools = {
            "technical": {
                "code_executor": "Run and test code",
                "log_analyzer": "Parse system logs",
                "monitoring_dashboard": "Real-time metrics",
                "deployment_tool": "Deploy to environments",
                "database_client": "Query and modify databases",
                "test_runner": "Execute automated tests",
                "profiler": "Analyze performance",
            },
            "business": {
                "data_analyzer": "Statistical analysis",
                "presentation_builder": "Create slides",
                "email_client": "Communications",
                "calendar_system": "Schedule management",
                "spreadsheet_tool": "Work with data",
                "report_generator": "Create reports",
                "crm_system": "Customer data",
            },
            "research": {
                "paper_database": "Search literature",
                "statistical_package": "Run analyses",
                "plotting_tool": "Create figures",
                "latex_compiler": "Document preparation",
                "citation_manager": "Handle references",
                "code_executor": "Run experiments",
                "data_repository": "Access datasets",
            },
            "creative": {
                "design_tool": "Create graphics",
                "image_editor": "Edit images",
                "grammar_checker": "Review text",
                "asset_exporter": "Export files",
                "color_tool": "Generate palettes",
                "video_editor": "Edit videos",
                "render_engine": "Process media",
            },
        }

    def generate_simple_scenario(self, domain: str = "technical") -> Dict[str, Any]:
        """Generate a simple single-tool scenario"""
        scenario_text = random.choice(
            self.simple_scenarios.get(domain, self.simple_scenarios["technical"])
        )

        # Pick just 1-2 tools for simple tasks
        all_tools = self.tools[domain]
        tool_names = list(all_tools.keys())
        selected_tools = random.sample(tool_names, min(2, len(tool_names)))
        available_tools = {tool: all_tools[tool] for tool in selected_tools}

        scenario = CHAOSScenario(
            scenario=scenario_text,
            difficulty="simple",
            tools_available=available_tools,
            constraints="Time: 30 minutes",
        )

        # Simple internal dialogue - less debate
        scenario.internal_dialogue.append(
            {
                "timestamp": 0,
                "voices": {
                    "optimizer": "This is straightforward - use the standard approach",
                    "pragmatist": "Let's just get it done efficiently",
                },
                "resolution": "Using standard tool for the task",
                "confidence": 90,
            }
        )

        # High, stable confidence for simple tasks
        scenario.confidence_trajectory = [90, 85, 90]

        # Simple successful outcome
        scenario.final_outcome = {
            "success_level": "full",
            "user_satisfaction": "100%",
            "lessons_learned": ["Simple tasks need simple solutions"],
            "time_taken": "5 minutes",
            "complexity_score": 1.0,
        }

        return asdict(scenario)

    def generate_progressive_scenario(
        self, domain: str = "technical", difficulty: str = None
    ) -> Dict[str, Any]:
        """Generate scenario with specified difficulty level"""

        if difficulty == "simple" or difficulty is None:
            return self.generate_simple_scenario(domain)

        # For basic to chaotic, add progressive complexity
        if difficulty in ["basic", "intermediate"]:
            base_scenarios = self.simple_scenarios[domain]
            complication = (
                " But the system is running slowly."
                if difficulty == "basic"
                else " But multiple things go wrong."
            )
        else:
            base_scenarios = self.complex_scenarios[domain]
            complication = (
                " The CEO is watching."
                if difficulty == "advanced"
                else " Everything that can go wrong does."
            )

        scenario_text = random.choice(base_scenarios) + complication

        # Tool selection based on difficulty
        num_tools = {"basic": 2, "intermediate": 3, "advanced": 4, "chaotic": 6}.get(
            difficulty, 2
        )

        all_tools = self.tools[domain]
        tool_names = list(all_tools.keys())
        selected_tools = random.sample(tool_names, min(num_tools, len(tool_names)))
        available_tools = {tool: all_tools[tool] for tool in selected_tools}

        scenario = CHAOSScenario(
            scenario=scenario_text,
            difficulty=difficulty,
            tools_available=available_tools,
            constraints=f"Time: {random.randint(1, 6)} hours",
        )

        # Add complexity based on difficulty
        if difficulty in ["intermediate", "advanced", "chaotic"]:
            # Add reality breaks
            scenario.reality_breaks.append(
                {
                    "timestamp": 300,
                    "discovery": "Tool behaves differently than expected",
                    "internal_reaction": "Need to adapt approach",
                    "impact_assessment": "Medium impact",
                    "adaptation": "Finding workaround",
                }
            )

        if difficulty in ["advanced", "chaotic"]:
            # Add metacognitive moments
            scenario.metacognitive_moments.append(
                {
                    "timestamp": 600,
                    "thought": "Am I overcomplicating this?",
                    "adjustment": "Stepping back to reassess",
                }
            )

        # Confidence trajectory based on difficulty
        confidence_patterns = {
            "basic": [80, 70, 85],
            "intermediate": [75, 60, 50, 70, 80],
            "advanced": [70, 50, 30, 45, 65, 75],
            "chaotic": [70, 40, 20, 35, 25, 40, 60, 70],
        }
        scenario.confidence_trajectory = confidence_patterns.get(
            difficulty, [70, 60, 80]
        )

        # Outcome varies by difficulty
        success_levels = {
            "basic": "full",
            "intermediate": "full",
            "advanced": "partial",
            "chaotic": "partial",
        }

        scenario.final_outcome = {
            "success_level": success_levels.get(difficulty, "partial"),
            "user_satisfaction": f"{random.randint(70, 95)}%",
            "lessons_learned": ["Match solution complexity to problem complexity"],
            "complexity_score": {
                "basic": 2,
                "intermediate": 4,
                "advanced": 7,
                "chaotic": 9,
            }.get(difficulty, 5),
        }

        return asdict(scenario)

    def generate_curriculum_batch(
        self, count_per_level: int = 5
    ) -> List[Dict[str, Any]]:
        """Generate a curriculum with progressive difficulty"""
        scenarios = []
        difficulties = ["simple", "basic", "intermediate", "advanced", "chaotic"]
        domains = ["technical", "business", "research", "creative"]

        for difficulty in difficulties:
            for _ in range(count_per_level):
                domain = random.choice(domains)
                scenario = self.generate_progressive_scenario(domain, difficulty)
                scenarios.append(scenario)

        return scenarios

    def save_curriculum(
        self, scenarios: List[Dict[str, Any]], base_filename: str = "chaos_curriculum"
    ):
        """Save curriculum organized by difficulty"""
        by_difficulty = {}
        for scenario in scenarios:
            diff = scenario["difficulty"]
            if diff not in by_difficulty:
                by_difficulty[diff] = []
            by_difficulty[diff].append(scenario)

        # Save complete curriculum
        with open(f"{base_filename}_complete.json", "w") as f:
            json.dump(scenarios, f, indent=2)

        # Save by difficulty level
        for difficulty, scenes in by_difficulty.items():
            with open(f"{base_filename}_{difficulty}.json", "w") as f:
                json.dump(scenes, f, indent=2)

        print(f"Saved curriculum with {len(scenarios)} scenarios")
        for diff, scenes in by_difficulty.items():
            print(f"  {diff}: {len(scenes)} scenarios")


if __name__ == "__main__":
    generator = CHAOSGenerator()

    print("=== CHAOS Framework Progressive Data Generator ===\n")

    # Generate examples at each difficulty level
    print("Generating examples at each difficulty level...\n")

    for difficulty in ["simple", "basic", "intermediate", "advanced", "chaotic"]:
        scenario = generator.generate_progressive_scenario("technical", difficulty)
        print(f"{difficulty.upper()} scenario:")
        print(f"  Task: {scenario['scenario'][:60]}...")
        print(f"  Tools: {len(scenario['tools_available'])}")
        print(f"  Confidence: {scenario['confidence_trajectory']}")
        print(f"  Complexity: {scenario['final_outcome']['complexity_score']}\n")

    # Generate full curriculum
    print("Generating complete curriculum...")
    curriculum = generator.generate_curriculum_batch(count_per_level=10)
    generator.save_curriculum(curriculum, "chaos_curriculum")

    print("\nDone! Files created:")
    print("- chaos_curriculum_complete.json (all scenarios)")
    print("- chaos_curriculum_simple.json")
    print("- chaos_curriculum_basic.json")
    print("- chaos_curriculum_intermediate.json")
    print("- chaos_curriculum_advanced.json")
    print("- chaos_curriculum_chaotic.json")

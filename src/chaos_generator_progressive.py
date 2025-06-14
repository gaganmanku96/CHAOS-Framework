"""
CHAOS Framework Data Generator - Extended with Simple Tasks
Includes progressive difficulty from single-tool to complex multi-tool scenarios
"""

import json
import random
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field, asdict
from enum import Enum
import os


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


@dataclass
class AlpacaEntry:
    """Alpaca format training entry for PEFT"""

    instruction: str
    input: str = ""
    output: str = ""


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

    def convert_to_alpaca_format(self, scenario: Dict[str, Any]) -> AlpacaEntry:
        """Convert CHAOS scenario to Alpaca format for PEFT training"""

        # Create instruction based on scenario and constraints
        instruction = f"You are an AI assistant helping with a {scenario['difficulty']} difficulty task. {scenario['scenario']} {scenario['constraints']}"

        # Create context input with available tools
        tools_list = ", ".join(
            [f"{name}: {desc}" for name, desc in scenario["tools_available"].items()]
        )
        input_text = f"Available tools: {tools_list}"

        # Create response with internal reasoning and actions
        response_parts = []

        # Add internal reasoning
        if scenario.get("internal_dialogue"):
            response_parts.append("**Internal Analysis:**")
            for dialogue in scenario["internal_dialogue"]:
                if "voices" in dialogue:
                    for voice, thought in dialogue["voices"].items():
                        response_parts.append(f"- {voice.title()}: {thought}")
                    response_parts.append(
                        f"Resolution: {dialogue.get('resolution', 'Proceeding with plan')}"
                    )
                    response_parts.append(
                        f"Confidence: {dialogue.get('confidence', 70)}%"
                    )

        # Add confidence trajectory
        if scenario.get("confidence_trajectory"):
            response_parts.append(
                f"\\n**Confidence Progression:** {scenario['confidence_trajectory']}"
            )

        # Add reality breaks and adaptations
        if scenario.get("reality_breaks"):
            response_parts.append("\\n**Adaptation Moments:**")
            for break_event in scenario["reality_breaks"]:
                response_parts.append(
                    f"- Discovery: {break_event.get('discovery', 'Unexpected situation')}"
                )
                response_parts.append(
                    f"- Adaptation: {break_event.get('adaptation', 'Adjusting approach')}"
                )

        # Add final outcome
        if scenario.get("final_outcome"):
            outcome = scenario["final_outcome"]
            response_parts.append(f"\\n**Final Outcome:**")
            response_parts.append(
                f"- Success Level: {outcome.get('success_level', 'partial')}"
            )
            response_parts.append(
                f"- User Satisfaction: {outcome.get('user_satisfaction', 'N/A')}"
            )
            if outcome.get("lessons_learned"):
                response_parts.append(
                    f"- Key Lessons: {', '.join(outcome['lessons_learned'])}"
                )

        output_text = "\\n".join(response_parts)

        return AlpacaEntry(
            instruction=instruction, input=input_text, output=output_text
        )

    def generate_alpaca_dataset(
        self, scenarios: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """Convert CHAOS scenarios to Alpaca format dataset"""
        alpaca_entries = []
        for scenario in scenarios:
            entry = self.convert_to_alpaca_format(scenario)
            alpaca_entries.append(asdict(entry))
        return alpaca_entries

    def save_alpaca_format(
        self,
        scenarios: List[Dict[str, Any]],
        filename: str = "chaos_alpaca_dataset.json",
    ):
        """Save scenarios in Alpaca format for PEFT training"""
        alpaca_data = self.generate_alpaca_dataset(scenarios)

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(alpaca_data, f, indent=2, ensure_ascii=False)

        print(f"Saved {len(alpaca_data)} Alpaca format entries to {filename}")
        return alpaca_data


# Gemini Enhanced Generator for Variety and Bulk Generation
class GeminiEnhancedGenerator(CHAOSGenerator):
    def __init__(self, api_key: Optional[str] = None):
        super().__init__()
        self.use_gemini = False
        self.model = None

        if api_key:
            try:
                import google.generativeai as genai

                genai.configure(api_key=api_key)
                self.model = genai.GenerativeModel("gemini-2.5-flash-preview-05-20")
                self.use_gemini = True
                print("Gemini integration enabled for enhanced variety")
            except ImportError:
                print(
                    "google-generativeai not installed. Run: pip install google-generativeai"
                )
            except Exception as e:
                print(f"Gemini integration failed: {e}")

    def generate_diverse_scenarios_for_usecase(
        self, usecase: str, domain: str = "technical", count: int = 250
    ) -> List[Dict[str, Any]]:
        """Generate diverse scenarios for a specific usecase using Gemini for variety"""

        if not self.use_gemini:
            print("Gemini not available, using basic generation with permutations")
            return self._generate_permutation_scenarios(usecase, domain, count)

        scenarios = []
        difficulties = ["simple", "basic", "intermediate", "advanced", "chaotic"]
        scenarios_per_difficulty = count // len(difficulties)

        for difficulty in difficulties:
            for batch in range(
                0, scenarios_per_difficulty, 10
            ):  # Generate in batches of 10
                batch_scenarios = self._generate_gemini_batch(
                    usecase,
                    domain,
                    difficulty,
                    min(10, scenarios_per_difficulty - batch),
                )
                scenarios.extend(batch_scenarios)

        # Fill remaining slots with mixed difficulties
        remaining = count - len(scenarios)
        if remaining > 0:
            mixed_scenarios = self._generate_gemini_batch(
                usecase, domain, "mixed", remaining
            )
            scenarios.extend(mixed_scenarios)

        return scenarios[:count]  # Ensure exact count

    def _generate_gemini_batch(
        self, usecase: str, domain: str, difficulty: str, batch_size: int
    ) -> List[Dict[str, Any]]:
        """Generate a batch of diverse scenarios using Gemini"""

        prompt = f"""Generate {batch_size} diverse and realistic scenarios for CHAOS framework training.

USECASE: {usecase}
DOMAIN: {domain}
DIFFICULTY: {difficulty}

Requirements:
1. Each scenario should be unique and realistic
2. Vary the context, constraints, and complications
3. Include different stakeholder pressures (CEO, client, team, etc.)
4. Add variety in time constraints, resource limitations, and technical challenges
5. Make scenarios that would teach an AI to think adaptively

For {difficulty} difficulty:
- Simple: 1 tool, straightforward task, minimal complications
- Basic: 1-2 tools, minor issues to resolve
- Intermediate: 2-3 tools, reality breaks that require adaptation
- Advanced: 3-4 tools, complex multi-step reasoning
- Chaotic: 4+ tools, constant pivoting and adaptation needed
- Mixed: Random difficulty from above

Return only a JSON list of scenario descriptions (strings), no other text:
["scenario 1 description", "scenario 2 description", ...]"""

        try:
            response = self.model.generate_content(prompt)
            scenarios_text = response.text.strip()

            # Parse JSON response
            import re

            json_match = re.search(r"\[(.*?)\]", scenarios_text, re.DOTALL)
            if json_match:
                scenarios_list = json.loads(json_match.group(0))
            else:
                scenarios_list = json.loads(scenarios_text)

            # Convert to full CHAOS scenarios
            full_scenarios = []
            for scenario_text in scenarios_list:
                if difficulty == "mixed":
                    chosen_difficulty = random.choice(
                        ["simple", "basic", "intermediate", "advanced", "chaotic"]
                    )
                else:
                    chosen_difficulty = difficulty

                # Override scenario text in the generation
                scenario = self.generate_progressive_scenario(domain, chosen_difficulty)
                scenario["scenario"] = scenario_text + f" (Generated for {usecase})"
                full_scenarios.append(scenario)

            return full_scenarios

        except Exception as e:
            print(f"Gemini generation failed: {e}")
            # Fallback to basic generation
            return self._generate_permutation_scenarios(
                usecase, domain, batch_size, difficulty
            )

    def _generate_permutation_scenarios(
        self, usecase: str, domain: str, count: int, difficulty: str = None
    ) -> List[Dict[str, Any]]:
        """Generate scenarios using permutations when Gemini is not available"""
        scenarios = []

        # Enhanced base scenarios for the usecase
        usecase_modifiers = [
            f"while implementing {usecase}",
            f"during {usecase} rollout",
            f"when {usecase} fails unexpectedly",
            f"while troubleshooting {usecase}",
            f"during {usecase} optimization",
            f"when scaling {usecase}",
            f"while integrating {usecase}",
            f"during {usecase} migration",
        ]

        complications = [
            "The system is under heavy load",
            "Key team members are unavailable",
            "The deadline was moved up by 2 days",
            "Budget has been cut by 50%",
            "A competitor just launched similar features",
            "Regulatory requirements changed",
            "The primary vendor is having issues",
            "Critical data is corrupted",
            "Network connectivity is intermittent",
            "The client is extremely demanding",
        ]

        difficulties = (
            ["simple", "basic", "intermediate", "advanced", "chaotic"]
            if not difficulty
            else [difficulty]
        )

        for i in range(count):
            chosen_difficulty = random.choice(difficulties)
            modifier = random.choice(usecase_modifiers)
            complication = random.choice(complications)

            base_scenario = f"Handle technical issues {modifier}. {complication}."

            # Generate full scenario
            scenario = self.generate_progressive_scenario(domain, chosen_difficulty)
            scenario["scenario"] = base_scenario
            scenarios.append(scenario)

        return scenarios


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

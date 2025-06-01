# Progressive CHAOS Training Curriculum

## Overview
A structured approach to training agentic AI systems, starting with simple single-tool tasks and progressively increasing complexity.

## Difficulty Levels

### 1. SIMPLE (Single Tool)
**Characteristics:**
- One primary tool
- Clear, straightforward task
- No complications
- High confidence (85-95%)
- 5-30 minute tasks

**Example:**
```json
{
  "scenario": "Run unit tests for the payment module",
  "tools_available": {"test_runner": "Execute automated tests"},
  "confidence_trajectory": [90, 85, 90],
  "complexity_score": 1.0
}
```

**Learning Goals:**
- Basic tool usage
- Direct problem-solution mapping
- When NOT to overthink

### 2. BASIC (1-2 Tools)
**Characteristics:**
- 1-2 tools needed
- Minor complications
- Slight confidence dips
- 30-60 minute tasks

**Example:**
```json
{
  "scenario": "Check server logs for errors. But the system is running slowly.",
  "tools_available": {
    "log_analyzer": "Parse system logs",
    "monitoring_dashboard": "Real-time metrics"
  },
  "confidence_trajectory": [80, 70, 85],
  "complexity_score": 2.0
}
```

**Learning Goals:**
- Tool selection
- Handling minor obstacles
- Basic adaptation

### 3. INTERMEDIATE (2-3 Tools)
**Characteristics:**
- 2-3 tools required
- Reality breaks occur
- Confidence swings
- 1-3 hour tasks

**Example:**
```json
{
  "scenario": "Deploy staging branch to test environment. But multiple things go wrong.",
  "reality_breaks": [{
    "discovery": "Deployment tool timeout",
    "adaptation": "Manual deployment steps"
  }],
  "confidence_trajectory": [75, 60, 50, 70, 80],
  "complexity_score": 4.0
}
```

**Learning Goals:**
- Multi-tool orchestration
- Handling unexpected failures
- Strategy pivoting

### 4. ADVANCED (3-4 Tools)
**Characteristics:**
- 3-4 tools needed
- Multiple reality breaks
- Metacognitive moments
- Internal debate
- 3-6 hour tasks

**Example:**
```json
{
  "scenario": "Debug memory leak in distributed system. The CEO is watching.",
  "internal_dialogue": [{
    "voices": {
      "optimizer": "Quick fix for demo",
      "skeptic": "Root cause needed",
      "creative": "Use monitoring as diagnostic"
    }
  }],
  "metacognitive_moments": [{
    "thought": "Am I solving the right problem?"
  }],
  "complexity_score": 7.0
}
```

**Learning Goals:**
- Complex reasoning
- Balancing competing priorities
- Creative tool combination

### 5. CHAOTIC (4+ Tools)
**Characteristics:**
- 4+ tools required
- Constant pivoting
- Multiple abandoned paths
- Low confidence valleys
- Emergent discoveries
- 6+ hour tasks

**Example:**
```json
{
  "scenario": "Migrate database with zero downtime. Everything that can go wrong does.",
  "abandoned_paths": [
    {"approach": "Standard migration", "reason": "Too slow"},
    {"approach": "Parallel processing", "reason": "Data corruption"}
  ],
  "emergent_discoveries": [{
    "type": "tool_synthesis",
    "insight": "Cache + load balancer = zero downtime"
  }],
  "confidence_trajectory": [70, 40, 20, 35, 25, 40, 60, 70],
  "complexity_score": 9.0
}
```

**Learning Goals:**
- Handling extreme uncertainty
- Learning from failures
- Innovation under pressure
- Complex tool synthesis

## Training Progression

### Phase 1: Foundation (Weeks 1-2)
- 70% Simple scenarios
- 20% Basic scenarios
- 10% Intermediate scenarios
- **Goal**: Solid tool usage, avoid overcomplication

### Phase 2: Building Complexity (Weeks 3-4)
- 20% Simple scenarios
- 40% Basic scenarios
- 30% Intermediate scenarios
- 10% Advanced scenarios
- **Goal**: Multi-tool coordination, basic adaptation

### Phase 3: Advanced Problem Solving (Weeks 5-6)
- 10% Basic scenarios
- 30% Intermediate scenarios
- 40% Advanced scenarios
- 20% Chaotic scenarios
- **Goal**: Complex reasoning, creative solutions

### Phase 4: Mastery (Weeks 7-8)
- 20% Intermediate scenarios
- 40% Advanced scenarios
- 40% Chaotic scenarios
- **Goal**: Expert-level adaptation, innovation

## Key Learning Principles

### 1. Appropriate Complexity
Models learn to match solution complexity to problem complexity:
- Simple problem → Simple solution
- Complex problem → Sophisticated approach

### 2. Progressive Confidence
Models develop realistic confidence patterns:
- High confidence on simple tasks
- Appropriate uncertainty on complex tasks
- Recovery from confidence drops

### 3. Tool Mastery Progression
- Single tool mastery
- Tool selection skills
- Tool combination
- Tool synthesis innovation

### 4. Failure Handling Evolution
- Simple: Failures are rare
- Basic: Minor workarounds
- Intermediate: Pivot strategies
- Advanced: Learn from failures
- Chaotic: Failures drive innovation

## Evaluation Metrics

### 1. Task Completion Rate by Difficulty
- Simple: 95-100%
- Basic: 90-95%
- Intermediate: 80-90%
- Advanced: 70-85%
- Chaotic: 60-80%

### 2. Appropriate Complexity Score
Measure if the model uses appropriately complex solutions:
- Overengineering simple tasks: -1 point
- Appropriate complexity: +1 point
- Under-engineering complex tasks: -1 point

### 3. Adaptation Quality
- Speed of pivot when needed
- Quality of alternative approaches
- Learning from failures

### 4. Innovation Index
- Novel tool combinations
- Creative constraint handling
- Emergent discoveries

## Implementation Guide

```python
from chaos_generator_progressive import CHAOSGenerator

# Create generator
generator = CHAOSGenerator()

# Generate curriculum
curriculum = generator.generate_curriculum_batch(count_per_level=100)

# Save organized by difficulty
generator.save_curriculum(curriculum, "training_data")

# Custom training loop
for week in range(1, 9):
    if week <= 2:  # Foundation
        weights = {"simple": 0.7, "basic": 0.2, "intermediate": 0.1}
    elif week <= 4:  # Building
        weights = {"simple": 0.2, "basic": 0.4, "intermediate": 0.3, "advanced": 0.1}
    elif week <= 6:  # Advanced
        weights = {"basic": 0.1, "intermediate": 0.3, "advanced": 0.4, "chaotic": 0.2}
    else:  # Mastery
        weights = {"intermediate": 0.2, "advanced": 0.4, "chaotic": 0.4}
    
    # Train with weighted sampling
```

## Expected Outcomes

After progressive training, models should:

1. **Recognize Task Complexity**: Automatically identify whether a task needs simple or complex approach
2. **Avoid Overengineering**: Use simple tools for simple tasks
3. **Handle Complexity Gracefully**: Sophisticated reasoning for complex tasks
4. **Adapt Intelligently**: Pivot strategies based on discoveries
5. **Learn from Experience**: Extract wisdom from failures
6. **Innovate When Needed**: Discover novel solutions under pressure

## Conclusion

This progressive curriculum ensures models develop both:
- **Competence**: Ability to handle tasks at all complexity levels
- **Wisdom**: Knowing when to use simple vs complex approaches

The result is an AI system that thinks like an expert: simple when possible, sophisticated when necessary, always adaptive.

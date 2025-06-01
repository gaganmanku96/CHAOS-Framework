# Contributing to CHAOS Framework

We love your input! We want to make contributing to CHAOS Framework as easy and transparent as possible.

## Ways to Contribute

1. **Report Bugs** - Use GitHub Issues
2. **Propose New Features** - Use GitHub Discussions first
3. **Submit Pull Requests** - Fix bugs or add features
4. **Improve Documentation** - Help others understand CHAOS better
5. **Share Results** - Tell us how CHAOS worked for your AI

## Pull Request Process

1. Fork the repo and create your branch from `main`
2. Add tests if you've added code
3. Update documentation as needed
4. Ensure all tests pass
5. Issue your pull request!

## Adding New Scenario Types

To add new domains or scenarios:

1. Edit `src/chaos_generator_progressive.py`
2. Add to `self.scenario_templates` 
3. Add corresponding tools to `self.tool_sets`
4. Include examples in your PR

Example:
```python
self.scenario_templates["medical"] = [
    "Diagnose patient with conflicting symptoms",
    "Handle emergency with limited resources"
]
```

## Code Style

- Use descriptive variable names
- Add comments for complex logic
- Follow PEP 8 guidelines
- Keep functions focused and small

## Reporting Bugs

**Great Bug Reports** include:
- Quick summary
- Steps to reproduce
- Expected behavior
- Actual behavior
- Additional context

## License

By contributing, you agree that your contributions will be licensed under MIT License.
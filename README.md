# BMAD - Build, Manage, Analyze, Deploy with AI

![BMAD Methodology](https://img.shields.io/badge/Methodology-BMAD-blue)
![AI Assisted](https://img.shields.io/badge/Development-AI%20Assisted-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🚀 Introduction

The BMAD methodology represents a paradigm shift in software development by leveraging AI assistants as a virtual product team. Instead of using AI tools merely for code generation, BMAD creates a structured approach where different AI personas collaborate on your project, each with specialized roles and responsibilities.

Inspired by the [BMad Code YouTube tutorial](https://www.youtube.com/watch?v=p0barbrWgQA) on building complex applications with free AI, this repository provides templates, tools, and implementation guides to help you apply the BMAD methodology to your own projects.

## 🧠 The BMAD Philosophy

Traditional development often involves a single developer wearing multiple hats or requires assembling a team of specialists. The BMAD approach creates a virtual team using role-specific AI prompts:

1. **You as CEO/Product Owner**: You guide the vision and make final decisions
2. **Project Manager AI**: Handles requirements, planning, and coordination
3. **Senior Developer AI**: Designs architecture and makes technical decisions
4. **Junior Developer AI**: Implements specific features based on specifications
5. **QA Engineer AI**: Tests functionality and identifies issues
6. **Technical Writer AI**: Creates documentation for users and developers

By structuring your interactions with AI assistants through these specific roles, you gain specialized expertise for each aspect of development while maintaining a cohesive development process.

## 📂 Repository Contents

### Role Prompts

The `/Role_Prompts` directory contains specialized prompts for each AI team member:

- **Project Manager**: Requirements gathering, task breakdown, risk management
- **Senior Developer**: Architecture design, technical leadership, technology selection
- **Junior Developer**: Feature implementation, bug fixing, testing
- **QA Engineer**: Test planning, defect detection, quality advocacy
- **Technical Writer**: User documentation, developer documentation, content organization

### YouTube Tutorial Extraction

The repository includes tools for extracting structured information from YouTube tutorials:

- `/docs/example_extraction.md`: A comprehensive example showing how to document tutorial content
- `/How_to_Plan_Build_Complex_Apps_with_Free_AI/youtube_extractor.py`: A Python script for generating project templates from YouTube tutorials

### BMAD V2 Tutorial Documentation

Complete documentation of the BMAD V2 methodology based on the YouTube tutorial:

- `/How_to_Plan_Build_Complex_Apps_with_Free_AI_BMAD_V2_Full_Workflow_Tutorial/extraction_template.md`: Detailed breakdown of the methodology
- `/How_to_Plan_Build_Complex_Apps_with_Free_AI_BMAD_V2_Full_Workflow_Tutorial/workflow_guide.md`: Step-by-step implementation guide

### Project Structure

A basic project structure to get you started:

- `/src/`: Source code directory
- `/tests/`: Test files
- `/docs/`: Additional documentation

## 🛠️ Getting Started

### Using the Role Prompts

1. Choose the appropriate role prompt for your current task
2. Copy the prompt and paste it into your conversation with an AI assistant
3. Replace placeholder text with your project-specific details
4. Begin your AI-assisted development process

Detailed instructions are available in the [Role Prompts README](/Role_Prompts/README.md).

### Using the YouTube Tutorial Extractor

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the extractor with a YouTube URL:
   ```bash
   cd How_to_Plan_Build_Complex_Apps_with_Free_AI
   python youtube_extractor.py "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"
   ```

3. Fill out the generated templates as you watch the tutorial

## 📚 Example Workflow

1. **Project Initiation**:
   - Use the Project Manager AI to define requirements and create a plan
   - Document the project scope and objectives

2. **Architecture Design**:
   - Switch to the Senior Developer AI role
   - Design the system architecture and make key technical decisions

3. **Implementation**:
   - Use the Junior Developer AI to write code for specific features
   - Implement one component at a time based on specifications

4. **Quality Assurance**:
   - Have the QA Engineer AI review implementations and identify issues
   - Create and execute test cases

5. **Documentation**:
   - Use the Technical Writer AI to create user guides and API documentation
   - Ensure all features are properly documented

## 🔄 The BMAD Cycle

The BMAD methodology is iterative and follows this cycle:

1. **Build**: Create initial implementation with Junior Developer AI
2. **Manage**: Track progress and adjust plans with Project Manager AI
3. **Analyze**: Test and review with QA Engineer AI
4. **Deploy**: Prepare for deployment with Senior Developer AI

Rinse and repeat for each feature or component.

## 🤝 Contributing

Contributions to the BMAD methodology and tools are welcome! Please feel free to submit pull requests with improvements to the templates, additional role definitions, or enhanced tools.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔗 Resources

- [BMAD V2 Full Workflow Tutorial](https://www.youtube.com/watch?v=p0barbrWgQA) - Original tutorial by BMad Code
- [Prompt Engineering Guide](https://www.promptingguide.ai/) - Helpful resource for creating effective prompts

---

<p align="center">Created with ❤️ using the BMAD methodology</p>

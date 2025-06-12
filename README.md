# Brand Monitoring Crew

Welcome to the Brand Monitoring Crew project, powered by [crewAI](https://crewai.com). This project is designed to create brand summaries using agents, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on generating comprehensive brand summaries, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/testing_crew/config/agents.yaml` to define your agents
- Modify `src/testing_crew/config/tasks.yaml` to define your tasks
- Modify `src/testing_crew/crew.py` to add your own logic, tools and specific args
- Modify `src/testing_crew/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the testing_crew Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The testing_crew Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the Brand Monitoring Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.


```mermaid
flowchart TD
    A[Start: Install Python 3.10-3.12] --> B[Install UV Package Manager]
    B --> C[Navigate to Project Directory]
    C --> D[Install Dependencies with `crewai install`]
    D --> E[Add `OPENAI_API_KEY` to .env]
    E --> F[Configure Agents in agents.yaml]
    F --> G[Configure Tasks in tasks.yaml]
    G --> H[Customize Logic in crew.py]
    H --> I[Customize Inputs in main.py]
    I --> J[Run Project with `crewai run`]
    J --> K[Agents Collaborate on Tasks]
    K --> L[Generate report.md Output]
    L --> M[End]
```

```mermaid
sequenceDiagram
    participant User as actor User
    participant TestingCrew as TestingCrew
    participant LLM as llmGemini (LLM)
    participant SerperDevTool as tool_google_search
    participant Researcher as Researcher Agent
    participant ReportingAnalyst as Reporting Analyst Agent
    participant Crew as Crew

    User->>TestingCrew: Instantiate TestingCrew()
    TestingCrew->>LLM: Initialize LLM (Gemini)
    TestingCrew->>SerperDevTool: Initialize SerperDevTool
    TestingCrew->>TestingCrew: Load config.yaml
    User->>TestingCrew: Start crew()
    TestingCrew->>Researcher: researcher() (with LLM, tool_google_search)
    TestingCrew->>ReportingAnalyst: reporting_analyst() (with LLM)
    TestingCrew->>Researcher: research_task() (assigns Researcher)
    TestingCrew->>ReportingAnalyst: reporting_task() (assigns ReportingAnalyst)
    TestingCrew->>Crew: crew() (with agents, tasks, sequential process)
    User->>TestingCrew: Run before_kickoff_function(inputs)
    TestingCrew->>TestingCrew: before_kickoff_function logic
    Crew->>Researcher: Execute research_task
    Researcher->>SerperDevTool: Use Google Search Tool
    Researcher->>LLM: Use LLM for research
    Crew->>ReportingAnalyst: Execute reporting_task
    ReportingAnalyst->>LLM: Use LLM for reporting
    Crew->>TestingCrew: Return result
    TestingCrew->>TestingCrew: after_kickoff_function(result)
    TestingCrew->>User: Return final result
```

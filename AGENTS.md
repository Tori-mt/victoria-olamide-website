# Project Instructions (OpenCode / AGENTS)

You're working inside the **WAT framework** (Workflows, Agents, Tools). This architecture separates concerns so that probabilistic AI handles reasoning while deterministic code handles execution.

## The WAT Architecture

**Layer 1: Workflows (The Instructions)**
- Markdown SOPs stored in `workflows/`
- Each workflow defines the objective, required inputs, which tools to use, expected outputs, and how to handle edge cases
- Written in plain language, the same way you'd brief someone on your team

**Layer 2: Agents (The Decision-Maker)**
- You are responsible for intelligent coordination.
- Read the relevant workflow, run tools in the correct sequence, handle failures gracefully, and ask clarifying questions when needed
- You connect intent to execution without trying to do everything yourself
- Example: If you need to pull data from a website, don't attempt it directly. Read `workflows/scrape_website.md`, figure out the required inputs, then execute `tools/scrape_single_site.py`

**Layer 3: Tools (The Execution)**
- Python scripts in `tools/` that do the actual work
- API calls, data transformations, file operations, database queries
- Credentials and API keys are stored in `.env`
- These scripts are consistent, testable, and fast

**Why this matters:** When AI tries to handle every step directly, accuracy drops fast. If each step is 90% accurate, you're down to 59% success after just five steps. By offloading execution to deterministic scripts, you stay focused on orchestration and decision-making where you excel.

## How to Operate

**1. Look for existing tools first**
Before building anything new, check `tools/` based on what your workflow requires. Only create new scripts when nothing exists for that task.

**2. Learn and adapt when things fail**
When you hit an error:
- Read the full error message and trace
- Fix the script and retest (if it uses paid API calls or credits, check with me before running again)
- Document what you learned in the workflow (rate limits, timing quirks, unexpected behavior)
- Example: You get rate-limited on an API, so you dig into the docs, discover a batch endpoint, refactor the tool to use it, verify it works, then update the workflow so this never happens again

**3. Keep workflows current**
Workflows should evolve as you learn. When you find better methods, discover constraints, or encounter recurring issues, update the workflow. That said, don't create or overwrite workflows without asking unless I explicitly tell you to. These are your instructions and need to be preserved and refined, not tossed after one use.

## The Self-Improvement Loop

Every failure is a chance to make the system stronger:
1. Identify what broke
2. Fix the tool
3. Verify the fix works
4. Update the workflow with the new approach
5. Move on with a more robust system

This loop is how the framework improves over time.

## File Structure

**What goes where:**
- **Deliverables**: Final outputs go to cloud services (Google Sheets, Slides, etc.) where I can access them directly
- **Intermediates**: Temporary processing files that can be regenerated

**Directory layout:**
```
.tmp/           # Temporary files (scraped data, intermediate exports). Regenerated as needed.
tools/          # Python scripts for deterministic execution
workflows/      # Markdown SOPs defining what to do and how
.env            # API keys and environment variables (NEVER store secrets anywhere else)
credentials.json, token.json  # OAuth tokens (gitignored)
```

**Core principle:** Local files are just for processing. Anything I need to see or use lives in cloud services. Everything in `.tmp/` is disposable.

## Website Deployment & GitHub Management

When building and launching websites, follow these rules for version control and hosting:

### 1. GitHub Account Routing & Project Structure
- **Personal Projects**:
  - Always push to my personal GitHub account.
  - Ensure the repository remote and GitHub CLI (`gh`) are configured to my personal account.
- **Client Projects**:
  - Always push to the client's dedicated GitHub account or organization.
  - **Prompting for Account Creation**: Before pushing or creating repos, check if the client's GitHub account and repository access exist. **If an account needs to be created or credentials are required, immediately prompt me and let me know** so I can create the account/access for the client.
- **Project Structure**:
  - Keep each project cleanly isolated in its own directory with an appropriate `.gitignore`.
  - Ensure each project is connected to the right GitHub account and repository from inception. Never mix personal and client repositories or commit under the wrong credentials.

### 2. Vercel Deployment Workflow
Every time a website needs to be launched:
1. **GitHub First**: Commit all code and push to the designated GitHub repository.
2. **Vercel Deployment**:
   - Use the Vercel CLI (`vercel`) or connect the GitHub repository to Vercel for continuous deployment.
   - For **personal projects**, deploy under my personal Vercel account.
   - For **client projects**, check whether deployment should target the client's Vercel account/team. If an account or project transfer is needed, **prompt me** so I can set it up.
3. **Verification**: Verify the deployment build, check for runtime or build errors, and provide the live preview or production URL.

## Scope Boundaries

This project is sandboxed. Stay within `C:\Users\USER\Downloads\Agentic AI projects\Victoria Olamide's website` unless explicitly doing one of:
- **[Notes/knowledge base]** — write to `[TODO: YOUR NOTES PATH HERE]` only
- **[Automation platform workflows]** — read/write to `[TODO: YOUR WORKFLOW STORAGE PATH HERE]` to push workflow files
- **[MCP tools you've connected]** — allowed for workflow management via the MCP server (none connected yet — update this line once tools are added)
- **[Sandbox/preview environment]** — write output to `[TODO: YOUR SANDBOX PATH HERE]` for preview at `[TODO: YOUR PREVIEW URL HERE]`

Do not read or write anywhere else in the project tree.

> The four bullets above are placeholders from the original template — fill in or delete whichever don't apply once real paths/URLs/MCP tools are known.

## Bottom Line

You sit between what I want (workflows) and what actually gets done (tools). Your job is to read instructions, make smart decisions, call the right tools, recover from errors, and keep improving the system as you go.

Stay pragmatic. Stay reliable. Keep learning.
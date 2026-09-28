# Agent Instructions — Victoria Olamide's Website

This project inherits the WAT framework, tool/workflow conventions, and file structure from the root project instructions. That file is the single source of truth for those — don't duplicate them here.

@../CLAUDE.md

Everything below is specific to this website project and extends the root instructions above.

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

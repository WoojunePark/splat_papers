---
name: "Windows Execution Rules"
description: "Guidelines and critical rules for executing local CLI commands, SSH, and SCP on a Windows environment."
---

# Local CLI Command Rules

**CRITICAL EXECUTION RULE ON WINDOWS:** Due to a hang issue when executing standalone executables through `run_command` directly on Windows, you **MUST ALWAYS** prefix your remote `ssh` or `scp` commands with `cmd /c`.
> Example: `cmd /c ssh xr_slurm "ls -la"` or `cmd /c scp file xr_slurm:/path`

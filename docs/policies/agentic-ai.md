Agentic AI systems, such as Claude Code and Codex, have become widely used in both industry and the academic community.
These systems are allowed on our clusters, but users must follow our guidelines to make sure their agents do not degrade our services.

__*Users are responsible for the actions of their agents.
Users whose agents contribute to service degradation or perform actions meant to bypass our policies, such as login node abuse, are subject to having their access suspended.*__

## Problem Behaviors

From our observations, agents tend to engage in their own variety of problematic behaviors that contribute to service degradation.
These behaviors may include:

- Open-ended recursive `find` and related commands (`grep`, `ripgrep`, etc.). Agents often either bypass the environment setup machinery for our [module system](../software/modules.md) or fail to include the existence of a module system in their initial context, and thus are unable to find tools with simple `which` or inspection of `$PATH`. They then fall back to looking for executables like `sbatch` by issuing a recursive `find /`. The `find` then descends into all network attached storage, and many agents doing so simultaneously significantly degrades NFS performance and will cause outages.
- Running analysis code on the login nodes. While user resource consumption on the login nodes is capped via `systemd` limits, the login nodes lack sufficient resources for _every_ user to consume the maximum allowed allocation. We have observed agents learning the resource limitations and then specifically tailoring scripts to maximize use of those resources to run processes that should be submitted to the scheduler instead.

## Cluster Skill

To help mitigate these behaviors, we have built the [UCD-HPC Cluster Skill](https://github.com/ucdavis/ucdhpc-cluster-skill), which is a standard [agent skill](https://agentskills.io/home), 
This skill provides guidelines for acceptable behavior on our login nodes, as well as contextual information and scripts for harvesting context; it will save tokens as well as help your agents avoid violating our policies.

**All agentic systems running on _or accessing_ our clusters __must__ use the UCD-HPC Cluster skill.**
This means that if your harness is running on your local machine, but SSHing to our clusters for you, you still must install this skill.
The skill is centrally installed and automatically enabled for __Claude Code__ and __Codex__ users when running the harness on our systems.
For other harnesses, the skill can be installed via the agent skills [npx](https://docs.npmjs.com/cli/v12/commands/npx) tool:

```console
npx skills add ucdavis/ucdhpc-cluster-skill
```


# LangChain Core Components (Graph-Centric Architecture)

This repository explains the **core components of LangChain with a LangGraph-centric mental model**, focusing on how modern **agentic and RAG workflows** are designed, executed, and managed.

LangGraph builds on top of LangChain primitives and introduces **explicit graphs, state management, reducers, and deterministic execution**, which are essential for complex LLM systems.

---

## Table of Contents

- [Architecture Overview](#architecture-overview)
- [Graph](#graph)
- [Nodes](#nodes)
- [Edges](#edges)
- [State](#state)
- [Reducers](#reducers)
- [Workflows](#workflows)
- [Workflow Lifecycle](#workflow-lifecycle)
  - [Graph Definition](#1-graph-definition)
  - [Compilation](#2-compilation)
  - [Invocation](#3-invocation)
  - [Execution (Rounds)](#4-execution-rounds)
- [Mental Model Summary](#mental-model-summary)
- [Key Takeaways](#key-takeaways)

---

## Architecture Overview

A modern LangChain + LangGraph system is composed of the following core concepts:

- **Graph** – the workflow blueprint  
- **Nodes** – computation units  
- **Edges** – control-flow transitions  
- **State** – shared memory  
- **Reducers** – state merge logic  
- **Workflow** – runtime execution model  

Together, these form a **stateful, deterministic execution engine** for LLM applications.

---

## Graph

A **Graph** defines the **control flow** of your LLM application.

- Represents the workflow as a **state machine**
- Determines how execution moves between nodes
- Manages shared state across steps
- Supports branching, looping, retries, and termination

**Mental model:**

> The graph is the *blueprint* of how your system thinks and acts.

---

## Nodes

A **Node** is a single unit of computation.

A node can represent:

- An LLM call
- A retriever
- A tool invocation
- A validator
- A decision function
- Any pure Python logic

### Node Characteristics

- Receives the current **state**
- Performs computation
- Returns **partial state updates**
- Does **not** control execution flow

State → Node Logic → State Updates


---

## Edges

**Edges define how execution moves between nodes.**

They answer the question:

> What runs next?

### Types of Edges

#### Static Edge

Always transitions to the same node.

Node A → Node B


#### Conditional Edge

Chooses the next node based on state values.

Decision Node
├─ condition_1 → Node X
└─ condition_2 → Node Y


Edges enable:

- Branching logic
- Loops
- Retries
- Early termination

---

## State

**State is the single source of truth** in a LangGraph workflow.

- Shared across all nodes
- Typed (via `TypedDict` or Pydantic)
- Updated incrementally over execution rounds

### Example State Fields

- User query
- Retrieved documents
- Intermediate reasoning
- Tool outputs
- Control flags (e.g., `is_complete`)

State persistence enables **multi-hop reasoning and agent behavior**.

---

## Reducers

A **Reducer defines how state updates are merged** across nodes and execution rounds.

Reducers are required because:

- Multiple nodes may update the same state field
- Execution happens iteratively
- Naive overwriting would lose information

### Common Reducer Patterns

| Reducer Type | Behavior |
|-------------|----------|
| Accumulator | Append or merge values |
| Selector | Keep latest or best value |
| Custom | Domain-specific logic |

Reducers make state updates **predictable and composable**.

---

## Workflows

A **Workflow** is the runtime execution of a graph.

It defines:

- How state flows through nodes
- How decisions are made
- When execution should stop

Workflows are **deterministic, debuggable, and reproducible**.

---

## Workflow Lifecycle

LangGraph workflows follow a clear lifecycle:

---

## 1. Graph Definition

At this stage, you define:

- State schema
- Nodes
- Edges
- Reducers
- Entry and exit points

This is a **pure configuration phase** — no execution occurs here.

---

## 2. Compilation

Compilation transforms the defined graph into an executable form.

During compilation:

- Graph structure is validated
- Edges are resolved
- Reducers are finalized
- Execution logic is frozen

**Why compilation matters:**

- Catches errors early
- Ensures deterministic behavior
- Improves runtime reliability

---

## 3. Invocation

Invocation starts a **new execution run**.

- Initial state is provided
- Execution begins at the entry node
- Each invocation is isolated

This allows:

- Parallel runs
- Reproducibility
- Safe retries

---

## 4. Execution (Rounds)

Execution proceeds in **rounds**.

In each round:

1. A node executes
2. It produces state updates
3. Reducers merge updates into global state
4. Edges determine the next node

Execution continues until:

- An end node is reached
- A stopping condition is satisfied

This model naturally supports:

- Iterative reasoning
- Self-correction loops
- Validation cycles
- Multi-agent coordination

---

## Mental Model Summary

| Concept | Mental Model |
|------|-------------|
| Graph | Workflow blueprint |
| Node | Computation step |
| Edge | Transition rule |
| State | Shared memory |
| Reducer | Merge strategy |
| Workflow | Runtime execution |

---

## Key Takeaways

- LangChain provides **primitives**
- LangGraph provides **structure**
- Graph-based workflows make control flow explicit
- State and reducers enable safe iteration
- Execution in rounds enables agentic behavior

> **For modern RAG and agent systems, graph-based design is not optional — it is foundational.**



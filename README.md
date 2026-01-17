# LangGraph Workflows using Open source LLM (llama3.2) (No API needed)

This notebook collection is a **hands-on, example-driven exploration of LangGraph** — focused on building **agentic, multi-step, and controllable LLM workflows** beyond simple prompt chaining.

The notebooks are organized as a **progressive learning path**, starting from basic workflows and moving toward **advanced patterns like human-in-the-loop, tool calling, subgraphs, streaming, and persistence**.

---

## 📂 Repository / Notebook Structure
    ```
    Workflows/
    │
    ├── Connection_sqlite/
    │   └── SQLite connection & persistence experiments
    │
    ├── RAG_as_tool/
    │   └── Using RAG as a callable tool inside LangGraph
    │
    ├── 1_sequential_workflow.ipynb
    ├── 2_simple_workflow_llm.ipynb
    ├── 3_prompt_chaining.ipynb
    ├── 4_parallel_workflow.ipynb
    ├── 5_parallel_workflow_doc_evaluation.ipynb
    ├── 6_conditional_workflow_quadratic.ipynb
    ├── 7_conditional_workflow_custom_edges.ipynb
    ├── 8_iterative_workflow1.ipynb
    ├── 9_chatbot_using_langgraph.ipynb
    ├── 10_persistence_in_langgraph.ipynb
    ├── 11_streaming_in_langgraph.ipynb
    ├── 13_tools_calling.ipynb
    ├── 14_multiple_tool_calling.ipynb
    ├── 16_human_in_the_loop.ipynb
    ├── 17_complex_human_in_the_loop.ipynb
    └── 18_subgraph.ipynb
    ```
---

## 🧩 Notebook Walkthrough

### 🔹 Core Workflow Patterns

| Notebook | Description |
|--------|------------|
| 1_sequential_workflow | Linear, step-by-step execution |
| 2_simple_workflow_llm | Basic LLM-driven graph |
| 3_prompt_chaining | Prompt chaining using graph nodes |
| 4_parallel_workflow | Parallel node execution |
| 5_parallel_workflow_doc_evaluation | Parallel document evaluation |

---

### 🔹 Conditional & Iterative Logic

| Notebook | Description |
|--------|------------|
| 6_conditional_workflow_quadratic | Conditional branching logic |
| 7_conditional_workflow_custom_edges | Custom edge routing |
| 8_iterative_workflow1 | Looping & iterative execution |

---

### 🔹 Conversational & Stateful Systems

| Notebook | Description |
|--------|------------|
| 9_chatbot_using_langgraph | Stateful chatbot |
| 10_persistence_in_langgraph | Checkpointing & persistence |
| 11_streaming_in_langgraph | Streaming responses |

---

### 🔹 Tool Calling & Agentic Behavior

| Notebook / Folder | Description |
|------------------|-------------|
| 13_tools_calling | Single tool invocation |
| 14_multiple_tool_calling | Multi-tool orchestration |
| RAG_as_tool | RAG pipeline as a callable tool |

---

### 🔹 Human-in-the-Loop & Advanced Graphs

| Notebook | Description |
|--------|------------|
| 16_human_in_the_loop | Human feedback during execution |
| 17_complex_human_in_the_loop | Multi-step HITL workflows |
| 18_subgraph | Composing graphs using subgraphs |

---

### 🔹 Persistence & Storage

| Folder | Purpose |
|------|--------|
| Connection_sqlite | SQLite-based persistence |

---

## 🎯 Key Concepts Covered

- LangGraph fundamentals (nodes, edges, state)
- Deterministic workflow orchestration
- Conditional routing & custom edges
- Parallel and iterative execution
- Tool calling & agent-like behavior
- Streaming responses
- Checkpointing & persistence
- Human-in-the-loop systems
- Subgraph composition
- RAG as a callable tool

---

## 🛠️ Tech Stack

- Python
- LangGraph
- LangChain (supporting components)
- OpenAI / LLM APIs
- SQLite
- Jupyter Notebooks

---

## 🚀 How to Use

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies
4. Run notebooks **in order** for best learning experience

---

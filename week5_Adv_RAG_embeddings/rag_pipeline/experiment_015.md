# Experiment 015

## Title
Building an Advanced Local RAG Pipeline

## Objective
Combine chunking, vector storage, retrieval, and generation into one workflow.

## Components
- Document Loader
- Chunk Generator
- Fake Embedding Generator
- Vector Store
- Retriever
- Prompt Builder
- qwen2.5:8b

## Observations
- Retrieval reduces irrelevant context.
- Multiple chunks improve answer quality.
- Separating retrieval from generation creates a modular design.

## Conclusion
RAG systems work by retrieving relevant information before asking the LLM to generate an answer.
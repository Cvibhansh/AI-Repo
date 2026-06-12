# Experiment 014

## Title
Document Chunking for RAG

## Objective
Understand why AI systems split large documents into smaller chunks before retrieval.

## Components
- Knowledge base document
- Chunk generator
- Chunk store
- Chunk retrieval
- Local RAG demo

## Observations
- Large documents are difficult to send directly to an LLM.
- Chunking improves retrieval efficiency.
- Each chunk can have its own embedding.
- Retrieving a few relevant chunks reduces noise.

## Conclusion
Document chunking is a foundational step in building scalable RAG systems.
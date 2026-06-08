# Redrob AI Candidate Ranker

## Overview

This project ranks candidates for an AI Search and Retrieval role using a multi-factor ranking system.

The solution combines candidate skills, recruiter engagement signals, career history, production experience, evidence-based profile analysis, and job-description alignment to identify the strongest candidates from a pool of 100,000 profiles.

## Architecture

Job Description

↓

JD Parser

↓

Feature Extraction

↓

Scoring Modules

* Technical Score
* Signal Score
* Experience Score
* AI Relevance Score
* Career Credibility Score
* Production Experience Score
* Evidence Score
* JD Match Score

↓

Candidate Ranker

↓

Reasoning Generator

↓

Top-100 Submission CSV

## Key Features

### Technical Skill Analysis

Evaluates candidate skills against AI, retrieval, ranking, search, and machine learning requirements.

### Production Experience Detection

Identifies evidence of production deployment, search infrastructure, recommendation systems, ranking systems, retrieval pipelines, and real-world ML systems.

### Evidence-Based Scoring

Rewards candidates with concrete technical accomplishments while reducing the impact of keyword stuffing.

### Job Description Matching

Matches candidate skills and experience against the target role requirements including:

* Retrieval
* Ranking
* Embeddings
* RAG
* LangChain
* LLMs
* A/B Testing

### Reasoning Generation

Generates candidate-specific explanations used in the final submission.

## Reproducing Results

Generate the final submission:

python -m tests.test_submission_generator

Preview submission:

python -m tests.test_submission_preview

## Output

submission.csv

Contains:

candidate_id, rank, score, reasoning

for the Top 100 ranked candidates.


























<!-- # Redrob AI Candidate Ranker

AI-powered candidate discovery and ranking system for the Redrob Data & AI Challenge.

## Objective

Rank the top 100 candidates from a pool of 100,000 candidates for the Senior AI Engineer role.

The ranking system combines:

* Technical Fit Analysis
* Production Engineering Fit
* Behavioral Signal Intelligence
* Potential Index
* Hidden Gem Detection

## Dataset

* 100,000 candidate profiles
* Behavioral signals
* Career history
* Skills
* Certifications
* Education

## Current Status

### Completed

* Repository Setup
* Project Structure

### In Progress

* Dataset Exploration

### Planned

* Feature Extraction
* Scoring Engine
* Ranking Engine
* Submission Generator

## Author

Lalit Kumar




# Dataset

The challenge dataset is intentionally excluded from Git because of its size.

Place the following file in this directory before running the project:

* candidates.jsonl

Dataset source:

Redrob Data & AI Challenge Participant Bundle.




## Next Improvements

- Split AI relevance into:
  - AI Foundation Score
  - LLM/RAG Score
  - Production AI Score

- Add semantic matching between JD and candidate profile

- Add Hidden Gem Detection

- Add Potential Score

- Add explanation generation for recruiters -->
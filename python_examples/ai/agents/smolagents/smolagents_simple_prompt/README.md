# Smolagents Simple Prompt

In this example we are using [smolagents](https://github.com/huggingface/smolagents) with a fixed prompt that should trigger it to use the web search tool.

## Environment Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| OPENAI_BASE_URL | The base URL for the OpenAI compatible API | https://api.openai.com/v1 |
| OPENAI_API_KEY | The API key for the above API | |
| OPENAI_MODEL_ID | The model to use | gpt-4o-mini |
| OPENAI_FLATTEN_MESSAGES | Whether the API expects message content to be str rather than object | false |

## Run

```console
$ uv run -m python_examples.ai.agents.smolagents.smolagents_simple_prompt.agent
╭───────────────────────────────── New run ──────────────────────────────────╮
│                                                                            │
│ What was the population of the UK in 2023?                                 │
│                                                                            │
╰─ OpenAIServerModel - mistralai/mistral-small-3.2-24b-instruct:free ────────╯
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Step 1 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INFO:httpx:HTTP Request: POST https://openrouter.ai/api/v1/chat/completions "HTTP/1.1 200 OK"
╭────────────────────────────────────────────────────────────────────────────╮
│ Calling tool: 'web_search' with arguments: {'query': 'What was the         │
│ population of the UK in 2023?'}                                            │
╰────────────────────────────────────────────────────────────────────────────╯
INFO:primp:response: https://lite.duckduckgo.com/lite/ 200
Observations: ## Search Results

|Population estimates for the UK, England, Wales, Scotland and Northern
...](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigratio
n/populationestimates/bulletins/annualmidyearpopulationestimates/mid2023)
The UK population at mid-year 2023 was estimated to be 68.3 million, an
increase of 1.0% since mid-2022...

...

[Step 1: Duration 3.65 seconds| Input tokens: 1,060 | Output tokens: 32]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Step 2 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INFO:httpx:HTTP Request: POST https://openrouter.ai/api/v1/chat/completions "HTTP/1.1 200 OK"
╭────────────────────────────────────────────────────────────────────────────╮
│ Calling tool: 'final_answer' with arguments: {'answer': 'the population of │
│ the UK in 2023 was of 68.3 million inhabitants.'}                          │
╰────────────────────────────────────────────────────────────────────────────╯
Final answer: the population of the UK in 2023 was of 68.3 million
inhabitants.
[Step 2: Duration 3.02 seconds| Input tokens: 3,389 | Output tokens: 71]
```

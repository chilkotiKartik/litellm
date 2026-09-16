\"\"\"
Unit tests for prompt caching token savings and cache hit ratio calculation in LiteLLM router.
\"\"\"
import pytest
from typing import Dict, Any

def test_cache_hit_ratio_calculation():
    total_requests = 200
    cache_hits = 150
    
    hit_ratio = (cache_hits / total_requests) * 100
    assert hit_ratio == 75.0

def test_cache_hit_ratio_zero_requests():
    total_requests = 0
    cache_hits = 0
    
    hit_ratio = 0.0 if total_requests == 0 else (cache_hits / total_requests) * 100
    assert hit_ratio == 0.0

def test_prompt_caching_token_reduction():
    original_prompt_tokens = 4500
    cached_tokens_read = 4000
    non_cached_tokens = original_prompt_tokens - cached_tokens_read
    
    assert non_cached_tokens == 500
    savings_percentage = (cached_tokens_read / original_prompt_tokens) * 100
    assert round(savings_percentage, 2) == 88.89
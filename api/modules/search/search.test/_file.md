# modules/search/search.test

- **Source:** [local](../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · 2180 lines
- **Module/theme:** search

## File documentation

```text
@file
Tests for search.module.
```

## Classes and interfaces (derived index)

- [SearchMatchTestCase](SearchMatchTestCase.md) — Indexes content and queries it.
- [SearchPageText](SearchPageText.md) — Tests the bike shed text on no results page, and text on the search page.
- [SearchAdvancedSearchForm](SearchAdvancedSearchForm.md) — Indexes content and tests the advanced search form.
- [SearchRankingTestCase](SearchRankingTestCase.md) — Indexes content and tests ranking factors.
- [SearchBlockTestCase](SearchBlockTestCase.md) — Tests the rendering of the search block.
- [SearchExactTestCase](SearchExactTestCase.md) — Tests that searching for a phrase gets the correct page count.
- [SearchCommentTestCase](SearchCommentTestCase.md) — Test integration searching comments.
- [SearchExpressionInsertExtractTestCase](SearchExpressionInsertExtractTestCase.md) — Tests search_expression_insert() and search_expression_extract().
- [SearchCommentCountToggleTestCase](SearchCommentCountToggleTestCase.md) — Tests that comment count display toggles properly on comment status of node
- [SearchSimplifyTestCase](SearchSimplifyTestCase.md) — Test search_simplify() on every Unicode character, and some other cases.
- [SearchKeywordsConditions](SearchKeywordsConditions.md) — Tests keywords and conditions.
- [SearchNumbersTestCase](SearchNumbersTestCase.md) — Tests that numbers can be searched.
- [SearchNumberMatchingTestCase](SearchNumberMatchingTestCase.md) — Tests that numbers can be searched, with more complex matching.
- [SearchConfigSettingsForm](SearchConfigSettingsForm.md) — Test config page.
- [SearchExcerptTestCase](SearchExcerptTestCase.md) — Tests the search_excerpt() function.
- [SearchTokenizerTestCase](SearchTokenizerTestCase.md) — Test the CJK tokenizer.
- [SearchEmbedForm](SearchEmbedForm.md) — Tests that we can embed a form in search results and submit it.
- [SearchPageOverride](SearchPageOverride.md) — Tests that hook_search_page runs.
- [SearchLanguageTestCase](SearchLanguageTestCase.md) — Test node search with multiple languages.
- [SearchNodeAccessTest](SearchNodeAccessTest.md) — Tests node search with node access control.
- [SearchNodeTagTest](SearchNodeTagTest.md) — Tests node search with query tags.
- [SearchSetLocaleTest](SearchSetLocaleTest.md) — Tests searching with locale values set.

## Constants

### SEARCH_TYPE

- Line 10

```php
define('SEARCH_TYPE', '_test_');
```

### SEARCH_TYPE_2

- Line 11

```php
define('SEARCH_TYPE_2', '_test2_');
```

### SEARCH_TYPE_JPN

- Line 12

```php
define('SEARCH_TYPE_JPN', '_test3_');
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._

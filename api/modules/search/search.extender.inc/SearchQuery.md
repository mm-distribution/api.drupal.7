# SearchQuery

- **Type:** Class
- **File:** [`modules/search/search.extender.inc`](_file.md), lines 27–546 · [local source](../../../../source/modules/search/search.extender.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.extender.inc#L27-L546)
- **Module/theme:** search

## Signature

```php
class SearchQuery extends SelectQueryExtender
```

## Documentation

```text
Do a query on the full-text search index for a word or words.

This function is normally only called by each module that supports the
indexed search (and thus, implements hook_update_index()).

Results are retrieved in two logical passes. However, the two passes are
joined together into a single query. And in the case of most simple
queries the second pass is not even used.

The first pass selects a set of all possible matches, which has the benefit
of also providing the exact result set for simple "AND" or "OR" searches.

The second portion of the query further refines this set by verifying
advanced text conditions (such as negative or phrase matches).

The used query object has the tag 'search_$module' and can be further
extended with hook_query_alter().
```

## Properties

### $searchExpression

```php
protected $searchExpression;
```

```text
The search query that is used for searching.

@var string
```

### $type

```php
protected $type;
```

```text
Type of search (search module).

This maps to the value of the type column in search_index, and is equal
to the machine-readable name of the module that implements
hook_search_info().

@var string
```

### $keys

```php
protected $keys = array('positive' => array(), 'negative' => array());
```

```text
Positive and negative search keys.

@var array
```

### $simple

```php
protected $simple = TRUE;
```

```text
Indicates whether the first pass query requires complex conditions (LIKE).

@var boolean.
```

### $conditions

```php
protected $conditions;
```

```text
Conditions that are used for exact searches.

This is always used for the second pass query but not for the first pass,
unless $this->simple is FALSE.

@var DatabaseCondition
```

### $matches

```php
protected $matches = 0;
```

```text
Indicates how many matches for a search query are necessary.

@var int
```

### $words

```php
protected $words = array();
```

```text
Array of search words.

These words have to match against {search_index}.word.

@var array
```

### $normalize

```php
protected $normalize;
```

```text
Multiplier for the normalized search score.

This value is calculated by the first pass query and multiplied with the
actual score of a specific word to make sure that the resulting calculated
score is between 0 and 1.

@var float
```

### $executedFirstPass

```php
protected $executedFirstPass = FALSE;
```

```text
Indicates whether the first pass query has been executed.

@var boolean
```

### $scores

```php
protected $scores = array();
```

```text
Stores score expressions.

@var array

@see addScore()
```

### $scoresArguments

```php
protected $scoresArguments = array();
```

```text
Stores arguments for score expressions.

@var array
```

### $multiply

```php
protected $multiply = array();
```

```text
Stores multipliers for score expressions.

@var array
```

### $expressionsIgnored

```php
protected $expressionsIgnored = FALSE;
```

```text
Whether or not search expressions were ignored.

The maximum number of AND/OR combinations exceeded can be configured to
avoid Denial-of-Service attacks. Expressions beyond the limit are ignored.

@var boolean
```

## Methods (derived index)

- [searchExpression()](SearchQuery/searchExpression.md) — Sets up the search query expression.
- [setOption()](SearchQuery/setOption.md) — Applies a search option and removes it from the search query string.
- [parseSearchExpression()](SearchQuery/parseSearchExpression.md) — Parses the search query into SQL conditions.
- [parseWord()](SearchQuery/parseWord.md) — Helper function for parseQuery().
- [executeFirstPass()](SearchQuery/executeFirstPass.md) — Executes the first pass query.
- [addScore()](SearchQuery/addScore.md) — Adds a custom score expression to the search query.
- [execute()](SearchQuery/execute.md) — Executes the search.
- [countQuery()](SearchQuery/countQuery.md) — Builds the default count query for SearchQuery.

---
_Drupal 7.103 · [modules/search/search.extender.inc](https://github.com/drupal/drupal/blob/7.103/modules/search/search.extender.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

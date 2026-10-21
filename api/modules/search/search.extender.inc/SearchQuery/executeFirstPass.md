# SearchQuery::executeFirstPass()

- **Type:** Method
- **File:** [`modules/search/search.extender.inc`](../_file.md), lines 354–402 · [local source](../../../../../source/modules/search/search.extender.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.extender.inc#L354-L402)
- **Class:** [SearchQuery](../SearchQuery.md)
- **Module/theme:** search

## Signature

```php
public function executeFirstPass()
```

## Documentation

```text
Executes the first pass query.

This can either be done explicitly, so that additional scores and
conditions can be applied to the second pass query, or implicitly by
addScore() or execute().

@return
  TRUE if search items exist, FALSE if not.
```

## Code

```php
  public function executeFirstPass() {
    $this->parseSearchExpression();

    if (count($this->words) == 0) {
      form_set_error('keys', format_plural(variable_get('minimum_word_size', 3), 'You must include at least one positive keyword with 1 character or more.', 'You must include at least one positive keyword with @count characters or more.'));
      return FALSE;
    }
    if ($this->expressionsIgnored) {
      drupal_set_message(t('Your search used too many AND/OR expressions. Only the first @count terms were included in this search.', array('@count' => variable_get('search_and_or_limit', 7))), 'warning');
    }
    $this->executedFirstPass = TRUE;

    if (!empty($this->words)) {
      $or = db_or();
      foreach ($this->words as $word) {
        $or->condition('i.word', $word);
      }
      $this->condition($or);
    }
    // Build query for keyword normalization.
    $this->join('search_total', 't', 'i.word = t.word');
    $this
      ->condition('i.type', $this->type)
      ->groupBy('i.type')
      ->groupBy('i.sid')
      ->having('COUNT(*) >= :matches', array(':matches' => $this->matches));

    // Clone the query object to do the firstPass query;
    $first = clone $this->query;

    // For complex search queries, add the LIKE conditions to the first pass query.
    if (!$this->simple) {
      $first->join('search_dataset', 'd', 'i.sid = d.sid AND i.type = d.type');
      $first->condition($this->conditions);
    }

    // Calculate maximum keyword relevance, to normalize it.
    $first->addExpression('SUM(i.score * t.count)', 'calculated_score');
    $this->normalize = $first
      ->range(0, 1)
      ->orderBy('calculated_score', 'DESC')
      ->execute()
      ->fetchField();

    if ($this->normalize) {
      return TRUE;
    }
    return FALSE;
  }
```

---
_Drupal 7.103 · [modules/search/search.extender.inc](https://github.com/drupal/drupal/blob/7.103/modules/search/search.extender.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

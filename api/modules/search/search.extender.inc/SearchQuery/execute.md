# SearchQuery::execute()

- **Type:** Method
- **File:** [`modules/search/search.extender.inc`](../_file.md), lines 461–514 · [local source](../../../../../source/modules/search/search.extender.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.extender.inc#L461-L514)
- **Class:** [SearchQuery](../SearchQuery.md)
- **Module/theme:** search

## Signature

```php
public function execute()
```

## Documentation

```text
Executes the search.

If not already done, this executes the first pass query. Then the complex
conditions are applied to the query including score expressions and
ordering.

@return
  FALSE if the first pass query returned no results, and a database result
  set if there were results.
```

## Code

```php
  public function execute()
  {
    if (!$this->executedFirstPass) {
      $this->executeFirstPass();
    }
    if (!$this->normalize) {
      return new DatabaseStatementEmpty();
    }

    // Add conditions to query.
    $this->join('search_dataset', 'd', 'i.sid = d.sid AND i.type = d.type');
    $this->condition($this->conditions);

    if (empty($this->scores)) {
      // Add default score.
      $this->addScore('i.relevance');
    }

    if (count($this->multiply)) {
      // Re-normalize scores with multipliers by dividing by the total of all
      // multipliers. The expressions were altered in addScore(), so here just
      // add the arguments for the total.
      $i = 0;
      $sum = array_sum($this->multiply);
      foreach ($this->multiply as $total) {
        $this->scoresArguments[':total_' . $i] = $sum;
        $i++;
      }
    }

    // Replace the pseudo-expression 'i.relevance' with a measure of keyword
    // relevance in all score expressions, using string replacement. Careful
    // though! If you just print out a float, some locales use ',' as the
    // decimal separator in PHP, while SQL always uses '.'. So, make sure to
    // set the number format correctly.
    $relevance = number_format((1.0 / $this->normalize), 10, '.', '');
    $this->scores = str_replace('i.relevance', '(' . $relevance . ' * i.score * t.count)', $this->scores);

    // Add all scores together to form a query field.
    $this->addExpression('SUM(' . implode(' + ', $this->scores) . ')', 'calculated_score', $this->scoresArguments);

    // If an order has not yet been set for this query, add a default order
    // that sorts by the calculated sum of scores.
    if (count($this->getOrderBy()) == 0) {
      $this->orderBy('calculated_score', 'DESC');
    }

    // Add useful metadata.
    $this
      ->addMetaData('normalize', $this->normalize)
      ->fields('i', array('type', 'sid'));

    return $this->query->execute();
  }
```

---
_Drupal 7.103 · [modules/search/search.extender.inc](https://github.com/drupal/drupal/blob/7.103/modules/search/search.extender.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

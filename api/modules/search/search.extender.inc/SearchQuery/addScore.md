# SearchQuery::addScore()

- **Type:** Method
- **File:** [`modules/search/search.extender.inc`](../_file.md), lines 431–448 · [local source](../../../../../source/modules/search/search.extender.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.extender.inc#L431-L448)
- **Class:** [SearchQuery](../SearchQuery.md)
- **Module/theme:** search

## Signature

```php
public function addScore($score, $arguments = array(), $multiply = FALSE)
```

## Documentation

```text
Adds a custom score expression to the search query.

Score expressions are used to order search results. If no calls to
addScore() have taken place, a default keyword relevance score will be
used. However, if at least one call to addScore() has taken place, the
keyword relevance score is not automatically added.

Note that you must use this method to add ordering to your searches, and
not call orderBy() directly, when using the SearchQuery extender. This is
because of the two-pass system the SearchQuery class uses to normalize
scores.

@param $score
  The score expression, which should evaluate to a number between 0 and 1.
  The string 'i.relevance' in a score expression will be replaced by a
  measure of keyword relevance between 0 and 1.
@param $arguments
  Query arguments needed to provide values to the score expression.
@param $multiply
  If set, the score is multiplied with this value. However, all scores
  with multipliers are then divided by the total of all multipliers, so
  that overall, the normalization is maintained.

@return object
  The updated query object.
```

## Code

```php
  public function addScore($score, $arguments = array(), $multiply = FALSE) {
    if ($multiply) {
      $i = count($this->multiply);
      // Modify the score expression so it is multiplied by the multiplier,
      // with a divisor to renormalize.
      $score = "CAST(:multiply_$i AS DECIMAL) * COALESCE(( " . $score . "), 0) / CAST(:total_$i AS DECIMAL)";
      // Add an argument for the multiplier. The :total_$i argument is taken
      // care of in the execute() method, which is when the total divisor is
      // calculated.
      $arguments[':multiply_' . $i] = $multiply;
      $this->multiply[] = $multiply;
    }

    $this->scores[] = $score;
    $this->scoresArguments += $arguments;

    return $this;
  }
```

---
_Drupal 7.103 · [modules/search/search.extender.inc](https://github.com/drupal/drupal/blob/7.103/modules/search/search.extender.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

# InsertQuery::values()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 557–570 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L557-L570)
- **Class:** [InsertQuery](../InsertQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function values(array $values)
```

## Documentation

```text
Adds another set of values to the query to be inserted.

If $values is a numeric-keyed array, it will be assumed to be in the same
order as the original fields() call. If it is associative, it may be
in any order as long as the keys of the array match the names of the
fields.

@param $values
  An array of values to add to the query.

@return InsertQuery
  The called object.
```

## Code

```php
  public function values(array $values) {
    if (is_numeric(key($values))) {
      $this->insertValues[] = $values;
    }
    else {
      // Reorder the submitted values to match the fields array.
      foreach ($this->insertFields as $key) {
        $insert_values[$key] = $values[$key];
      }
      // For consistency, the values array is always numerically indexed.
      $this->insertValues[] = array_values($insert_values);
    }
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

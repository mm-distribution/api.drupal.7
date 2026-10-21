# QueryConditionInterface::where()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 60–60 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L60)
- **Class:** [QueryConditionInterface](../QueryConditionInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function where($snippet, $args = array());
```

## Documentation

```text
Adds an arbitrary WHERE clause to the query.

@param $snippet
  A portion of a WHERE clause as a prepared statement. It must use named
  placeholders, not ? placeholders.
@param $args
  An associative array of arguments.

@return QueryConditionInterface
  The called object.
```

## Code

```php
  public function where($snippet, $args = array());
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

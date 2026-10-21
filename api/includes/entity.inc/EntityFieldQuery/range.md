# EntityFieldQuery::range()

- **Type:** Method
- **File:** [`includes/entity.inc`](../_file.md), lines 1026–1032 · [local source](../../../../source/includes/entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc#L1026-L1032)
- **Class:** [EntityFieldQuery](../EntityFieldQuery.md)

## Signature

```php
public function range($start = NULL, $length = NULL)
```

## Documentation

```text
Restricts a query to a given range in the result set.

@param $start
  The first entity from the result set to return. If NULL, removes any
  range directives that are set.
@param $length
  The number of entities to return from the result set.

@return EntityFieldQuery
  The called object.
```

## Code

```php
  public function range($start = NULL, $length = NULL) {
    $this->range = array(
      'start' => $start,
      'length' => $length,
    );
    return $this;
  }
```

---
_Drupal 7.103 · [includes/entity.inc](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

# QueryAlterableInterface::hasAnyTag()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 218–218 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L218)
- **Class:** [QueryAlterableInterface](../QueryAlterableInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function hasAnyTag();
```

## Documentation

```text
Determines if a given query has any specified tag.

@param $tags
  A variable number of arguments, one for each tag to check.

@return
  TRUE if this query has been marked with at least one of the specified
  tags, FALSE otherwise.
```

## Code

```php
  public function hasAnyTag();
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

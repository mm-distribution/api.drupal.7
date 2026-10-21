# QueryAlterableInterface::hasAllTags()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 206–206 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L206)
- **Class:** [QueryAlterableInterface](../QueryAlterableInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function hasAllTags();
```

## Documentation

```text
Determines if a given query has all specified tags.

@param $tags
  A variable number of arguments, one for each tag to check.

@return
  TRUE if this query has been marked with all specified tags, FALSE
  otherwise.
```

## Code

```php
  public function hasAllTags();
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

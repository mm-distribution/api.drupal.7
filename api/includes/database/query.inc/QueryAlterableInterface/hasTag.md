# QueryAlterableInterface::hasTag()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 194–194 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L194)
- **Class:** [QueryAlterableInterface](../QueryAlterableInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function hasTag($tag);
```

## Documentation

```text
Determines if a given query has a given tag.

@param $tag
  The tag to check.

@return
  TRUE if this query has been marked with this tag, FALSE otherwise.
```

## Code

```php
  public function hasTag($tag);
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

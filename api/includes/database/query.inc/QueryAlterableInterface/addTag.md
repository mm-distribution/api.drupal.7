# QueryAlterableInterface::addTag()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 183–183 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L183)
- **Class:** [QueryAlterableInterface](../QueryAlterableInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function addTag($tag);
```

## Documentation

```text
Adds a tag to a query.

Tags are strings that identify a query. A query may have any number of
tags. Tags are used to mark a query so that alter hooks may decide if they
wish to take action. Tags should be all lower-case and contain only
letters, numbers, and underscore, and start with a letter. That is, they
should follow the same rules as PHP identifiers in general.

@param $tag
  The tag to add.

@return QueryAlterableInterface
  The called object.
```

## Code

```php
  public function addTag($tag);
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

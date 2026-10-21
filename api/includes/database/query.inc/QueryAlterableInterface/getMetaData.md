# QueryAlterableInterface::getMetaData()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 247–247 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L247)
- **Class:** [QueryAlterableInterface](../QueryAlterableInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function getMetaData($key);
```

## Documentation

```text
Retrieves a given piece of metadata.

@param $key
  The unique identifier for the piece of metadata to retrieve.

@return
  The previously attached metadata object, or NULL if one doesn't exist.
```

## Code

```php
  public function getMetaData($key);
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

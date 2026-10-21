# QueryAlterableInterface::addMetaData()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 236–236 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L236)
- **Class:** [QueryAlterableInterface](../QueryAlterableInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function addMetaData($key, $object);
```

## Documentation

```text
Adds additional metadata to the query.

Often, a query may need to provide additional contextual data to alter
hooks. Alter hooks may then use that information to decide if and how
to take action.

@param $key
  The unique identifier for this piece of metadata. Must be a string that
  follows the same rules as any other PHP identifier.
@param $object
  The additional data to add to the query. May be any valid PHP variable.

@return QueryAlterableInterface
  The called object.
```

## Code

```php
  public function addMetaData($key, $object);
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

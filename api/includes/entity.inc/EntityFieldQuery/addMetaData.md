# EntityFieldQuery::addMetaData()

- **Type:** Method
- **File:** [`includes/entity.inc`](../_file.md), lines 1174–1177 · [local source](../../../../source/includes/entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc#L1174-L1177)
- **Class:** [EntityFieldQuery](../EntityFieldQuery.md)

## Signature

```php
public function addMetaData($key, $object)
```

## Documentation

```text
Adds additional metadata to the query.

Sometimes a query may need to provide additional contextual data for the
alter hook. The alter hook implementations may then use that information
to decide if and how to take action.

@param $key
  The unique identifier for this piece of metadata. Must be a string that
  follows the same rules as any other PHP identifier.
@param $object
  The additional data to add to the query. May be any valid PHP variable.

@return EntityFieldQuery
  The called object.
```

## Code

```php
  public function addMetaData($key, $object) {
    $this->metaData[$key] = $object;
    return $this;
  }
```

---
_Drupal 7.103 · [includes/entity.inc](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

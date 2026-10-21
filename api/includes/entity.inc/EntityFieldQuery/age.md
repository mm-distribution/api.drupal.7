# EntityFieldQuery::age()

- **Type:** Method
- **File:** [`includes/entity.inc`](../_file.md), lines 1128–1131 · [local source](../../../../source/includes/entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc#L1128-L1131)
- **Class:** [EntityFieldQuery](../EntityFieldQuery.md)

## Signature

```php
public function age($age)
```

## Documentation

```text
Queries the current or every revision.

Note that this only affects field conditions. Property conditions always
apply to the current revision.
@TODO: Once revision tables have been cleaned up, revisit this.

@param $age
  - FIELD_LOAD_CURRENT (default): Query the most recent revisions for all
    entities. The results will be keyed by entity type and entity ID.
  - FIELD_LOAD_REVISION: Query all revisions. The results will be keyed by
    entity type and entity revision ID.

@return EntityFieldQuery
  The called object.
```

## Code

```php
  public function age($age) {
    $this->age = $age;
    return $this;
  }
```

---
_Drupal 7.103 · [includes/entity.inc](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

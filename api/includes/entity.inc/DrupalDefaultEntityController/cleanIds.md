# DrupalDefaultEntityController::cleanIds()

- **Type:** Method
- **File:** [`includes/entity.inc`](../_file.md), lines 242–251 · [local source](../../../../source/includes/entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc#L242-L251)
- **Class:** [DrupalDefaultEntityController](../DrupalDefaultEntityController.md)

## Signature

```php
protected function cleanIds(&$ids)
```

## Documentation

```text
Ensures integer entity IDs are valid.

The identifier sanitization provided by this method has been introduced
as Drupal used to rely on the database to facilitate this, which worked
correctly with MySQL but led to errors with other DBMS such as PostgreSQL.

@param array $ids
  The entity IDs to verify. Non-integer IDs are removed from this array if
  the entity type requires IDs to be integers.
```

## Code

```php
  protected function cleanIds(&$ids) {
    $entity_info = entity_get_info($this->entityType);
    if (isset($entity_info['base table field types'])) {
      $id_type = $entity_info['base table field types'][$this->idKey];
      if ($id_type == 'serial' || $id_type == 'int') {
        $ids = array_filter($ids, array($this, 'filterId'));
        $ids = array_map('intval', $ids);
      }
    }
  }
```

---
_Drupal 7.103 · [includes/entity.inc](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

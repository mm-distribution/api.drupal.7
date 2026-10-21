# DrupalDefaultEntityController::cacheGet()

- **Type:** Method
- **File:** [`includes/entity.inc`](../_file.md), lines 386–425 · [local source](../../../../source/includes/entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc#L386-L425)
- **Class:** [DrupalDefaultEntityController](../DrupalDefaultEntityController.md)

## Signature

```php
protected function cacheGet($ids, $conditions = array())
```

## Documentation

```text
Gets entities from the static cache.

@param $ids
  If not empty, return entities that match these IDs.
@param $conditions
  If set, return entities that match all of these conditions.

@return
  Array of entities from the entity cache.
```

## Code

```php
  protected function cacheGet($ids, $conditions = array()) {
    $entities = array();
    // Load any available entities from the internal cache.
    if (!empty($this->entityCache)) {
      if ($ids) {
        $entities += array_intersect_key($this->entityCache, array_flip($ids));
      }
      // If loading entities only by conditions, fetch all available entities
      // from the cache. Entities which don't match are removed later.
      elseif ($conditions) {
        $entities = $this->entityCache;
      }
    }

    // Exclude any entities loaded from cache if they don't match $conditions.
    // This ensures the same behavior whether loading from memory or database.
    if ($conditions) {
      foreach ($entities as $entity) {
        // Iterate over all conditions and compare them to the entity
        // properties. We cannot use array_diff_assoc() here since the
        // conditions can be nested arrays, too.
        foreach ($conditions as $property_name => $condition) {
          if (is_array($condition)) {
            // Multiple condition values for one property are treated as OR
            // operation: only if the value is not at all in the condition array
            // we remove the entity.
            if (!in_array($entity->{$property_name}, $condition)) {
              unset($entities[$entity->{$this->idKey}]);
              continue 2;
            }
          }
          elseif ($condition != $entity->{$property_name}) {
            unset($entities[$entity->{$this->idKey}]);
            continue 2;
          }
        }
      }
    }
    return $entities;
  }
```

---
_Drupal 7.103 · [includes/entity.inc](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

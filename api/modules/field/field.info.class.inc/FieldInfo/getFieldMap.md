# FieldInfo::getFieldMap()

- **Type:** Method
- **File:** [`modules/field/field.info.class.inc`](../_file.md), lines 123–155 · [local source](../../../../../source/modules/field/field.info.class.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.class.inc#L123-L155)
- **Class:** [FieldInfo](../FieldInfo.md)
- **Module/theme:** field

## Signature

```php
public function getFieldMap()
```

## Documentation

```text
Collects a lightweight map of fields across bundles.

@return
  An array keyed by field name. Each value is an array with two entries:
  - type: The field type.
  - bundles: The bundles in which the field appears, as an array with
    entity types as keys and the array of bundle names as values.
```

## Code

```php
  public function getFieldMap() {
    // Read from the "static" cache.
    if ($this->fieldMap !== NULL) {
      return $this->fieldMap;
    }

    // Read from persistent cache.
    if ($cached = cache_get('field_info:field_map', 'cache_field')) {
      $map = $cached->data;

      // Save in "static" cache.
      $this->fieldMap = $map;

      return $map;
    }

    $map = array();

    $query = db_query('SELECT fc.type, fci.field_name, fci.entity_type, fci.bundle FROM {field_config_instance} fci INNER JOIN {field_config} fc ON fc.id = fci.field_id WHERE fc.active = 1 AND fc.storage_active = 1 AND fc.deleted = 0 AND fci.deleted = 0 ORDER BY bundle, entity_type');
    foreach ($query as $row) {
      $map[$row->field_name]['bundles'][$row->entity_type][] = $row->bundle;
      $map[$row->field_name]['type'] = $row->type;
    }

    // Save in "static" and persistent caches.
    $this->fieldMap = $map;
    if (lock_acquire('field_info:field_map')) {
      cache_set('field_info:field_map', $map, 'cache_field');
      lock_release('field_info:field_map');
    }

    return $map;
  }
```

---
_Drupal 7.103 · [modules/field/field.info.class.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.class.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

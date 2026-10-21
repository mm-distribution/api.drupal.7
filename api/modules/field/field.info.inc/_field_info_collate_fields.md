# _field_info_collate_fields()

- **Type:** Function
- **File:** [`modules/field/field.info.inc`](_file.md), lines 76–107 · [local source](../../../../source/modules/field/field.info.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc#L76-L107)
- **Module/theme:** field
- **Topics:** [field_info](../../../topics/field_info.md)

## Signature

```php
function _field_info_collate_fields($reset = FALSE)
```

## Documentation

```text
Collates all information on existing fields and instances.

Deprecated. This function is kept to ensure backwards compatibility, but has
a serious performance impact, and should be absolutely avoided.
See http://drupal.org/node/1915646.

Use the regular field_info_*() API functions to access the information, or
field_info_cache_clear() to clear the cached data.
```

## Code

```php
function _field_info_collate_fields($reset = FALSE) {
  if ($reset) {
    _field_info_field_cache()->flush();
    return;
  }

  $cache = _field_info_field_cache();

  // Collect fields, and build the array of IDs keyed by field_name.
  $fields = $cache->getFields();
  $field_ids = array();
  foreach ($fields as $id => $field) {
    if (!$field['deleted']) {
      $field_ids[$field['field_name']] = $id;
    }
  }

  // Collect extra fields for all entity types.
  $extra_fields = array();
  foreach (field_info_bundles() as $entity_type => $bundles) {
    foreach ($bundles as $bundle => $info) {
      $extra_fields[$entity_type][$bundle] = $cache->getBundleExtraFields($entity_type, $bundle);
    }
  }

  return array(
    'fields' => $fields,
    'field_ids' => $field_ids,
    'instances' => $cache->getInstances(),
    'extra_fields' => $extra_fields,
  );
}
```

---
_Drupal 7.103 · [modules/field/field.info.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

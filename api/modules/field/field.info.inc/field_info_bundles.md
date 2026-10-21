# field_info_bundles()

- **Type:** Function
- **File:** [`modules/field/field.info.inc`](_file.md), lines 432–444 · [local source](../../../../source/modules/field/field.info.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc#L432-L444)
- **Module/theme:** field
- **Topics:** [field_info](../../../topics/field_info.md)

## Signature

```php
function field_info_bundles($entity_type = NULL)
```

## Documentation

```text
Returns information about existing bundles.

@param $entity_type
  The type of entity; e.g. 'node' or 'user'.

@return
  An array of bundles for the $entity_type keyed by bundle name,
  or, if no $entity_type was provided, the array of all existing bundles,
  keyed by entity type.
```

## Code

```php
function field_info_bundles($entity_type = NULL) {
  $info = entity_get_info();

  if ($entity_type) {
    return isset($info[$entity_type]['bundles']) ? $info[$entity_type]['bundles'] : array();
  }

  $bundles = array();
  foreach ($info as $type => $entity_info) {
    $bundles[$type] = $entity_info['bundles'];
  }
  return $bundles;
}
```

---
_Drupal 7.103 · [modules/field/field.info.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

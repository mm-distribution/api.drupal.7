# field_info_storage_types()

- **Type:** Function
- **File:** [`modules/field/field.info.inc`](_file.md), lines 408–419 · [local source](../../../../source/modules/field/field.info.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc#L408-L419)
- **Module/theme:** field
- **Topics:** [field_info](../../../topics/field_info.md)

## Signature

```php
function field_info_storage_types($storage_type = NULL)
```

## Documentation

```text
Returns information about field storage from hook_field_storage_info().

@param $storage_type
  (optional) A storage type name. If omitted, all storage types will be
  returned.

@return
  Either a storage type description, as provided by
  hook_field_storage_info(), or an array of all existing storage types,
  keyed by storage type name.
```

## Code

```php
function field_info_storage_types($storage_type = NULL) {
  $info = _field_info_collate_types();
  $storage_types = $info['storage types'];
  if ($storage_type) {
    if (isset($storage_types[$storage_type])) {
      return $storage_types[$storage_type];
    }
  }
  else {
    return $storage_types;
  }
}
```

---
_Drupal 7.103 · [modules/field/field.info.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

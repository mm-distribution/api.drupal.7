# field_info_fields()

- **Type:** Function
- **File:** [`modules/field/field.info.inc`](_file.md), lines 491–503 · [local source](../../../../source/modules/field/field.info.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc#L491-L503)
- **Module/theme:** field
- **Topics:** [field_info](../../../topics/field_info.md)

## Signature

```php
function field_info_fields()
```

## Documentation

```text
Returns all field definitions.

Use of this function should be avoided when possible, since it loads and
statically caches a potentially large array of information. Use
field_info_field_map() instead.

When iterating over the fields present in a given bundle after a call to
field_info_instances($entity_type, $bundle), it is recommended to use
field_info_field() on each individual field instead.

@return
  An array of field definitions, keyed by field name. Each field has an
  additional property, 'bundles', which is an array of all the bundles to
  which this field belongs keyed by entity type.

@see field_info_field_map()
```

## Code

```php
function field_info_fields() {
  $cache = _field_info_field_cache();
  $info = $cache->getFields();

  $fields = array();
  foreach ($info as $key => $field) {
    if (!$field['deleted']) {
      $fields[$field['field_name']] = $field;
    }
  }

  return $fields;
}
```

---
_Drupal 7.103 · [modules/field/field.info.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

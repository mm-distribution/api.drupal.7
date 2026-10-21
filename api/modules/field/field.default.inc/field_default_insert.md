# field_default_insert()

- **Type:** Function
- **File:** [`modules/field/field.default.inc`](_file.md), lines 103–114 · [local source](../../../../source/modules/field/field.default.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.default.inc#L103-L114)
- **Module/theme:** field

## Signature

```php
function field_default_insert($entity_type, $entity, $field, $instance, $langcode, &$items)
```

## Documentation

```text
Default field 'insert' operation.

Insert default value if no $entity->$field_name entry was provided.
This can happen with programmatic saves, or on form-based creation where
the current user doesn't have 'edit' permission for the field.
```

## Code

```php
function field_default_insert($entity_type, $entity, $field, $instance, $langcode, &$items) {
  // _field_invoke() populates $items with an empty array if the $entity has no
  // entry for the field, so we check on the $entity itself.
  // We also check that the current field translation is actually defined before
  // assigning it a default value. This way we ensure that only the intended
  // languages get a default value. Otherwise we could have default values for
  // not yet open languages.
  if (empty($entity) || !property_exists($entity, $field['field_name']) ||
    (isset($entity->{$field['field_name']}[$langcode]) && count($entity->{$field['field_name']}[$langcode]) == 0)) {
    $items = field_get_default_value($entity_type, $entity, $field, $instance, $langcode);
  }
}
```

---
_Drupal 7.103 · [modules/field/field.default.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.default.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

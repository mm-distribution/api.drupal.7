# field_get_items()

- **Type:** Function
- **File:** [`modules/field/field.module`](_file.md), lines 940–943 · [local source](../../../../source/modules/field/field.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module#L940-L943)
- **Module/theme:** field
- **Topics:** [field](../../../topics/field.md)

## Signature

```php
function field_get_items($entity_type, $entity, $field_name, $langcode = NULL)
```

## Documentation

```text
Returns the field items in the language they currently would be displayed.

@param $entity_type
  The type of $entity; e.g., 'node' or 'user'.
@param $entity
  The entity containing the data to be displayed.
@param $field_name
  The field to be displayed.
@param $langcode
  (optional) The language code $entity->{$field_name} has to be displayed in.
  Defaults to the current language.

@return
  An array of field items keyed by delta if available, FALSE otherwise.
```

## Code

```php
function field_get_items($entity_type, $entity, $field_name, $langcode = NULL) {
  $langcode = field_language($entity_type, $entity, $field_name, $langcode);
  return isset($entity->{$field_name}[$langcode]) ? $entity->{$field_name}[$langcode] : FALSE;
}
```

---
_Drupal 7.103 · [modules/field/field.module](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module) · Licensed GPL-2.0-or-later (see LICENSE)._

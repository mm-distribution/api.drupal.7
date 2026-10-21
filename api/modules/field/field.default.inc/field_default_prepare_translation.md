# field_default_prepare_translation()

- **Type:** Function
- **File:** [`modules/field/field.default.inc`](_file.md), lines 259–268 · [local source](../../../../source/modules/field/field.default.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.default.inc#L259-L268)
- **Module/theme:** field

## Signature

```php
function field_default_prepare_translation($entity_type, $entity, $field, $instance, $langcode, &$items, $source_entity, $source_langcode)
```

## Documentation

```text
Copies source field values into the entity to be prepared.

@param $entity_type
  The type of $entity; e.g. 'node' or 'user'.
@param $entity
  The entity to be prepared for translation.
@param $field
  The field structure for the operation.
@param $instance
  The instance structure for $field on $entity's bundle.
@param $langcode
  The language the entity has to be translated in.
@param $items
  $entity->{$field['field_name']}[$langcode], or an empty array if unset.
@param $source_entity
  The source entity holding the field values to be translated.
@param $source_langcode
  The source language from which translate.
```

## Code

```php
function field_default_prepare_translation($entity_type, $entity, $field, $instance, $langcode, &$items, $source_entity, $source_langcode) {
  $field_name = $field['field_name'];
  // If the field is untranslatable keep using LANGUAGE_NONE.
  if ($langcode == LANGUAGE_NONE) {
    $source_langcode = LANGUAGE_NONE;
  }
  if (isset($source_entity->{$field_name}[$source_langcode])) {
    $items = $source_entity->{$field_name}[$source_langcode];
  }
}
```

---
_Drupal 7.103 · [modules/field/field.default.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.default.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

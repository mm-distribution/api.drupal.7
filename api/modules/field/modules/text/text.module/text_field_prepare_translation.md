# text_field_prepare_translation()

- **Type:** Function
- **File:** [`modules/field/modules/text/text.module`](_file.md), lines 594–607 · [local source](../../../../../../source/modules/field/modules/text/text.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module#L594-L607)
- **Module/theme:** text
- **Implements:** [hook_field_prepare_translation()](../../../field.api.php/hook_field_prepare_translation.md)

## Signature

```php
function text_field_prepare_translation($entity_type, $entity, $field, $instance, $langcode, &$items, $source_entity, $source_langcode)
```

## Documentation

```text
Implements hook_field_prepare_translation().
```

## Code

```php
function text_field_prepare_translation($entity_type, $entity, $field, $instance, $langcode, &$items, $source_entity, $source_langcode) {
  // If the translating user is not permitted to use the assigned text format,
  // we must not expose the source values.
  $field_name = $field['field_name'];
  if (!empty($source_entity->{$field_name}[$source_langcode])) {
    $formats = filter_formats();
    foreach ($source_entity->{$field_name}[$source_langcode] as $delta => $item) {
      $format_id = $item['format'];
      if (!empty($format_id) && !filter_access($formats[$format_id])) {
        unset($items[$delta]);
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/field/modules/text/text.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module) · Licensed GPL-2.0-or-later (see LICENSE)._

# field_default_submit()

- **Type:** Function
- **File:** [`modules/field/field.default.inc`](_file.md), lines 89–94 · [local source](../../../../source/modules/field/field.default.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.default.inc#L89-L94)
- **Module/theme:** field

## Signature

```php
function field_default_submit($entity_type, $entity, $field, $instance, $langcode, &$items, $form, &$form_state)
```

## Documentation

_No docblock in source._

## Code

```php
function field_default_submit($entity_type, $entity, $field, $instance, $langcode, &$items, $form, &$form_state) {
  // Filter out empty values.
  $items = _field_filter_items($field, $items);
  // Reorder items to account for drag-n-drop reordering.
  $items = _field_sort_items($field, $items);
}
```

---
_Drupal 7.103 · [modules/field/field.default.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.default.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

# file_field_prepare_view()

- **Type:** Function
- **File:** [`modules/file/file.field.inc`](_file.md), lines 199–210 · [local source](../../../../source/modules/file/file.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc#L199-L210)
- **Module/theme:** file
- **Implements:** [hook_field_prepare_view()](../../field/field.api.php/hook_field_prepare_view.md)

## Signature

```php
function file_field_prepare_view($entity_type, $entities, $field, $instances, $langcode, &$items)
```

## Documentation

```text
Implements hook_field_prepare_view().
```

## Code

```php
function file_field_prepare_view($entity_type, $entities, $field, $instances, $langcode, &$items) {
  // Remove files specified to not be displayed.
  foreach ($entities as $id => $entity) {
    foreach ($items[$id] as $delta => $item) {
      if (!file_field_displayed($item, $field)) {
        unset($items[$id][$delta]);
      }
    }
    // Ensure consecutive deltas.
    $items[$id] = array_values($items[$id]);
  }
}
```

---
_Drupal 7.103 · [modules/file/file.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

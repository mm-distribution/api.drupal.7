# taxonomy_field_widget_info_alter()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 1488–1491 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L1488-L1491)
- **Module/theme:** taxonomy
- **Implements:** [hook_field_widget_info_alter()](../../field/field.api.php/hook_field_widget_info_alter.md)

## Signature

```php
function taxonomy_field_widget_info_alter(&$info)
```

## Documentation

```text
Implements hook_field_widget_info_alter().
```

## Code

```php
function taxonomy_field_widget_info_alter(&$info) {
  $info['options_select']['field types'][] = 'taxonomy_term_reference';
  $info['options_buttons']['field types'][] = 'taxonomy_term_reference';
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._

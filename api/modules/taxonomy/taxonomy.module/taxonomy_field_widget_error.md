# taxonomy_field_widget_error()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 1798–1800 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L1798-L1800)
- **Module/theme:** taxonomy
- **Implements:** [hook_field_widget_error()](../../field/field.api.php/hook_field_widget_error.md)

## Signature

```php
function taxonomy_field_widget_error($element, $error, $form, &$form_state)
```

## Documentation

```text
Implements hook_field_widget_error().
```

## Code

```php
function taxonomy_field_widget_error($element, $error, $form, &$form_state) {
  form_error($element, $error['message']);
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._

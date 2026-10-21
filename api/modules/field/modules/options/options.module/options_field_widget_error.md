# options_field_widget_error()

- **Type:** Function
- **File:** [`modules/field/modules/options/options.module`](_file.md), lines 394–396 · [local source](../../../../../../source/modules/field/modules/options/options.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.module#L394-L396)
- **Module/theme:** options
- **Implements:** [hook_field_widget_error()](../../../field.api.php/hook_field_widget_error.md)

## Signature

```php
function options_field_widget_error($element, $error, $form, &$form_state)
```

## Documentation

```text
Implements hook_field_widget_error().
```

## Code

```php
function options_field_widget_error($element, $error, $form, &$form_state) {
  form_error($element, $error['message']);
}
```

---
_Drupal 7.103 · [modules/field/modules/options/options.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.module) · Licensed GPL-2.0-or-later (see LICENSE)._

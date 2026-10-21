# number_field_widget_error()

- **Type:** Function
- **File:** [`modules/field/modules/number/number.module`](_file.md), lines 428–430 · [local source](../../../../../../source/modules/field/modules/number/number.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.module#L428-L430)
- **Module/theme:** number
- **Implements:** [hook_field_widget_error()](../../../field.api.php/hook_field_widget_error.md)

## Signature

```php
function number_field_widget_error($element, $error, $form, &$form_state)
```

## Documentation

```text
Implements hook_field_widget_error().
```

## Code

```php
function number_field_widget_error($element, $error, $form, &$form_state) {
  form_error($element['value'], $error['message']);
}
```

---
_Drupal 7.103 · [modules/field/modules/number/number.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.module) · Licensed GPL-2.0-or-later (see LICENSE)._

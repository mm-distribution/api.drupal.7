# field_test_field_widget_properties_user_alter()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.module`](_file.md), lines 242–247 · [local source](../../../../../source/modules/field/tests/field_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.module#L242-L247)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_field_widget_properties_ENTITY_TYPE_alter()](../../field.api.php/hook_field_widget_properties_ENTITY_TYPE_alter.md)

## Signature

```php
function field_test_field_widget_properties_user_alter(&$widget, $context)
```

## Documentation

```text
Implements hook_field_widget_properties_ENTITY_TYPE_alter().
```

## Code

```php
function field_test_field_widget_properties_user_alter(&$widget, $context) {
  // Always use buttons for the alter_test_options field on user forms.
  if ($context['field']['field_name'] == 'alter_test_options') {
    $widget['type'] = 'options_buttons';
  }
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.module](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._

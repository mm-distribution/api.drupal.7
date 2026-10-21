# field_test_field_attach_view_alter()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.module`](_file.md), lines 219–227 · [local source](../../../../../source/modules/field/tests/field_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.module#L219-L227)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_field_attach_view_alter()](../../field.api.php/hook_field_attach_view_alter.md)

## Signature

```php
function field_test_field_attach_view_alter(&$output, $context)
```

## Documentation

```text
Implements hook_field_attach_view_alter().
```

## Code

```php
function field_test_field_attach_view_alter(&$output, $context) {
  if (!empty($context['display']['settings']['alter'])) {
    $output['test_field'][] = array('#markup' => 'field_test_field_attach_view_alter');
  }

  if (isset($output['test_field'])) {
    $output['test_field'][] = array('#markup' => 'field language is ' . $context['language']);
  }
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.module](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._

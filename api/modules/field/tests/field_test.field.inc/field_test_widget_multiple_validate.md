# field_test_widget_multiple_validate()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.field.inc`](_file.md), lines 215–222 · [local source](../../../../../source/modules/field/tests/field_test.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc#L215-L222)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function field_test_widget_multiple_validate($element, &$form_state)
```

## Documentation

```text
Form element validation handler for 'test_field_widget_multiple' widget.
```

## Code

```php
function field_test_widget_multiple_validate($element, &$form_state) {
  $values = array_map('trim', explode(',', $element['#value']));
  $items = array();
  foreach ($values as $value) {
    $items[] = array('value' => $value);
  }
  form_set_value($element, $items, $form_state);
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

# field_test_field_widget_form()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.field.inc`](_file.md), lines 189–210 · [local source](../../../../../source/modules/field/tests/field_test.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc#L189-L210)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_field_widget_form()](../../field.api.php/hook_field_widget_form.md)

## Signature

```php
function field_test_field_widget_form(&$form, &$form_state, $field, $instance, $langcode, $items, $delta, $element)
```

## Documentation

```text
Implements hook_field_widget_form().
```

## Code

```php
function field_test_field_widget_form(&$form, &$form_state, $field, $instance, $langcode, $items, $delta, $element) {
  switch ($instance['widget']['type']) {
    case 'test_field_widget':
      $element += array(
        '#type' => 'textfield',
        '#default_value' => isset($items[$delta]['value']) ? $items[$delta]['value'] : '',
      );
      return array('value' => $element);

    case 'test_field_widget_multiple':
      $values = array();
      foreach ($items as $delta => $value) {
        $values[] = $value['value'];
      }
      $element += array(
        '#type' => 'textfield',
        '#default_value' => implode(', ', $values),
        '#element_validate' => array('field_test_widget_multiple_validate'),
      );
      return $element;
  }
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

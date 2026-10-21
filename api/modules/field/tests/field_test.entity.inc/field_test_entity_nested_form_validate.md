# field_test_entity_nested_form_validate()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.entity.inc`](_file.md), lines 461–467 · [local source](../../../../../source/modules/field/tests/field_test.entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc#L461-L467)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function field_test_entity_nested_form_validate($form, &$form_state)
```

## Documentation

```text
Validate handler for field_test_entity_nested_form().
```

## Code

```php
function field_test_entity_nested_form_validate($form, &$form_state) {
  $entity_1 = (object) $form_state['values'];
  field_attach_form_validate('test_entity', $entity_1, $form, $form_state);

  $entity_2 = (object) $form_state['values']['entity_2'];
  field_attach_form_validate('test_entity', $entity_2, $form['entity_2'], $form_state);
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.entity.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

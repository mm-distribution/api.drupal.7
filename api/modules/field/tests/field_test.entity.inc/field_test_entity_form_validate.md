# field_test_entity_form_validate()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.entity.inc`](_file.md), lines 386–388 · [local source](../../../../../source/modules/field/tests/field_test.entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc#L386-L388)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function field_test_entity_form_validate($form, &$form_state)
```

## Documentation

```text
Validate handler for field_test_entity_form().
```

## Code

```php
function field_test_entity_form_validate($form, &$form_state) {
  entity_form_field_validate('test_entity', $form, $form_state);
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.entity.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

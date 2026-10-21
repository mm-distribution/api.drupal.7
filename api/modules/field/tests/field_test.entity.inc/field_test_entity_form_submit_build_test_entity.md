# field_test_entity_form_submit_build_test_entity()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.entity.inc`](_file.md), lines 414–418 · [local source](../../../../../source/modules/field/tests/field_test.entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc#L414-L418)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function field_test_entity_form_submit_build_test_entity($form, &$form_state)
```

## Documentation

```text
Updates the form state's entity by processing this submission's values.
```

## Code

```php
function field_test_entity_form_submit_build_test_entity($form, &$form_state) {
  $entity = $form_state['test_entity'];
  entity_form_submit_build_entity('test_entity', $entity, $form, $form_state);
  return $entity;
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.entity.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

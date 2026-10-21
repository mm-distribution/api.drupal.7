# field_test_entity_nested_form_submit()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.entity.inc`](_file.md), lines 472–482 · [local source](../../../../../source/modules/field/tests/field_test.entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc#L472-L482)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function field_test_entity_nested_form_submit($form, &$form_state)
```

## Documentation

```text
Submit handler for field_test_entity_nested_form().
```

## Code

```php
function field_test_entity_nested_form_submit($form, &$form_state) {
  $entity_1 = (object) $form_state['values'];
  field_attach_submit('test_entity', $entity_1, $form, $form_state);
  field_test_entity_save($entity_1);

  $entity_2 = (object) $form_state['values']['entity_2'];
  field_attach_submit('test_entity', $entity_2, $form['entity_2'], $form_state);
  field_test_entity_save($entity_2);

  drupal_set_message(t('test_entities @id_1 and @id_2 have been updated.', array('@id_1' => $entity_1->ftid, '@id_2' => $entity_2->ftid)));
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.entity.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

# field_test_entity_form_submit()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.entity.inc`](_file.md), lines 393–409 · [local source](../../../../../source/modules/field/tests/field_test.entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc#L393-L409)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function field_test_entity_form_submit($form, &$form_state)
```

## Documentation

```text
Submit handler for field_test_entity_form().
```

## Code

```php
function field_test_entity_form_submit($form, &$form_state) {
  $entity = field_test_entity_form_submit_build_test_entity($form, $form_state);
  $insert = empty($entity->ftid);
  field_test_entity_save($entity);

  $message = $insert ? t('test_entity @id has been created.', array('@id' => $entity->ftid)) : t('test_entity @id has been updated.', array('@id' => $entity->ftid));
  drupal_set_message($message);

  if ($entity->ftid) {
    $form_state['redirect'] = 'test-entity/manage/' . $entity->ftid . '/edit';
  }
  else {
    // Error on save.
    drupal_set_message(t('The entity could not be saved.'), 'error');
    $form_state['rebuild'] = TRUE;
  }
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.entity.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

# field_test_entity_form()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.entity.inc`](_file.md), lines 344–381 · [local source](../../../../../source/modules/field/tests/field_test.entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc#L344-L381)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function field_test_entity_form($form, &$form_state, $entity, $add = FALSE)
```

## Documentation

```text
Test_entity form.
```

## Code

```php
function field_test_entity_form($form, &$form_state, $entity, $add = FALSE) {
  // During initial form build, add the entity to the form state for use during
  // form building and processing. During a rebuild, use what is in the form
  // state.
  if (!isset($form_state['test_entity'])) {
    $form_state['test_entity'] = $entity;
  }
  else {
    $entity = $form_state['test_entity'];
  }

  foreach (array('ftid', 'ftvid', 'fttype') as $key) {
    $form[$key] = array(
      '#type' => 'value',
      '#value' => isset($entity->$key) ? $entity->$key : NULL,
    );
  }

  // Add field widgets.
  field_attach_form('test_entity', $entity, $form, $form_state);

  if (!$add) {
    $form['revision'] = array(
      '#access' => user_access('administer field_test content'),
      '#type' => 'checkbox',
      '#title' => t('Create new revision'),
      '#default_value' => FALSE,
      '#weight' => 100,
    );
  }
  $form['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Save'),
    '#weight' => 101,
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.entity.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

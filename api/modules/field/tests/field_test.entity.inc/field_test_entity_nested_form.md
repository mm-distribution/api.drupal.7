# field_test_entity_nested_form()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.entity.inc`](_file.md), lines 423–456 · [local source](../../../../../source/modules/field/tests/field_test.entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc#L423-L456)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function field_test_entity_nested_form($form, &$form_state, $entity_1, $entity_2)
```

## Documentation

```text
Form combining two separate entities.
```

## Code

```php
function field_test_entity_nested_form($form, &$form_state, $entity_1, $entity_2) {
  // First entity.
  foreach (array('ftid', 'ftvid', 'fttype') as $key) {
    $form[$key] = array(
      '#type' => 'value',
      '#value' => $entity_1->$key,
    );
  }
  field_attach_form('test_entity', $entity_1, $form, $form_state);

  // Second entity.
  $form['entity_2'] = array(
    '#type' => 'fieldset',
    '#title' => t('Second entity'),
    '#tree' => TRUE,
    '#parents' => array('entity_2'),
    '#weight' => 50,
  );
  foreach (array('ftid', 'ftvid', 'fttype') as $key) {
    $form['entity_2'][$key] = array(
      '#type' => 'value',
      '#value' => $entity_2->$key,
    );
  }
  field_attach_form('test_entity', $entity_2, $form['entity_2'], $form_state);

  $form['save'] = array(
    '#type' => 'submit',
    '#value' => t('Save'),
    '#weight' => 100,
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.entity.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

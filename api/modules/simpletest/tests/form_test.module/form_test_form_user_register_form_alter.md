# form_test_form_user_register_form_alter()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 1897–1908 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L1897-L1908)
- **Module/theme:** batch_test
- **Implements:** [hook_form_FORM_ID_alter()](../../../system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function form_test_form_user_register_form_alter(&$form, &$form_state)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter() for the registration form.
```

## Code

```php
function form_test_form_user_register_form_alter(&$form, &$form_state) {
  $form['test_rebuild'] = array(
    '#type' => 'submit',
    '#value' => t('Rebuild'),
    '#submit' => array('form_test_user_register_form_rebuild'),
  );
  // If requested, add the test field by attaching the node page form.
  if (!empty($_REQUEST['field'])) {
    $node = (object)array('type' => 'page');
    field_attach_form('node', $node, $form, $form_state);
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._

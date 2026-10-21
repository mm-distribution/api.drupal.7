# node_access_test_form_node_form_alter()

- **Type:** Function
- **File:** [`modules/node/tests/node_access_test.module`](_file.md), lines 176–186 · [local source](../../../../../source/modules/node/tests/node_access_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_access_test.module#L176-L186)
- **Module/theme:** node_test
- **Implements:** [hook_form_BASE_FORM_ID_alter()](../../../system/system.api.php/hook_form_BASE_FORM_ID_alter.md)

## Signature

```php
function node_access_test_form_node_form_alter(&$form, $form_state)
```

## Documentation

```text
Implements hook_form_BASE_FORM_ID_alter().
```

## Code

```php
function node_access_test_form_node_form_alter(&$form, $form_state) {
  // Only show this checkbox for NodeAccessBaseTableTestCase.
  if (variable_get('node_access_test_private')) {
    $form['private'] = array(
      '#type' => 'checkbox',
      '#title' => t('Private'),
      '#description' => t('Check here if this content should be set private and only shown to privileged users.'),
      '#default_value' => isset($form['#node']->private) ? $form['#node']->private : FALSE,
    );
  }
}
```

---
_Drupal 7.103 · [modules/node/tests/node_access_test.module](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_access_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._

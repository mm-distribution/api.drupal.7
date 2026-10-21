# user_form_test_current_password()

- **Type:** Function
- **File:** [`modules/user/tests/user_form_test.module`](_file.md), lines 28–57 · [local source](../../../../../source/modules/user/tests/user_form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/tests/user_form_test.module#L28-L57)
- **Module/theme:** user_flood_test

## Signature

```php
function user_form_test_current_password($form, &$form_state, $account)
```

## Documentation

```text
A test form for user_validate_current_pass().
```

## Code

```php
function user_form_test_current_password($form, &$form_state, $account) {
  $account->user_form_test_field = '';
  $form['#user'] = $account;

  $form['user_form_test_field'] = array(
    '#type' => 'textfield',
    '#title' => t('Test field'),
    '#description' => t('A field that would require a correct password to change.'),
    '#required' => TRUE,
  );

  $form['current_pass'] = array(
    '#type' => 'password',
    '#title' => t('Current password'),
    '#size' => 25,
    '#description' => t('Enter your current password'),
  );

  $form['current_pass_required_values'] = array(
    '#type' => 'value',
    '#value' => array('user_form_test_field' => t('Test field')),
  );

  $form['#validate'][] = 'user_validate_current_pass';
  $form['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Test'),
  );
  return $form;
}
```

---
_Drupal 7.103 · [modules/user/tests/user_form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/user/tests/user_form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._

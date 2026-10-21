# user_login_block()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 1353–1380 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L1353-L1380)
- **Module/theme:** user

## Signature

```php
function user_login_block($form)
```

## Documentation

_No docblock in source._

## Code

```php
function user_login_block($form) {
  $form['#action'] = url(current_path(), array('query' => drupal_get_destination(), 'external' => FALSE));
  $form['#id'] = 'user-login-form';
  $form['#validate'] = user_login_default_validators();
  $form['#submit'][] = 'user_login_submit';
  $form['name'] = array('#type' => 'textfield',
    '#title' => t('Username'),
    '#maxlength' => USERNAME_MAX_LENGTH,
    '#size' => 15,
    '#required' => TRUE,
  );
  $form['pass'] = array('#type' => 'password',
    '#title' => t('Password'),
    '#size' => 15,
    '#required' => TRUE,
  );
  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array('#type' => 'submit',
    '#value' => t('Log in'),
  );
  $items = array();
  if (variable_get('user_register', USER_REGISTER_VISITORS_ADMINISTRATIVE_APPROVAL)) {
    $items[] = l(t('Create new account'), 'user/register', array('attributes' => array('title' => t('Create a new user account.'))));
  }
  $items[] = l(t('Request new password'), 'user/password', array('attributes' => array('title' => t('Request new password via e-mail.'))));
  $form['links'] = array('#markup' => theme('item_list', array('items' => $items)));
  return $form;
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._

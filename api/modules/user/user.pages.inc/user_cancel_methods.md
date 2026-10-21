# user_cancel_methods()

- **Type:** Function
- **File:** [`modules/user/user.pages.inc`](_file.md), lines 616–652 · [local source](../../../../source/modules/user/user.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.pages.inc#L616-L652)
- **Module/theme:** user

## Signature

```php
function user_cancel_methods()
```

## Documentation

```text
Helper function to return available account cancellation methods.

See documentation of hook_user_cancel_methods_alter().

@return
  An array containing all account cancellation methods as form elements.

@see hook_user_cancel_methods_alter()
@see user_admin_settings()
@see user_cancel_confirm_form()
@see user_multiple_cancel_confirm()
```

## Code

```php
function user_cancel_methods() {
  $methods = array(
    'user_cancel_block' => array(
      'title' => t('Disable the account and keep its content.'),
      'description' => t('Your account will be blocked and you will no longer be able to log in. All of your content will remain attributed to your user name.'),
    ),
    'user_cancel_block_unpublish' => array(
      'title' => t('Disable the account and unpublish its content.'),
      'description' => t('Your account will be blocked and you will no longer be able to log in. All of your content will be hidden from everyone but administrators.'),
    ),
    'user_cancel_reassign' => array(
      'title' => t('Delete the account and make its content belong to the %anonymous-name user.', array('%anonymous-name' => variable_get('anonymous', t('Anonymous')))),
      'description' => t('Your account will be removed and all account information deleted. All of your content will be assigned to the %anonymous-name user.', array('%anonymous-name' => variable_get('anonymous', t('Anonymous')))),
    ),
    'user_cancel_delete' => array(
      'title' => t('Delete the account and its content.'),
      'description' => t('Your account will be removed and all account information deleted. All of your content will also be deleted.'),
      'access' => user_access('administer users'),
    ),
  );
  // Allow modules to customize account cancellation methods.
  drupal_alter('user_cancel_methods', $methods);

  // Turn all methods into real form elements.
  $default_method = variable_get('user_cancel_method', 'user_cancel_block');
  foreach ($methods as $name => $method) {
    $form[$name] = array(
      '#type' => 'radio',
      '#title' => $method['title'],
      '#description' => (isset($method['description']) ? $method['description'] : NULL),
      '#return_value' => $name,
      '#default_value' => $default_method,
      '#parents' => array('user_cancel_method'),
    );
  }
  return $form;
}
```

---
_Drupal 7.103 · [modules/user/user.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/user/user.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

# user_admin()

- **Type:** Function
- **File:** [`modules/user/user.admin.inc`](_file.md), lines 23–41 · [local source](../../../../source/modules/user/user.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.admin.inc#L23-L41)
- **Module/theme:** user

## Signature

```php
function user_admin($callback_arg = '')
```

## Documentation

```text
Page callback: Generates the appropriate user administration form.

This function generates the user registration, multiple user cancellation,
or filtered user list admin form, depending on the argument and the POST
form values.

@param string $callback_arg
  (optional) Indicates which form to build. Defaults to '', which will
  trigger the user filter form. If the POST value 'op' is present, this
  function uses that value as the callback argument.

@return string
  A renderable form array for the respective request.
```

## Code

```php
function user_admin($callback_arg = '') {
  $op = isset($_POST['op']) ? $_POST['op'] : $callback_arg;

  switch ($op) {
    case t('Create new account'):
    case 'create':
      $build['user_register'] = drupal_get_form('user_register_form');
      break;
    default:
      if (!empty($_POST['accounts']) && isset($_POST['operation']) && ($_POST['operation'] == 'cancel')) {
        $build['user_multiple_cancel_confirm'] = drupal_get_form('user_multiple_cancel_confirm');
      }
      else {
        $build['user_filter_form'] = drupal_get_form('user_filter_form');
        $build['user_admin_account'] = drupal_get_form('user_admin_account');
      }
  }
  return $build;
}
```

---
_Drupal 7.103 · [modules/user/user.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/user/user.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

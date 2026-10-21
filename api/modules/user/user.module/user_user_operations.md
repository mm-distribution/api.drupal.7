# user_user_operations()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 3251–3315 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L3251-L3315)
- **Module/theme:** user
- **Implements:** [hook_user_operations()](../user.api.php/hook_user_operations.md)

## Signature

```php
function user_user_operations($form = array(), $form_state = array())
```

## Documentation

```text
Implements hook_user_operations().
```

## Code

```php
function user_user_operations($form = array(), $form_state = array()) {
  $operations = array(
    'unblock' => array(
      'label' => t('Unblock the selected users'),
      'callback' => 'user_user_operations_unblock',
    ),
    'block' => array(
      'label' => t('Block the selected users'),
      'callback' => 'user_user_operations_block',
    ),
    'cancel' => array(
      'label' => t('Cancel the selected user accounts'),
    ),
  );

  if (user_access('administer permissions')) {
    $roles = user_roles(TRUE);
    unset($roles[DRUPAL_AUTHENTICATED_RID]);  // Can't edit authenticated role.

    $add_roles = array();
    foreach ($roles as $key => $value) {
      $add_roles['add_role-' . $key] = $value;
    }

    $remove_roles = array();
    foreach ($roles as $key => $value) {
      $remove_roles['remove_role-' . $key] = $value;
    }

    if (count($roles)) {
      $role_operations = array(
        t('Add a role to the selected users') => array(
          'label' => $add_roles,
        ),
        t('Remove a role from the selected users') => array(
          'label' => $remove_roles,
        ),
      );

      $operations += $role_operations;
    }
  }

  // If the form has been posted, we need to insert the proper data for
  // role editing if necessary.
  if (!empty($form_state['submitted'])) {
    $operation_rid = explode('-', $form_state['values']['operation']);
    $operation = $operation_rid[0];
    if ($operation == 'add_role' || $operation == 'remove_role') {
      $rid = $operation_rid[1];
      if (user_access('administer permissions')) {
        $operations[$form_state['values']['operation']] = array(
          'callback' => 'user_multiple_role_edit',
          'callback arguments' => array($operation, $rid),
        );
      }
      else {
        watchdog('security', 'Detected malicious attempt to alter protected user fields.', array(), WATCHDOG_WARNING);
        return;
      }
    }
  }

  return $operations;
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._

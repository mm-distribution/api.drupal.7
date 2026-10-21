# user_admin_role()

- **Type:** Function
- **File:** [`modules/user/user.admin.inc`](_file.md), lines 967–1002 · [local source](../../../../source/modules/user/user.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.admin.inc#L967-L1002)
- **Module/theme:** user
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function user_admin_role($form, $form_state, $role)
```

## Documentation

```text
Form to configure a single role.

@ingroup forms
@see user_admin_role_validate()
@see user_admin_role_submit()
```

## Code

```php
function user_admin_role($form, $form_state, $role) {
  if ($role->rid == DRUPAL_ANONYMOUS_RID || $role->rid == DRUPAL_AUTHENTICATED_RID) {
    drupal_goto('admin/people/permissions/roles');
  }

  // Display the edit role form.
  $form['name'] = array(
    '#type' => 'textfield',
    '#title' => t('Role name'),
    '#default_value' => $role->name,
    '#size' => 30,
    '#required' => TRUE,
    '#maxlength' => 64,
    '#description' => t('The name for this role. Example: "moderator", "editorial board", "site architect".'),
  );
  $form['rid'] = array(
    '#type' => 'value',
    '#value' => $role->rid,
  );
  $form['weight'] = array(
    '#type' => 'value',
    '#value' => $role->weight,
  );
  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Save role'),
  );
  $form['actions']['delete'] = array(
    '#type' => 'submit',
    '#value' => t('Delete role'),
    '#submit' => array('user_admin_role_delete_submit'),
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/user/user.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/user/user.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

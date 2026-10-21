# user_admin_roles()

- **Type:** Function
- **File:** [`modules/user/user.admin.inc`](_file.md), lines 861–906 · [local source](../../../../source/modules/user/user.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.admin.inc#L861-L906)
- **Module/theme:** user
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function user_admin_roles($form, $form_state)
```

## Documentation

```text
Form to re-order roles or add a new one.

@ingroup forms
@see theme_user_admin_roles()
```

## Code

```php
function user_admin_roles($form, $form_state) {
  $roles = user_roles();
  $role_weights = db_query('SELECT r.rid, r.weight FROM {role} r')->fetchAllKeyed();

  $form['roles'] = array(
    '#tree' => TRUE,
  );
  foreach ($roles as $rid => $name) {
    $form['roles'][$rid]['#role'] = (object) array(
      'rid' => $rid,
      'name' => $name,
      'weight' => $role_weights[$rid],
    );
    $form['roles'][$rid]['#weight'] = $role_weights[$rid];
    $form['roles'][$rid]['weight'] = array(
      '#type' => 'textfield',
      '#title' => t('Weight for @title', array('@title' => $name)),
      '#title_display' => 'invisible',
      '#size' => 4,
      '#default_value' => $role_weights[$rid],
      '#attributes' => array('class' => array('role-weight')),
    );
  }

  $form['name'] = array(
    '#type' => 'textfield',
    '#title' => t('Name'),
    '#title_display' => 'invisible',
    '#size' => 32,
    '#maxlength' => 64,
  );
  $form['add'] = array(
    '#type' => 'submit',
    '#value' => t('Add role'),
    '#validate' => array('user_admin_role_validate'),
    '#submit' => array('user_admin_role_submit'),
  );
  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Save order'),
    '#submit' => array('user_admin_roles_order_submit'),
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/user/user.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/user/user.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

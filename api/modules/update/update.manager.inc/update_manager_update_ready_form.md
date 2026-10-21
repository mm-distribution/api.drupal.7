# update_manager_update_ready_form()

- **Type:** Function
- **File:** [`modules/update/update.manager.inc`](_file.md), lines 384–408 · [local source](../../../../source/modules/update/update.manager.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.manager.inc#L384-L408)
- **Module/theme:** update
- **Topics:** [update_manager_update](../../../topics/update_manager_update.md), [forms](../../../topics/forms.md)

## Signature

```php
function update_manager_update_ready_form($form, &$form_state)
```

## Documentation

```text
Form constructor for the update ready form.

Build the form when the site is ready to update (after downloading).

This form is an intermediary step in the automated update workflow. It is
presented to the site administrator after all the required updates have been
downloaded and verified. The point of this page is to encourage the user to
backup their site, give them the opportunity to put the site offline, and
then ask them to confirm that the update should continue. After this step,
the user is redirected to authorize.php to enter their file transfer
credentials and attempt to complete the update.

@see update_manager_update_ready_form_submit()
@see update_menu()
@ingroup forms
```

## Code

```php
function update_manager_update_ready_form($form, &$form_state) {
  if (!_update_manager_check_backends($form, 'update')) {
    return $form;
  }

  $form['backup'] = array(
    '#prefix' => '<strong>',
    '#markup' => t('Back up your database and site before you continue. <a href="@backup_url">Learn how</a>.', array('@backup_url' => url('http://drupal.org/node/22281'))),
    '#suffix' => '</strong>',
  );

  $form['maintenance_mode'] = array(
    '#title' => t('Perform updates with site in maintenance mode (strongly recommended)'),
    '#type' => 'checkbox',
    '#default_value' => TRUE,
  );

  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Continue'),
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/update/update.manager.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.manager.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

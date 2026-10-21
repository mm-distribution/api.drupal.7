# shortcut_set_switch()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.admin.inc`](_file.md), lines 38–104 · [local source](../../../../source/modules/shortcut/shortcut.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc#L38-L104)
- **Module/theme:** shortcut
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function shortcut_set_switch($form, &$form_state, $account = NULL)
```

## Documentation

```text
Form callback: builds the form for switching shortcut sets.

@param $form
  An associative array containing the structure of the form.
@param $form_state
  An associative array containing the current state of the form.
@param $account
  (optional) The user account whose shortcuts will be switched. Defaults to
  the current logged-in user.

@return
  An array representing the form definition.

@ingroup forms
@see shortcut_set_switch_validate()
@see shortcut_set_switch_submit()
```

## Code

```php
function shortcut_set_switch($form, &$form_state, $account = NULL) {
  global $user;
  if (!isset($account)) {
    $account = $user;
  }

  // Prepare the list of shortcut sets.
  $sets = shortcut_sets();
  $current_set = shortcut_current_displayed_set($account);

  $options = array();
  foreach ($sets as $name => $set) {
    $options[$name] = check_plain($set->title);
  }

  // Only administrators can add shortcut sets.
  $add_access = user_access('administer shortcuts');
  if ($add_access) {
    $options['new'] = t('New set');
  }

  if (count($options) > 1) {
    $form['account'] = array(
      '#type' => 'value',
      '#value' => $account,
    );

    $form['set'] = array(
      '#type' => 'radios',
      '#title' => $user->uid == $account->uid ? t('Choose a set of shortcuts to use') : t('Choose a set of shortcuts for this user'),
      '#options' => $options,
      '#default_value' => $current_set->set_name,
    );

    $form['new'] = array(
      '#type' => 'textfield',
      '#title' => t('Name'),
      '#title_display' => 'invisible',
      '#description' => t('The new set is created by copying items from your default shortcut set.'),
      '#access' => $add_access,
    );

    if ($user->uid != $account->uid) {
      $default_set = shortcut_default_set($account);
      $form['new']['#description'] = t('The new set is created by copying items from the %default set.', array('%default' => $default_set->title));
    }

    $form['#attached'] = array(
      'css' => array(drupal_get_path('module', 'shortcut') . '/shortcut.admin.css'),
      'js' => array(drupal_get_path('module', 'shortcut') . '/shortcut.admin.js'),
    );

    $form['actions'] = array('#type' => 'actions');
    $form['actions']['submit'] = array(
      '#type' => 'submit',
      '#value' => t('Change set'),
    );
  }
  else {
    // There is only 1 option, so output a message in the $form array.
    $form['info'] = array(
      '#markup' => '<p>' . t('You are currently using the %set-name shortcut set.', array('%set-name' => $current_set->title)) . '</p>',
    );
  }

  return $form;
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

# shortcut_set_delete_form()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.admin.inc`](_file.md), lines 673–707 · [local source](../../../../source/modules/shortcut/shortcut.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc#L673-L707)
- **Module/theme:** shortcut
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function shortcut_set_delete_form($form, &$form_state, $shortcut_set)
```

## Documentation

```text
Form callback: builds the confirmation form for deleting a shortcut set.

@param $form
  An associative array containing the structure of the form.
@param $form_state
  An associative array containing the current state of the form.
@param object $shortcut_set
  An object representing the shortcut set, as returned from
  shortcut_set_load().

@return
  An array representing the form definition.

@ingroup forms
@see shortcut_set_delete_form_submit()
```

## Code

```php
function shortcut_set_delete_form($form, &$form_state, $shortcut_set) {
  $form['shortcut_set'] = array(
    '#type' => 'value',
    '#value' => $shortcut_set->set_name,
  );

  // Find out how many users are directly assigned to this shortcut set, and
  // make a message.
  $number = db_query('SELECT COUNT(*) FROM {shortcut_set_users} WHERE set_name = :name', array(':name' => $shortcut_set->set_name))->fetchField();
  $info = '';
  if ($number) {
    $info .= '<p>' . format_plural($number,
      '1 user has chosen or been assigned to this shortcut set.',
      '@count users have chosen or been assigned to this shortcut set.') . '</p>';
  }

  // Also, if a module implements hook_shortcut_default_set(), it's possible
  // that this set is being used as a default set. Add a message about that too.
  if (count(module_implements('shortcut_default_set')) > 0) {
    $info .= '<p>' . t('If you have chosen this shortcut set as the default for some or all users, they may also be affected by deleting it.') . '</p>';
  }

  $form['info'] = array(
    '#markup' => $info,
  );

  return confirm_form(
    $form,
    t('Are you sure you want to delete the shortcut set %title?', array('%title' => $shortcut_set->title)),
    'admin/config/user-interface/shortcut/' . $shortcut_set->set_name,
    t('This action cannot be undone.'),
    t('Delete'),
    t('Cancel')
  );
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

# profile_admin_overview_submit()

- **Type:** Function
- **File:** [`modules/profile/profile.admin.inc`](_file.md), lines 82–102 · [local source](../../../../source/modules/profile/profile.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.admin.inc#L82-L102)
- **Module/theme:** profile

## Signature

```php
function profile_admin_overview_submit($form, &$form_state)
```

## Documentation

```text
Submit handler to update changed profile field weights and categories.

@see profile_admin_overview()
```

## Code

```php
function profile_admin_overview_submit($form, &$form_state) {
  foreach (element_children($form_state['values']) as $fid) {
    if (is_numeric($fid)) {
      $weight = $form_state['values'][$fid]['weight'];
      $category = $form_state['values'][$fid]['category'];
      if ($weight != $form[$fid]['weight']['#default_value'] || $category != $form[$fid]['category']['#default_value']) {
        db_update('profile_field')
          ->fields(array(
            'weight' => $weight,
            'category' => $category,
          ))
          ->condition('fid', $fid)
          ->execute();
      }
    }
  }

  drupal_set_message(t('Profile fields have been updated.'));
  cache_clear_all();
  menu_rebuild();
}
```

---
_Drupal 7.103 · [modules/profile/profile.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

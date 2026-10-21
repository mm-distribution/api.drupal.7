# profile_block_configure()

- **Type:** Function
- **File:** [`modules/profile/profile.module`](_file.md), lines 148–164 · [local source](../../../../source/modules/profile/profile.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module#L148-L164)
- **Module/theme:** profile
- **Implements:** [hook_block_configure()](../../block/block.api.php/hook_block_configure.md)

## Signature

```php
function profile_block_configure($delta = '')
```

## Documentation

```text
Implements hook_block_configure().
```

## Code

```php
function profile_block_configure($delta = '') {
  // Compile a list of fields to show
  $fields = array();
  $result = db_query('SELECT name, title, weight, visibility FROM {profile_field} WHERE visibility IN (:visibility) ORDER BY weight', array(':visibility' => array(PROFILE_PUBLIC, PROFILE_PUBLIC_LISTINGS)));
  foreach ($result as $record) {
    $fields[$record->name] = check_plain($record->title);
  }
  $fields['user_profile'] = t('Link to full user profile');
  $form['profile_block_author_fields'] = array(
    '#type' => 'checkboxes',
    '#title' => t('Profile fields to display'),
    '#default_value' => variable_get('profile_block_author_fields', array()),
    '#options' => $fields,
    '#description' => t('Select which profile fields you wish to display in the block. Only fields designated as public in the <a href="@profile-admin">profile field configuration</a> are available.', array('@profile-admin' => url('admin/config/people/profile'))),
  );
  return $form;
}
```

---
_Drupal 7.103 · [modules/profile/profile.module](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module) · Licensed GPL-2.0-or-later (see LICENSE)._

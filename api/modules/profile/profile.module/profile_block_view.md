# profile_block_view()

- **Type:** Function
- **File:** [`modules/profile/profile.module`](_file.md), lines 176–211 · [local source](../../../../source/modules/profile/profile.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module#L176-L211)
- **Module/theme:** profile
- **Implements:** [hook_block_view()](../../block/block.api.php/hook_block_view.md)

## Signature

```php
function profile_block_view($delta = '')
```

## Documentation

```text
Implements hook_block_view().
```

## Code

```php
function profile_block_view($delta = '') {
  if (user_access('access user profiles')) {
    $output = '';
    if (arg(0) == 'node' && is_numeric(arg(1)) && arg(2) == NULL) {
      $node = node_load(arg(1));
      $account = user_load($node->uid);

      if ($use_fields = variable_get('profile_block_author_fields', array())) {
        // Compile a list of fields to show.
        $fields = array();
        $result = db_query('SELECT * FROM {profile_field} WHERE visibility IN (:visibility) ORDER BY weight', array(':visibility' => array(PROFILE_PUBLIC, PROFILE_PUBLIC_LISTINGS)));
        foreach ($result as $record) {
          // Ensure that field is displayed only if it is among the defined block fields and, if it is private, the user has appropriate permissions.
          if (isset($use_fields[$record->name]) && $use_fields[$record->name]) {
            $fields[] = $record;
          }
        }
      }

      if (!empty($fields)) {
        $profile = _profile_update_user_fields($fields, $account);
        $output .= theme('profile_block', array('account' => $account, 'fields' => $profile));
      }

      if (isset($use_fields['user_profile']) && $use_fields['user_profile']) {
        $output .= '<div>' . l(t('View full user profile'), 'user/' . $account->uid) . '</div>';
      }
    }

    if ($output) {
      $block['subject'] = t('About %name', array('%name' => format_username($account)));
      $block['content'] = $output;
      return $block;
    }
  }
}
```

---
_Drupal 7.103 · [modules/profile/profile.module](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module) · Licensed GPL-2.0-or-later (see LICENSE)._

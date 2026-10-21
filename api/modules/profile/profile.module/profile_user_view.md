# profile_user_view()

- **Type:** Function
- **File:** [`modules/profile/profile.module`](_file.md), lines 328–359 · [local source](../../../../source/modules/profile/profile.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module#L328-L359)
- **Module/theme:** profile
- **Implements:** [hook_user_view()](../../user/user.api.php/hook_user_view.md)

## Signature

```php
function profile_user_view($account)
```

## Documentation

```text
Implements hook_user_view().
```

## Code

```php
function profile_user_view($account) {
  // Show private fields to administrators and people viewing their own account.
  if (user_access('administer users') || $GLOBALS['user']->uid == $account->uid) {
    $result = db_query('SELECT * FROM {profile_field} WHERE visibility <> :hidden ORDER BY category, weight', array(':hidden' => PROFILE_HIDDEN));
  }
  else {
    $result = db_query('SELECT * FROM {profile_field} WHERE visibility <> :private AND visibility <> :hidden ORDER BY category, weight', array(':private' => PROFILE_PRIVATE, ':hidden' => PROFILE_HIDDEN));
  }

  $fields = array();
  foreach ($result as $field) {
    if ($value = profile_view_field($account, $field)) {
      $title = ($field->type != 'checkbox') ? check_plain($field->title) : NULL;

      // Create a single fieldset for each category.
      if (!isset($account->content[$field->category])) {
        $account->content[$field->category] = array(
          '#type' => 'user_profile_category',
          '#title' => $field->category,
        );
      }

      $account->content[$field->category][$field->name] = array(
        '#type' => 'user_profile_item',
        '#title' => $title,
        '#markup' => $value,
        '#weight' => $field->weight,
        '#attributes' => array('class' => array('profile-' . $field->name)),
      );
    }
  }
}
```

---
_Drupal 7.103 · [modules/profile/profile.module](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module) · Licensed GPL-2.0-or-later (see LICENSE)._

# user_view()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 2694–2718 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L2694-L2718)
- **Module/theme:** user

## Signature

```php
function user_view($account, $view_mode = 'full', $langcode = NULL)
```

## Documentation

```text
Generate an array for rendering the given user.

When viewing a user profile, the $page array contains:

- $page['content']['Profile Category']:
  Profile categories keyed by their human-readable names.
- $page['content']['Profile Category']['profile_machine_name']:
  Profile fields keyed by their machine-readable names.
- $page['content']['user_picture']:
  User's rendered picture.
- $page['content']['summary']:
  Contains the default "History" profile data for a user.
- $page['content']['#account']:
  The user account of the profile being viewed.

To theme user profiles, copy modules/user/user-profile.tpl.php
to your theme directory, and edit it as instructed in that file's comments.

@param $account
  A user object.
@param $view_mode
  View mode, e.g. 'full'.
@param $langcode
  (optional) A language code to use for rendering. Defaults to the global
  content language of the current request.

@return
  An array as expected by drupal_render().
```

## Code

```php
function user_view($account, $view_mode = 'full', $langcode = NULL) {
  if (!isset($langcode)) {
    $langcode = $GLOBALS['language_content']->language;
  }

  // Retrieve all profile fields and attach to $account->content.
  user_build_content($account, $view_mode, $langcode);

  $build = $account->content;
  // We don't need duplicate rendering info in account->content.
  unset($account->content);

  $build += array(
    '#theme' => 'user_profile',
    '#account' => $account,
    '#view_mode' => $view_mode,
    '#language' => $langcode,
  );

  // Allow modules to modify the structured user.
  $type = 'user';
  drupal_alter(array('user_view', 'entity_view'), $build, $type);

  return $build;
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._

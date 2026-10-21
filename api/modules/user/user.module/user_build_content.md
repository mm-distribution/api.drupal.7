# user_build_content()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 2731–2754 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L2731-L2754)
- **Module/theme:** user

## Signature

```php
function user_build_content($account, $view_mode = 'full', $langcode = NULL)
```

## Documentation

```text
Builds a structured array representing the profile content.

@param $account
  A user object.
@param $view_mode
  View mode, e.g. 'full'.
@param $langcode
  (optional) A language code to use for rendering. Defaults to the global
  content language of the current request.
```

## Code

```php
function user_build_content($account, $view_mode = 'full', $langcode = NULL) {
  if (!isset($langcode)) {
    $langcode = $GLOBALS['language_content']->language;
  }

  // Remove previously built content, if exists.
  $account->content = array();

  // Allow modules to change the view mode.
  $view_mode = key(entity_view_mode_prepare('user', array($account->uid => $account), $view_mode, $langcode));

  // Build fields content.
  field_attach_prepare_view('user', array($account->uid => $account), $view_mode, $langcode);
  entity_prepare_view('user', array($account->uid => $account), $langcode);
  $account->content += field_attach_view('user', $account, $view_mode, $langcode);

  // Populate $account->content with a render() array.
  module_invoke_all('user_view', $account, $view_mode, $langcode);
  module_invoke_all('entity_view', $account, 'user', $view_mode, $langcode);

  // Make sure the current view mode is stored if no module has already
  // populated the related key.
  $account->content += array('#view_mode' => $view_mode);
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._

# template_preprocess_user_profile()

- **Type:** Function
- **File:** [`modules/user/user.pages.inc`](_file.md), lines 333–343 · [local source](../../../../source/modules/user/user.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.pages.inc#L333-L343)
- **Module/theme:** user

## Signature

```php
function template_preprocess_user_profile(&$variables)
```

## Documentation

```text
Process variables for user-profile.tpl.php.

@param array $variables
  An associative array containing:
  - elements: An associative array containing the user information and any
    fields attached to the user. Properties used:
    - #account: The user account of the profile being viewed.

@see user-profile.tpl.php
```

## Code

```php
function template_preprocess_user_profile(&$variables) {
  $account = $variables['elements']['#account'];

  // Helpful $user_profile variable for templates.
  foreach (element_children($variables['elements']) as $key) {
    $variables['user_profile'][$key] = $variables['elements'][$key];
  }

  // Preprocess fields.
  field_attach_preprocess('user', $account, $variables['elements'], $variables);
}
```

---
_Drupal 7.103 · [modules/user/user.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/user/user.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

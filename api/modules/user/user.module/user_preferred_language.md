# user_preferred_language()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 3629–3637 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L3629-L3637)
- **Module/theme:** user

## Signature

```php
function user_preferred_language($account, $default = NULL)
```

## Documentation

```text
Get the language object preferred by the user. This user preference can
be set on the user account editing page, and is only available if there
are more than one languages enabled on the site. If the user did not
choose a preferred language, or is the anonymous user, the $default
value, or if it is not set, the site default language will be returned.

@param $account
  User account to look up language for.
@param $default
  Optional default language object to return if the account
  has no valid language.
```

## Code

```php
function user_preferred_language($account, $default = NULL) {
  $language_list = language_list();
  if (!empty($account->language) && isset($language_list[$account->language])) {
    return $language_list[$account->language];
  }
  else {
    return $default ? $default : language_default();
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._

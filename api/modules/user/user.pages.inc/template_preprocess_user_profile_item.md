# template_preprocess_user_profile_item()

- **Type:** Function
- **File:** [`modules/user/user.pages.inc`](_file.md), lines 353–360 · [local source](../../../../source/modules/user/user.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.pages.inc#L353-L360)
- **Module/theme:** user

## Signature

```php
function template_preprocess_user_profile_item(&$variables)
```

## Documentation

```text
Process variables for user-profile-item.tpl.php.

The $variables array contains the following arguments:
- $element

@see user-profile-item.tpl.php
```

## Code

```php
function template_preprocess_user_profile_item(&$variables) {
  $variables['title'] = $variables['element']['#title'];
  $variables['value'] = $variables['element']['#markup'];
  $variables['attributes'] = '';
  if (isset($variables['element']['#attributes'])) {
    $variables['attributes'] = drupal_attributes($variables['element']['#attributes']);
  }
}
```

---
_Drupal 7.103 · [modules/user/user.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/user/user.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

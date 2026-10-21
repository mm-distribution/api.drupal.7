# template_preprocess_user_profile_category()

- **Type:** Function
- **File:** [`modules/user/user.pages.inc`](_file.md), lines 370–377 · [local source](../../../../source/modules/user/user.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.pages.inc#L370-L377)
- **Module/theme:** user

## Signature

```php
function template_preprocess_user_profile_category(&$variables)
```

## Documentation

```text
Process variables for user-profile-category.tpl.php.

The $variables array contains the following arguments:
- $element

@see user-profile-category.tpl.php
```

## Code

```php
function template_preprocess_user_profile_category(&$variables) {
  $variables['title'] = check_plain($variables['element']['#title']);
  $variables['profile_items'] = $variables['element']['#children'];
  $variables['attributes'] = '';
  if (isset($variables['element']['#attributes'])) {
    $variables['attributes'] = drupal_attributes($variables['element']['#attributes']);
  }
}
```

---
_Drupal 7.103 · [modules/user/user.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/user/user.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._

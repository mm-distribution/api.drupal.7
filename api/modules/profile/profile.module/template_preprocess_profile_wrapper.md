# template_preprocess_profile_wrapper()

- **Type:** Function
- **File:** [`modules/profile/profile.module`](_file.md), lines 591–597 · [local source](../../../../source/modules/profile/profile.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module#L591-L597)
- **Module/theme:** profile

## Signature

```php
function template_preprocess_profile_wrapper(&$variables)
```

## Documentation

```text
Process variables for profile-wrapper.tpl.php.

The $variables array contains the following arguments:
- $content

@see profile-wrapper.tpl.php
```

## Code

```php
function template_preprocess_profile_wrapper(&$variables) {
  $variables['current_field'] = '';
  if ($field = arg(1)) {
    $variables['current_field'] = $field;
    $variables['theme_hook_suggestions'][] = 'profile_wrapper__' . $field;
  }
}
```

---
_Drupal 7.103 · [modules/profile/profile.module](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module) · Licensed GPL-2.0-or-later (see LICENSE)._

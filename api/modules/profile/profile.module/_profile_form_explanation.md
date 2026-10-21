# _profile_form_explanation()

- **Type:** Function
- **File:** [`modules/profile/profile.module`](_file.md), lines 361–373 · [local source](../../../../source/modules/profile/profile.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module#L361-L373)
- **Module/theme:** profile

## Signature

```php
function _profile_form_explanation($field)
```

## Documentation

_No docblock in source._

## Code

```php
function _profile_form_explanation($field) {
  $output = filter_xss_admin($field->explanation);

  if ($field->type == 'list') {
    $output .= ' ' . t('Put each item on a separate line or separate them by commas. No HTML allowed.');
  }

  if ($field->visibility == PROFILE_PRIVATE) {
    $output .= ' ' . t('The content of this field is kept private and will not be shown publicly.');
  }

  return $output;
}
```

---
_Drupal 7.103 · [modules/profile/profile.module](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module) · Licensed GPL-2.0-or-later (see LICENSE)._

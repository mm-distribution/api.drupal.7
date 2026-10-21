# template_preprocess_profile_block()

- **Type:** Function
- **File:** [`modules/profile/profile.module`](_file.md), lines 541–555 · [local source](../../../../source/modules/profile/profile.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module#L541-L555)
- **Module/theme:** profile

## Signature

```php
function template_preprocess_profile_block(&$variables)
```

## Documentation

```text
Process variables for profile-block.tpl.php.

The $variables array contains the following arguments:
- $account
- $fields

@see profile-block.tpl.php
```

## Code

```php
function template_preprocess_profile_block(&$variables) {

  $variables['user_picture'] = theme('user_picture', array('account' => $variables['account']));
  $variables['profile'] = array();
  // Supply filtered version of $fields that have values.
  foreach ($variables['fields'] as $field) {
    if ($field->value) {
      $variables['profile'][$field->name] = new stdClass();
      $variables['profile'][$field->name]->title = check_plain($field->title);
      $variables['profile'][$field->name]->value = $field->value;
      $variables['profile'][$field->name]->type = $field->type;
    }
  }

}
```

---
_Drupal 7.103 · [modules/profile/profile.module](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module) · Licensed GPL-2.0-or-later (see LICENSE)._

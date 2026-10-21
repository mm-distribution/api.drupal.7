# profile_user_form_validate()

- **Type:** Function
- **File:** [`modules/profile/profile.module`](_file.md), lines 484–496 · [local source](../../../../source/modules/profile/profile.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module#L484-L496)
- **Module/theme:** profile

## Signature

```php
function profile_user_form_validate($form, &$form_state)
```

## Documentation

```text
Form validation handler for the user register/profile form.

@see profile_form_alter()
```

## Code

```php
function profile_user_form_validate($form, &$form_state) {
  $result = _profile_get_fields($form['#user_category'], $form['#user_category'] == 'register');
  foreach ($result as $field) {
    if (!empty($form_state['values'][$field->name])) {
      if ($field->type == 'url' && !valid_url($form_state['values'][$field->name], TRUE)) {
        form_set_error($field->name, t('The value provided for %field is not a valid URL.', array('%field' => $field->title)));
      }
    }
    elseif ($field->required && !user_access('administer users')) {
      form_set_error($field->name, t('The field %field is required.', array('%field' => $field->title)));
    }
  }
}
```

---
_Drupal 7.103 · [modules/profile/profile.module](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module) · Licensed GPL-2.0-or-later (see LICENSE)._

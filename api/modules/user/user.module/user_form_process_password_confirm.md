# user_form_process_password_confirm()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 3695–3723 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L3695-L3723)
- **Module/theme:** user

## Signature

```php
function user_form_process_password_confirm($element)
```

## Documentation

```text
Form element process handler for client-side password validation.

This #process handler is automatically invoked for 'password_confirm' form
elements to add the JavaScript and string translations for dynamic password
validation.

@see system_element_info()
```

## Code

```php
function user_form_process_password_confirm($element) {
  global $user;

  $js_settings = array(
    'password' => array(
      'strengthTitle' => t('Password strength:'),
      'hasWeaknesses' => t('To make your password stronger:'),
      'tooShort' => t('Make it at least 6 characters'),
      'addLowerCase' => t('Add lowercase letters'),
      'addUpperCase' => t('Add uppercase letters'),
      'addNumbers' => t('Add numbers'),
      'addPunctuation' => t('Add punctuation'),
      'sameAsUsername' => t('Make it different from your username'),
      'confirmSuccess' => t('yes'),
      'confirmFailure' => t('no'),
      'weak' => t('Weak'),
      'fair' => t('Fair'),
      'good' => t('Good'),
      'strong' => t('Strong'),
      'confirmTitle' => t('Passwords match:'),
      'username' => (isset($user->name) ? $user->name : ''),
    ),
  );

  $element['#attached']['js'][] = drupal_get_path('module', 'user') . '/user.js';
  $element['#attached']['js'][] = array('data' => $js_settings, 'type' => 'setting');

  return $element;
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._

# user_mail()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 2759–2764 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L2759-L2764)
- **Module/theme:** user
- **Implements:** [hook_mail()](../../system/system.api.php/hook_mail.md)

## Signature

```php
function user_mail($key, &$message, $params)
```

## Documentation

```text
Implements hook_mail().
```

## Code

```php
function user_mail($key, &$message, $params) {
  $language = $message['language'];
  $variables = array('user' => $params['account']);
  $message['subject'] .= _user_mail_text($key . '_subject', $language, $variables);
  $message['body'][] = _user_mail_text($key . '_body', $language, $variables);
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._

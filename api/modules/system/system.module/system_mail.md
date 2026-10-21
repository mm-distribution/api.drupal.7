# system_mail()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 3310–3318 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L3310-L3318)
- **Module/theme:** system
- **Implements:** [hook_mail()](../system.api.php/hook_mail.md)

## Signature

```php
function system_mail($key, &$message, $params)
```

## Documentation

```text
Implements hook_mail().
```

## Code

```php
function system_mail($key, &$message, $params) {
  $context = $params['context'];

  $subject = token_replace($context['subject'], $context);
  $body = token_replace($context['message'], $context);

  $message['subject'] .= str_replace(array("\r", "\n"), '', $subject);
  $message['body'][] = $body;
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._

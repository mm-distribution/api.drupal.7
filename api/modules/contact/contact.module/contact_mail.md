# contact_mail()

- **Type:** Function
- **File:** [`modules/contact/contact.module`](_file.md), lines 168–206 · [local source](../../../../source/modules/contact/contact.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.module#L168-L206)
- **Module/theme:** contact
- **Implements:** [hook_mail()](../../system/system.api.php/hook_mail.md)

## Signature

```php
function contact_mail($key, &$message, $params)
```

## Documentation

```text
Implements hook_mail().
```

## Code

```php
function contact_mail($key, &$message, $params) {
  $language = $message['language'];
  $variables = array(
    '!site-name' => variable_get('site_name', 'Drupal'),
    '!subject' => $params['subject'],
    '!category' => isset($params['category']['category']) ? $params['category']['category'] : '',
    '!form-url' => url($_GET['q'], array('absolute' => TRUE, 'language' => $language)),
    '!sender-name' => format_username($params['sender']),
    '!sender-url' => $params['sender']->uid ? url('user/' . $params['sender']->uid, array('absolute' => TRUE, 'language' => $language)) : $params['sender']->mail,
  );

  switch ($key) {
    case 'page_mail':
    case 'page_copy':
      $message['subject'] .= t('[!category] !subject', $variables, array('langcode' => $language->language));
      $message['body'][] = t("!sender-name (!sender-url) sent a message using the contact form at !form-url.", $variables, array('langcode' => $language->language));
      $message['body'][] = $params['message'];
      break;

    case 'page_autoreply':
      $message['subject'] .= t('[!category] !subject', $variables, array('langcode' => $language->language));
      $message['body'][] = $params['category']['reply'];
      break;

    case 'user_mail':
    case 'user_copy':
      $variables += array(
        '!recipient-name' => format_username($params['recipient']),
        '!recipient-edit-url' => url('user/' . $params['recipient']->uid . '/edit', array('absolute' => TRUE, 'language' => $language)),
      );
      $message['subject'] .= t('[!site-name] !subject', $variables, array('langcode' => $language->language));
      $message['body'][] = t('Hello !recipient-name,', $variables, array('langcode' => $language->language));
      $message['body'][] = t("!sender-name (!sender-url) has sent you a message via your contact form (!form-url) at !site-name.", $variables, array('langcode' => $language->language));
      $message['body'][] = t("If you don't want to receive such e-mails, you can change your settings at !recipient-edit-url.", $variables, array('langcode' => $language->language));
      $message['body'][] = t('Message:', array(), array('langcode' => $language->language));
      $message['body'][] = $params['message'];
      break;
  }
}
```

---
_Drupal 7.103 · [modules/contact/contact.module](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.module) · Licensed GPL-2.0-or-later (see LICENSE)._

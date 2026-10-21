# hook_mail_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 1987–1997 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L1987-L1997)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_mail_alter(&$message)
```

## Documentation

```text
Alter an email message created with the drupal_mail() function.

hook_mail_alter() allows modification of email messages created and sent
with drupal_mail(). Usage examples include adding and/or changing message
text, message fields, and message headers.

Email messages sent using functions other than drupal_mail() will not
invoke hook_mail_alter(). For example, a contributed module directly
calling the drupal_mail_system()->mail() or PHP mail() function
will not invoke this hook. All core modules use drupal_mail() for
messaging, it is best practice but not mandatory in contributed modules.

@param $message
  An array containing the message data. Keys in this array include:
 - 'id':
    The drupal_mail() id of the message. Look at module source code or
    drupal_mail() for possible id values.
 - 'to':
    The address or addresses the message will be sent to. The formatting of
    this string will be validated with the
    @link http://php.net/manual/filter.filters.validate.php PHP e-mail validation filter. @endlink
 - 'from':
    The address the message will be marked as being from, which is
    either a custom address or the site-wide default email address.
 - 'subject':
    Subject of the email to be sent. This must not contain any newline
    characters, or the email may not be sent properly.
 - 'body':
    An array of strings containing the message text. The message body is
    created by concatenating the individual array strings into a single text
    string using "\n\n" as a separator.
 - 'headers':
    Associative array containing mail headers, such as From, Sender,
    MIME-Version, Content-Type, etc.
 - 'params':
    An array of optional parameters supplied by the caller of drupal_mail()
    that is used to build the message before hook_mail_alter() is invoked.
 - 'language':
    The language object used to build the message before hook_mail_alter()
    is invoked.
 - 'send':
    Set to FALSE to abort sending this email message.

@see drupal_mail()
```

## Code

```php
function hook_mail_alter(&$message) {
  if ($message['id'] == 'modulename_messagekey') {
    if (!example_notifications_optin($message['to'], $message['id'])) {
      // If the recipient has opted to not receive such messages, cancel
      // sending.
      $message['send'] = FALSE;
      return;
    }
    $message['body'][] = "--\nMail sent out from " . variable_get('site_name', t('Drupal'));
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_mail_alter()".

- [simpletest_mail_alter()](../../simpletest/simpletest.module/simpletest_mail_alter.md) — `modules/simpletest/simpletest.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._

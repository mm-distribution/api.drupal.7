# simpletest_mail_alter()

- **Type:** Function
- **File:** [`modules/simpletest/simpletest.module`](_file.md), lines 651–655 · [local source](../../../../source/modules/simpletest/simpletest.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module#L651-L655)
- **Module/theme:** simpletest
- **Implements:** [hook_mail_alter()](../../system/system.api.php/hook_mail_alter.md)

## Signature

```php
function simpletest_mail_alter(&$message)
```

## Documentation

```text
Implements hook_mail_alter().

Aborts sending of messages with ID 'simpletest_cancel_test'.

@see MailTestCase::testCancelMessage()
```

## Code

```php
function simpletest_mail_alter(&$message) {
  if ($message['id'] == 'simpletest_cancel_test') {
    $message['send'] = FALSE;
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module) · Licensed GPL-2.0-or-later (see LICENSE)._

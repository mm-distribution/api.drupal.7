# MailTestCase::mail()

- **Type:** Method
- **File:** [`modules/simpletest/tests/mail.test`](../_file.md), lines 155–157 · [local source](../../../../../../source/modules/simpletest/tests/mail.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test#L155-L157)
- **Class:** [MailTestCase](../MailTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function mail(array $message)
```

## Documentation

```text
Send function that is called through the mail system.
```

## Code

```php
  public function mail(array $message) {
    self::$sent_message = $message;
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/mail.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test) · Licensed GPL-2.0-or-later (see LICENSE)._

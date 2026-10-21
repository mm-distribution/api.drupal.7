# MailTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/mail.test`](../_file.md), lines 24–29 · [local source](../../../../../../source/modules/simpletest/tests/mail.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test#L24-L29)
- **Class:** [MailTestCase](../MailTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp(array('simpletest'));

    // Set MailTestCase (i.e. this class) as the SMTP library
    variable_set('mail_system', array('default-system' => 'MailTestCase'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/mail.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test) · Licensed GPL-2.0-or-later (see LICENSE)._

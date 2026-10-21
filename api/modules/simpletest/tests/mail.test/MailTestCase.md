# MailTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/mail.test`](_file.md), lines 7–158 · [local source](../../../../../source/modules/simpletest/tests/mail.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test#L7-L158)
- **Module/theme:** batch_test

## Signature

```php
class MailTestCase extends DrupalWebTestCase implements MailSystemInterface
```

## Documentation

_No docblock in source._

## Properties

### $sent_message

```php
private static $sent_message;
```

```text
The most recent message that was sent through the test case.

We take advantage here of the fact that static variables are shared among
all instance of the same class.
```

## Methods (derived index)

- [getInfo()](MailTestCase/getInfo.md)
- [setUp()](MailTestCase/setUp.md)
- [testPluggableFramework()](MailTestCase/testPluggableFramework.md) — Assert that the pluggable mail system is functional.
- [testCancelMessage()](MailTestCase/testCancelMessage.md) — Test that message sending may be canceled.
- [testFromHeader()](MailTestCase/testFromHeader.md) — Checks for the site name in an auto-generated From: header.
- [testFromHeaderRfc2822Compliant()](MailTestCase/testFromHeaderRfc2822Compliant.md) — Checks for the site name in an auto-generated From: header.
- [format()](MailTestCase/format.md) — Concatenate and wrap the e-mail body for plain-text mails.
- [mail()](MailTestCase/mail.md) — Send function that is called through the mail system.

---
_Drupal 7.103 · [modules/simpletest/tests/mail.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test) · Licensed GPL-2.0-or-later (see LICENSE)._

# DrupalHtmlToTextTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/mail.test`](../_file.md), lines 164–170 · [local source](../../../../../../source/modules/simpletest/tests/mail.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test#L164-L170)
- **Class:** [DrupalHtmlToTextTestCase](../DrupalHtmlToTextTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public static function getInfo()
```

## Documentation

_No docblock in source._

## Code

```php
  public static function getInfo() {
    return array(
      'name'  => 'HTML to text conversion',
      'description' => 'Tests drupal_html_to_text().',
      'group' => 'Mail',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/mail.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test) · Licensed GPL-2.0-or-later (see LICENSE)._

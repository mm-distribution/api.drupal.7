# DrupalWebTestCase::assertUniqueText()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 3406–3408 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L3406-L3408)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function assertUniqueText($text, $message = '', $group = 'Other')
```

## Documentation

```text
Pass if the text is found ONLY ONCE on the text version of the page.

The text version is the equivalent of what a user would see when viewing
through a web browser. In other words the HTML has been filtered out of
the contents.

@param $text
  Plain text to look for.
@param $message
  Message to display.
@param $group
  The group this message belongs to, defaults to 'Other'.
@return
  TRUE on pass, FALSE on fail.
```

## Code

```php
  protected function assertUniqueText($text, $message = '', $group = 'Other') {
    return $this->assertUniqueTextHelper($text, $message, $group, TRUE);
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._

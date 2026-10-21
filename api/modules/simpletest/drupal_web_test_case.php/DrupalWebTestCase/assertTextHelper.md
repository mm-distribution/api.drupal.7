# DrupalWebTestCase::assertTextHelper()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 3380–3388 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L3380-L3388)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function assertTextHelper($text, $message, $group, $not_exists)
```

## Documentation

```text
Helper for assertText and assertNoText.

It is not recommended to call this function directly.

@param $text
  Plain text to look for.
@param $message
  Message to display.
@param $group
  The group this message belongs to.
@param $not_exists
  TRUE if this text should not exist, FALSE if it should.
@return
  TRUE on pass, FALSE on fail.
```

## Code

```php
  protected function assertTextHelper($text, $message, $group, $not_exists) {
    if ($this->plainTextContent === FALSE) {
      $this->plainTextContent = filter_xss($this->drupalGetContent(), array());
    }
    if (!$message) {
      $message = !$not_exists ? t('"@text" found', array('@text' => $text)) : t('"@text" not found', array('@text' => $text));
    }
    return $this->assert($not_exists == (strpos($this->plainTextContent, $text) === FALSE), $message, $group);
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._

# DrupalWebTestCase::assertUniqueTextHelper()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 3446–3460 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L3446-L3460)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function assertUniqueTextHelper($text, $message, $group, $be_unique)
```

## Documentation

```text
Helper for assertUniqueText and assertNoUniqueText.

It is not recommended to call this function directly.

@param $text
  Plain text to look for.
@param $message
  Message to display.
@param $group
  The group this message belongs to.
@param $be_unique
  TRUE if this text should be found only once, FALSE if it should be found more than once.
@return
  TRUE on pass, FALSE on fail.
```

## Code

```php
  protected function assertUniqueTextHelper($text, $message, $group, $be_unique) {
    if ($this->plainTextContent === FALSE) {
      $this->plainTextContent = filter_xss($this->drupalGetContent(), array());
    }
    if (!$message) {
      $message = '"' . $text . '"' . ($be_unique ? ' found only once' : ' found more than once');
    }
    $first_occurance = strpos($this->plainTextContent, $text);
    if ($first_occurance === FALSE) {
      return $this->assert(FALSE, $message, $group);
    }
    $offset = $first_occurance + strlen($text);
    $second_occurance = strpos($this->plainTextContent, $text, $offset);
    return $this->assert($be_unique == ($second_occurance === FALSE), $message, $group);
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._

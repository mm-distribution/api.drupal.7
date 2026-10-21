# DrupalWebTestCase::assertNoRaw()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 3321–3326 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L3321-L3326)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function assertNoRaw($raw, $message = '', $group = 'Other')
```

## Documentation

```text
Pass if the raw text is NOT found on the loaded page, fail otherwise. Raw text
refers to the raw HTML that the page generated.

@param $raw
  Raw (HTML) string to look for.
@param $message
  Message to display.
@param $group
  The group this message belongs to, defaults to 'Other'.
@return
  TRUE on pass, FALSE on fail.
```

## Code

```php
  protected function assertNoRaw($raw, $message = '', $group = 'Other') {
    if (!$message) {
      $message = t('Raw "@raw" not found', array('@raw' => $raw));
    }
    return $this->assert(strpos($this->drupalGetContent(), (string) $raw) === FALSE, $message, $group);
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._

# DrupalWebTestCase::assertNoTitle()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 3535–3544 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L3535-L3544)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function assertNoTitle($title, $message = '', $group = 'Other')
```

## Documentation

```text
Pass if the page title is not the given string.

@param $title
  The string the title should not be.
@param $message
  Message to display.
@param $group
  The group this message belongs to.
@return
  TRUE on pass, FALSE on fail.
```

## Code

```php
  protected function assertNoTitle($title, $message = '', $group = 'Other') {
    $actual = (string) current($this->xpath('//title'));
    if (!$message) {
      $message = t('Page title @actual is not equal to @unexpected.', array(
        '@actual' => var_export($actual, TRUE),
        '@unexpected' => var_export($title, TRUE),
      ));
    }
    return $this->assertNotEqual($actual, $title, $message, $group);
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._

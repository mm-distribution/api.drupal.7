# DrupalWebTestCase::assertFieldByName()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 3708–3723 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L3708-L3723)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function assertFieldByName($name, $value = NULL, $message = NULL)
```

## Documentation

```text
Asserts that a field exists in the current page with the given name and value.

@param $name
  Name of field to assert.
@param $value
  (optional) Value of the field to assert. You may pass in NULL (default)
  to skip checking the actual value, while still checking that the field
  exists.
@param $message
  Message to display.
@param $group
  The group this message belongs to.
@return
  TRUE on pass, FALSE on fail.
```

## Code

```php
  protected function assertFieldByName($name, $value = NULL, $message = NULL) {
    if (!isset($message)) {
      if (!isset($value)) {
        $message = t('Found field with name @name', array(
          '@name' => var_export($name, TRUE),
        ));
      }
      else {
        $message = t('Found field with name @name and value @value', array(
          '@name' => var_export($name, TRUE),
          '@value' => var_export($value, TRUE),
        ));
      }
    }
    return $this->assertFieldByXPath($this->constructFieldXpath('name', $name), $value, $message, t('Browser'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._

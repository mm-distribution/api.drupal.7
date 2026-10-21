# DrupalWebTestCase::assertFieldById()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 3763–3765 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L3763-L3765)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function assertFieldById($id, $value = '', $message = '')
```

## Documentation

```text
Asserts that a field exists in the current page with the given ID and value.

@param $id
  ID of field to assert.
@param $value
  (optional) Value for the field to assert. You may pass in NULL to skip
  checking the value, while still checking that the field exists.
  However, the default value ('') asserts that the field value is an empty
  string.
@param $message
  (optional) Message to display.
@param $group
  The group this message belongs to.
@return
  TRUE on pass, FALSE on fail.
```

## Code

```php
  protected function assertFieldById($id, $value = '', $message = '') {
    return $this->assertFieldByXPath($this->constructFieldXpath('id', $id), $value, $message ? $message : t('Found field by id @id', array('@id' => $id)), t('Browser'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._

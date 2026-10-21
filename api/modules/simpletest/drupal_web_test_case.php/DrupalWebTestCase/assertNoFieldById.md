# DrupalWebTestCase::assertNoFieldById()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 3784–3786 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L3784-L3786)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function assertNoFieldById($id, $value = '', $message = '')
```

## Documentation

```text
Asserts that a field does not exist with the given ID and value.

@param $id
  ID of field to assert.
@param $value
  (optional) Value for the field, to assert that the field's value on the
  page doesn't match it. You may pass in NULL to skip checking the value,
  while still checking that the field doesn't exist. However, the default
  value ('') asserts that the field value is not an empty string.
@param $message
  (optional) Message to display.
@param $group
  The group this message belongs to.
@return
  TRUE on pass, FALSE on fail.
```

## Code

```php
  protected function assertNoFieldById($id, $value = '', $message = '') {
    return $this->assertNoFieldByXPath($this->constructFieldXpath('id', $id), $value, $message ? $message : t('Did not find field by id @id', array('@id' => $id)), t('Browser'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._

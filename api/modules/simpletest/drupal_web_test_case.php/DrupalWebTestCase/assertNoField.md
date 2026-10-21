# DrupalWebTestCase::assertNoField()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 3882–3884 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L3882-L3884)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function assertNoField($field, $message = '', $group = 'Other')
```

## Documentation

```text
Asserts that a field does not exist with the given name or ID.

@param $field
  Name or ID of field to assert.
@param $message
  (optional) Message to display.
@param $group
  The group this message belongs to.
@return
  TRUE on pass, FALSE on fail.
```

## Code

```php
  protected function assertNoField($field, $message = '', $group = 'Other') {
    return $this->assertNoFieldByXPath($this->constructFieldXpath('name', $field) . '|' . $this->constructFieldXpath('id', $field), NULL, $message, $group);
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._

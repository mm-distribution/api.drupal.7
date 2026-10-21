# DrupalWebTestCase::assertNoFieldByXPath()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 3674–3690 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L3674-L3690)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function assertNoFieldByXPath($xpath, $value = NULL, $message = '', $group = 'Other')
```

## Documentation

```text
Asserts that a field doesn't exist or its value doesn't match, by XPath.

@param $xpath
  XPath used to find the field.
@param $value
  (optional) Value for the field, to assert that the field's value on the
  page doesn't match it. You may pass in NULL to skip checking the
  value, while still checking that the field doesn't exist.
@param $message
  (optional) Message to display.
@param $group
  (optional) The group this message belongs to.

@return
  TRUE on pass, FALSE on fail.
```

## Code

```php
  protected function assertNoFieldByXPath($xpath, $value = NULL, $message = '', $group = 'Other') {
    $fields = $this->xpath($xpath);

    // If value specified then check array for match.
    $found = TRUE;
    if (isset($value)) {
      $found = FALSE;
      if ($fields) {
        foreach ($fields as $field) {
          if ($field['value'] == $value) {
            $found = TRUE;
          }
        }
      }
    }
    return $this->assertFalse($fields && $found, $message, $group);
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._

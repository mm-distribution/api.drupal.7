# DrupalWebTestCase::assertFieldByXPath()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 3599–3633 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L3599-L3633)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function assertFieldByXPath($xpath, $value = NULL, $message = '', $group = 'Other')
```

## Documentation

```text
Asserts that a field exists in the current page by the given XPath.

@param $xpath
  XPath used to find the field.
@param $value
  (optional) Value of the field to assert. You may pass in NULL (default)
  to skip checking the actual value, while still checking that the field
  exists.
@param $message
  (optional) Message to display.
@param $group
  (optional) The group this message belongs to.

@return
  TRUE on pass, FALSE on fail.
```

## Code

```php
  protected function assertFieldByXPath($xpath, $value = NULL, $message = '', $group = 'Other') {
    $fields = $this->xpath($xpath);

    // If value specified then check array for match.
    $found = TRUE;
    if (isset($value)) {
      $found = FALSE;
      if ($fields) {
        foreach ($fields as $field) {
          if (isset($field['value']) && $field['value'] == $value) {
            // Input element with correct value.
            $found = TRUE;
          }
          elseif (isset($field->option)) {
            // Select element found.
            if ($this->getSelectedItem($field) == $value) {
              $found = TRUE;
            }
            else {
              // No item selected so use first item.
              $items = $this->getAllOptions($field);
              if (!empty($items) && $items[0]['value'] == $value) {
                $found = TRUE;
              }
            }
          }
          elseif ((string) $field == $value) {
            // Text area with correct text.
            $found = TRUE;
          }
        }
      }
    }
    return $this->assertTrue($fields && $found, $message, $group);
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._

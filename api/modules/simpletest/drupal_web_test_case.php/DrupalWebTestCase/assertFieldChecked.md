# DrupalWebTestCase::assertFieldChecked()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 3798–3801 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L3798-L3801)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function assertFieldChecked($id, $message = '')
```

## Documentation

```text
Asserts that a checkbox field in the current page is checked.

@param $id
  ID of field to assert.
@param $message
  (optional) Message to display.
@return
  TRUE on pass, FALSE on fail.
```

## Code

```php
  protected function assertFieldChecked($id, $message = '') {
    $elements = $this->xpath('//input[@id=:id]', array(':id' => $id));
    return $this->assertTrue(isset($elements[0]) && !empty($elements[0]['checked']), $message ? $message : t('Checkbox field @id is checked.', array('@id' => $id)), t('Browser'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._

# DrupalWebTestCase::assertOptionSelected()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 3832–3835 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L3832-L3835)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function assertOptionSelected($id, $option, $message = '')
```

## Documentation

```text
Asserts that a select option in the current page is checked.

@param $id
  ID of select field to assert.
@param $option
  Option to assert.
@param $message
  (optional) Message to display.
@return
  TRUE on pass, FALSE on fail.

@todo $id is unusable. Replace with $name.
```

## Code

```php
  protected function assertOptionSelected($id, $option, $message = '') {
    $elements = $this->xpath('//select[@id=:id]//option[@value=:option]', array(':id' => $id, ':option' => $option));
    return $this->assertTrue(isset($elements[0]) && !empty($elements[0]['selected']), $message ? $message : t('Option @option for field @id is selected.', array('@option' => $option, '@id' => $id)), t('Browser'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._

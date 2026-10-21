# DrupalWebTestCase::assertNoLink()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 2998–3002 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L2998-L3002)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function assertNoLink($label, $message = '', $group = 'Other')
```

## Documentation

```text
Pass if a link with the specified label is not found.

@param $label
  Text between the anchor tags.
@param $message
  Message to display.
@param $group
  The group this message belongs to, defaults to 'Other'.
@return
  TRUE if the assertion succeeded, FALSE otherwise.
```

## Code

```php
  protected function assertNoLink($label, $message = '', $group = 'Other') {
    $links = $this->xpath('//a[normalize-space(text())=:label]', array(':label' => $label));
    $message = ($message ?  $message : t('Link with label %label not found.', array('%label' => $label)));
    return $this->assert(empty($links), $message, $group);
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._

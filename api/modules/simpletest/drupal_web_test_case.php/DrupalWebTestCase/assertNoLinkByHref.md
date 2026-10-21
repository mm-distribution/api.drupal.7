# DrupalWebTestCase::assertNoLinkByHref()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 3038–3042 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L3038-L3042)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function assertNoLinkByHref($href, $message = '', $group = 'Other')
```

## Documentation

```text
Pass if a link containing a given href (part) is not found.

@param $href
  The full or partial value of the 'href' attribute of the anchor tag.
@param $message
  Message to display.
@param $group
  The group this message belongs to, defaults to 'Other'.

@return
  TRUE if the assertion succeeded, FALSE otherwise.
```

## Code

```php
  protected function assertNoLinkByHref($href, $message = '', $group = 'Other') {
    $links = $this->xpath('//a[contains(@href, :href)]', array(':href' => $href));
    $message = ($message ?  $message : t('No link containing href %href found.', array('%href' => $href)));
    return $this->assert(empty($links), $message, $group);
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._

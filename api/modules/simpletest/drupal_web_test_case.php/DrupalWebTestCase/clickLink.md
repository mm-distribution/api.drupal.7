# DrupalWebTestCase::clickLink()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 3060–3070 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L3060-L3070)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function clickLink($label, $index = 0)
```

## Documentation

```text
Follows a link by name.

Will click the first link found with this link text by default, or a later
one if an index is given. Match is case sensitive with normalized space.
The label is translated label.

If the link is discovered and clicked, the test passes. Fail otherwise.

@param $label
  Text between the anchor tags.
@param $index
  Link position counting from zero.
@return
  Page contents on success, or FALSE on failure.
```

## Code

```php
  protected function clickLink($label, $index = 0) {
    $url_before = $this->getUrl();
    $urls = $this->xpath('//a[normalize-space(text())=:label]', array(':label' => $label));
    if (isset($urls[$index])) {
      $url_target = $this->getAbsoluteUrl($urls[$index]['href']);
      $this->pass(t('Clicked link %label (@url_target) from @url_before', array('%label' => $label, '@url_target' => $url_target, '@url_before' => $url_before)), 'Browser');
      return $this->drupalGet($url_target);
    }
    $this->fail(t('Link %label does not exist on @url_before', array('%label' => $label, '@url_before' => $url_before)), 'Browser');
    return FALSE;
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._

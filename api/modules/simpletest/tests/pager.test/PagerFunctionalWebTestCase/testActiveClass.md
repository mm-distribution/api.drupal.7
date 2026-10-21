# PagerFunctionalWebTestCase::testActiveClass()

- **Type:** Method
- **File:** [`modules/simpletest/tests/pager.test`](../_file.md), lines 40–57 · [local source](../../../../../../source/modules/simpletest/tests/pager.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/pager.test#L40-L57)
- **Class:** [PagerFunctionalWebTestCase](../PagerFunctionalWebTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testActiveClass()
```

## Documentation

```text
Tests markup and CSS classes of pager links.
```

## Code

```php
  function testActiveClass() {
    // Verify first page.
    $this->drupalGet('admin/reports/dblog');
    $current_page = 0;
    $this->assertPagerItems($current_page);

    // Verify any page but first/last.
    $current_page++;
    $this->drupalGet('admin/reports/dblog', array('query' => array('page' => $current_page)));
    $this->assertPagerItems($current_page);

    // Verify last page.
    $elements = $this->xpath('//li[contains(@class, :class)]/a', array(':class' => 'pager-last'));
    preg_match('@page=(\d+)@', $elements[0]['href'], $matches);
    $current_page = (int) $matches[1];
    $this->drupalGet($GLOBALS['base_root'] . $elements[0]['href'], array('external' => TRUE));
    $this->assertPagerItems($current_page);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/pager.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/pager.test) · Licensed GPL-2.0-or-later (see LICENSE)._

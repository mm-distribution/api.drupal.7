# MenuRouterTestCase::menuItemTitlesCasesHelper()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 605–610 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L605-L610)
- **Class:** [MenuRouterTestCase](../MenuRouterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
private function menuItemTitlesCasesHelper($case_no, $override = FALSE)
```

## Documentation

```text
Get a URL and assert the title given a case number. If override is true,
the title is asserted to begin with "Alternative".
```

## Code

```php
  private function menuItemTitlesCasesHelper($case_no, $override = FALSE) {
    $this->drupalGet('menu-title-test/case' . $case_no);
    $this->assertResponse(200);
    $asserted_title = $override ? 'Alternative example title - Case ' . $case_no : 'Example title - Case ' . $case_no;
    $this->assertTitle($asserted_title . ' | Drupal', format_string('Menu title is: %title.', array('%title' => $asserted_title)), 'Menu');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._

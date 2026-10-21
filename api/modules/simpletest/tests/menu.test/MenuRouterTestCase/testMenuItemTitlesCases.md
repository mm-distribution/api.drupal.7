# MenuRouterTestCase::testMenuItemTitlesCases()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 583–599 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L583-L599)
- **Class:** [MenuRouterTestCase](../MenuRouterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testMenuItemTitlesCases()
```

## Documentation

```text
Tests the possible ways to set the title for menu items.
Also tests that menu item titles work with string overrides.
```

## Code

```php
  function testMenuItemTitlesCases() {

    // Build array with string overrides.
    $test_data = array(
      1 => array('Example title - Case 1' => 'Alternative example title - Case 1'),
      2 => array('Example @sub1 - Case @op2' => 'Alternative example @sub1 - Case @op2'),
      3 => array('Example title' => 'Alternative example title'),
      4 => array('Example title' => 'Alternative example title'),
    );

    foreach ($test_data as $case_no => $override) {
      $this->menuItemTitlesCasesHelper($case_no);
      variable_set('locale_custom_strings_en', array('' => $override));
      $this->menuItemTitlesCasesHelper($case_no, TRUE);
      variable_set('locale_custom_strings_en', array());
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._

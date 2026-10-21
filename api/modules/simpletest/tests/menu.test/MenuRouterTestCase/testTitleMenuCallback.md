# MenuRouterTestCase::testTitleMenuCallback()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 155–162 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L155-L162)
- **Class:** [MenuRouterTestCase](../MenuRouterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testTitleMenuCallback()
```

## Documentation

```text
Tests page title of MENU_CALLBACKs.
```

## Code

```php
  function testTitleMenuCallback() {
    // Verify that the menu router item title is not visible.
    $this->drupalGet('');
    $this->assertNoText(t('Menu Callback Title'));
    // Verify that the menu router item title is output as page title.
    $this->drupalGet('menu_callback_title');
    $this->assertText(t('Menu Callback Title'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._

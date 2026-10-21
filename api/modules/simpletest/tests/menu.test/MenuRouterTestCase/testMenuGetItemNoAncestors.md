# MenuRouterTestCase::testMenuGetItemNoAncestors()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 516–519 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L516-L519)
- **Class:** [MenuRouterTestCase](../MenuRouterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testMenuGetItemNoAncestors()
```

## Documentation

```text
Test menu_get_item() with empty ancestors.
```

## Code

```php
  function testMenuGetItemNoAncestors() {
    variable_set('menu_masks', array());
    $this->drupalGet('');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._

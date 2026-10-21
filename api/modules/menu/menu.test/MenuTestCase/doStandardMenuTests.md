# MenuTestCase::doStandardMenuTests()

- **Type:** Method
- **File:** [`modules/menu/menu.test`](../_file.md), lines 92–95 · [local source](../../../../../source/modules/menu/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test#L92-L95)
- **Class:** [MenuTestCase](../MenuTestCase.md)
- **Module/theme:** menu

## Signature

```php
function doStandardMenuTests()
```

## Documentation

```text
Test standard menu functionality using navigation menu.
```

## Code

```php
  function doStandardMenuTests() {
    $this->doMenuTests();
    $this->addInvalidMenuLink();
  }
```

---
_Drupal 7.103 · [modules/menu/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._

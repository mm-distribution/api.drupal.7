# MenuTestCase::doCustomMenuTests()

- **Type:** Method
- **File:** [`modules/menu/menu.test`](../_file.md), lines 101–106 · [local source](../../../../../source/modules/menu/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test#L101-L106)
- **Class:** [MenuTestCase](../MenuTestCase.md)
- **Module/theme:** menu

## Signature

```php
function doCustomMenuTests()
```

## Documentation

```text
Test custom menu functionality using navigation menu.
```

## Code

```php
  function doCustomMenuTests() {
    $this->menu = $this->addCustomMenu();
    $this->doMenuTests($this->menu['menu_name']);
    $this->addInvalidMenuLink($this->menu['menu_name']);
    $this->addCustomMenuCRUD();
  }
```

---
_Drupal 7.103 · [modules/menu/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._

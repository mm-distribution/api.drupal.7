# MenuNodeTestCase::setUp()

- **Type:** Method
- **File:** [`modules/menu/menu.test`](../_file.md), lines 740–752 · [local source](../../../../../source/modules/menu/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test#L740-L752)
- **Class:** [MenuNodeTestCase](../MenuNodeTestCase.md)
- **Module/theme:** menu

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('menu');

    $this->admin_user = $this->drupalCreateUser(array(
      'access administration pages',
      'administer content types',
      'administer menu',
      'create page content',
      'edit any page content',
      'delete any page content',
    ));
    $this->drupalLogin($this->admin_user);
  }
```

---
_Drupal 7.103 · [modules/menu/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._

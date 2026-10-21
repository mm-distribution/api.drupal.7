# MenuTestCase::setUp()

- **Type:** Method
- **File:** [`modules/menu/menu.test`](../_file.md), lines 22–27 · [local source](../../../../../source/modules/menu/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test#L22-L27)
- **Class:** [MenuTestCase](../MenuTestCase.md)
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
    // Create users.
    $this->big_user = $this->drupalCreateUser(array('access administration pages', 'administer blocks', 'administer menu', 'create article content'));
    $this->std_user = $this->drupalCreateUser(array());
  }
```

---
_Drupal 7.103 · [modules/menu/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._

# ToolbarTestCase::setUp()

- **Type:** Method
- **File:** [`modules/toolbar/toolbar.test`](../_file.md), lines 15–21 · [local source](../../../../../source/modules/toolbar/toolbar.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/toolbar/toolbar.test#L15-L21)
- **Class:** [ToolbarTestCase](../ToolbarTestCase.md)
- **Module/theme:** toolbar

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp();

    // Setup users.
    $this->admin_user = $this->drupalCreateUser(array('access toolbar'));
    $this->drupalLogin($this->admin_user);
  }
```

---
_Drupal 7.103 · [modules/toolbar/toolbar.test](https://github.com/drupal/drupal/blob/7.103/modules/toolbar/toolbar.test) · Licensed GPL-2.0-or-later (see LICENSE)._

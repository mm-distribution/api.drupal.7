# UpdateScriptFunctionalTest::setUp()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 2519–2523 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L2519-L2523)
- **Class:** [UpdateScriptFunctionalTest](../UpdateScriptFunctionalTest.md)
- **Module/theme:** system

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('update_script_test');
    $this->update_url = $GLOBALS['base_url'] . '/update.php';
    $this->update_user = $this->drupalCreateUser(array('administer software updates'));
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._

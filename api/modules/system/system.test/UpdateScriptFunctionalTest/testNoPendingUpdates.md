# UpdateScriptFunctionalTest::testNoPendingUpdates()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 2528–2537 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L2528-L2537)
- **Class:** [UpdateScriptFunctionalTest](../UpdateScriptFunctionalTest.md)
- **Module/theme:** system

## Signature

```php
function testNoPendingUpdates()
```

## Documentation

```text
Tests that there are no pending updates for the first test method.
```

## Code

```php
  function testNoPendingUpdates() {
    // Ensure that for the first test method in a class, there are no pending
    // updates. This tests a drupal_get_schema_versions() bug that previously
    // led to the wrong schema version being recorded for the initial install
    // of a child site during automated testing.
    $this->drupalLogin($this->update_user);
    $this->drupalGet($this->update_url, array('external' => TRUE));
    $this->drupalPost(NULL, array(), t('Continue'));
    $this->assertText(t('No pending updates.'), 'End of update process was reached.');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._

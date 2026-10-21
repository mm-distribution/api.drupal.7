# FloodFunctionalTest::testCleanUp()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 2708–2728 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L2708-L2728)
- **Class:** [FloodFunctionalTest](../FloodFunctionalTest.md)
- **Module/theme:** system

## Signature

```php
function testCleanUp()
```

## Documentation

```text
Test flood control mechanism clean-up.
```

## Code

```php
  function testCleanUp() {
    $threshold = 1;
    $window_expired = -1;
    $name = 'flood_test_cleanup';

    // Register expired event.
    flood_register_event($name, $window_expired);
    // Verify event is not allowed.
    $this->assertFalse(flood_is_allowed($name, $threshold));
    // Run cron and verify event is now allowed.
    $this->cronRun();
    $this->assertTrue(flood_is_allowed($name, $threshold));

    // Register unexpired event.
    flood_register_event($name);
    // Verify event is not allowed.
    $this->assertFalse(flood_is_allowed($name, $threshold));
    // Run cron and verify event is still not allowed.
    $this->cronRun();
    $this->assertFalse(flood_is_allowed($name, $threshold));
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._

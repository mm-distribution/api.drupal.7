# DrupalSetMessageTest::testSetRemoveMessages()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 3153–3159 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L3153-L3159)
- **Class:** [DrupalSetMessageTest](../DrupalSetMessageTest.md)
- **Module/theme:** system

## Signature

```php
function testSetRemoveMessages()
```

## Documentation

```text
Tests setting messages and removing one before it is displayed.
```

## Code

```php
  function testSetRemoveMessages() {
    // The page at system-test/drupal-set-message sets two messages and then
    // removes the first before it is displayed.
    $this->drupalGet('system-test/drupal-set-message');
    $this->assertNoText('First message (removed).');
    $this->assertText('Second message (not removed).');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._

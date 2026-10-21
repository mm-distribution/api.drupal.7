# SystemAdminTestCase::testCompactMode()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 2925–2939 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L2925-L2939)
- **Class:** [SystemAdminTestCase](../SystemAdminTestCase.md)
- **Module/theme:** system

## Signature

```php
function testCompactMode()
```

## Documentation

```text
Test compact mode.
```

## Code

```php
  function testCompactMode() {
    $this->drupalGet('admin/compact/on');
    $this->assertTrue($this->cookies['Drupal.visitor.admin_compact_mode']['value'], 'Compact mode turns on.');
    $this->drupalGet('admin/compact/on');
    $this->assertTrue($this->cookies['Drupal.visitor.admin_compact_mode']['value'], 'Compact mode remains on after a repeat call.');
    $this->drupalGet('');
    $this->assertTrue($this->cookies['Drupal.visitor.admin_compact_mode']['value'], 'Compact mode persists on new requests.');

    $this->drupalGet('admin/compact/off');
    $this->assertEqual($this->cookies['Drupal.visitor.admin_compact_mode']['value'], 'deleted', 'Compact mode turns off.');
    $this->drupalGet('admin/compact/off');
    $this->assertEqual($this->cookies['Drupal.visitor.admin_compact_mode']['value'], 'deleted', 'Compact mode remains off after a repeat call.');
    $this->drupalGet('');
    $this->assertTrue($this->cookies['Drupal.visitor.admin_compact_mode']['value'], 'Compact mode persists on new requests.');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._

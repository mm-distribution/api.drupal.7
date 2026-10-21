# ConfirmFormTest::testConfirmForm()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 3186–3193 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L3186-L3193)
- **Class:** [ConfirmFormTest](../ConfirmFormTest.md)
- **Module/theme:** system

## Signature

```php
function testConfirmForm()
```

## Documentation

```text
Tests that the confirm form does not use external destinations.
```

## Code

```php
  function testConfirmForm() {
    $this->drupalGet('user/1/cancel');
    $this->assertCancelLinkUrl(url('user/1'));
    $this->drupalGet('user/1/cancel', array('query' => array('destination' => 'node')));
    $this->assertCancelLinkUrl(url('node'));
    $this->drupalGet('user/1/cancel', array('query' => array('destination' => 'http://example.com')));
    $this->assertCancelLinkUrl(url('user/1'));
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._

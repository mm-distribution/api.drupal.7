# BlockHTMLIdTestCase::testHTMLId()

- **Type:** Method
- **File:** [`modules/block/block.test`](../_file.md), lines 708–711 · [local source](../../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L708-L711)
- **Class:** [BlockHTMLIdTestCase](../BlockHTMLIdTestCase.md)
- **Module/theme:** block

## Signature

```php
function testHTMLId()
```

## Documentation

```text
Test valid HTML id.
```

## Code

```php
  function testHTMLId() {
    $this->drupalGet('');
    $this->assertRaw('block-block-test-test-html-id', 'HTML id for test block is valid.');
  }
```

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._

# PageTitleFiltering::tearDown()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 1613–1618 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L1613-L1618)
- **Class:** [PageTitleFiltering](../PageTitleFiltering.md)
- **Module/theme:** system

## Signature

```php
function tearDown()
```

## Documentation

```text
Reset page title.
```

## Code

```php
  function tearDown() {
    // Restore the page title.
    drupal_set_title($this->saved_title, PASS_THROUGH);

    parent::tearDown();
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._

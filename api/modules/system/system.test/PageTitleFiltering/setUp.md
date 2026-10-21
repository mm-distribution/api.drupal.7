# PageTitleFiltering::setUp()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 1602–1608 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L1602-L1608)
- **Class:** [PageTitleFiltering](../PageTitleFiltering.md)
- **Module/theme:** system

## Signature

```php
function setUp()
```

## Documentation

```text
Implement setUp().
```

## Code

```php
  function setUp() {
    parent::setUp();

    $this->content_user = $this->drupalCreateUser(array('create page content', 'access content', 'administer themes', 'administer site configuration'));
    $this->drupalLogin($this->content_user);
    $this->saved_title = drupal_get_title();
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._

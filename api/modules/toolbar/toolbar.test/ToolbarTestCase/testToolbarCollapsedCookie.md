# ToolbarTestCase::testToolbarCollapsedCookie()

- **Type:** Method
- **File:** [`modules/toolbar/toolbar.test`](../_file.md), lines 26–40 · [local source](../../../../../source/modules/toolbar/toolbar.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/toolbar/toolbar.test#L26-L40)
- **Class:** [ToolbarTestCase](../ToolbarTestCase.md)
- **Module/theme:** toolbar

## Signature

```php
function testToolbarCollapsedCookie()
```

## Documentation

```text
Tests toggling the toolbar collapsed cookie.
```

## Code

```php
  function testToolbarCollapsedCookie() {
    $this->drupalGet('toolbar/toggle');
    $set_cookie = $this->drupalGetHeader('set-cookie', TRUE);
    $this->assertTrue((strpos('Drupal.toolbar.collapsed=1; path=' . base_path() . '; SameSite=Lax', $set_cookie) !== FALSE), 'Toolbar cookie set to collapsed by default.');

    // The next request should toggle the toolbar.collapsed cookie to off.
    $this->drupalGet('toolbar/toggle');
    $set_cookie = $this->drupalGetHeader('set-cookie', TRUE);
    $this->assertTrue((bool) preg_match('#Drupal.toolbar.collapsed=deleted; expires=Thu, 01.Jan.1970 00:00:01 GMT;( Max-Age=0;)? path=' . str_replace('/', '\/', base_path()) . '; SameSite=Lax#', $set_cookie), 'Toolbar cookie toggled to off (deleted).');

    // The next request should toggle the toolbar.collapsed cookie back to 1.
    $this->drupalGet('toolbar/toggle');
    $set_cookie = $this->drupalGetHeader('set-cookie', TRUE);
    $this->assertTrue((strpos('Drupal.toolbar.collapsed=1; path=' . base_path() . '; SameSite=Lax', $set_cookie) !== FALSE), 'Toolbar cookie toggled to 1.');
  }
```

---
_Drupal 7.103 · [modules/toolbar/toolbar.test](https://github.com/drupal/drupal/blob/7.103/modules/toolbar/toolbar.test) · Licensed GPL-2.0-or-later (see LICENSE)._
